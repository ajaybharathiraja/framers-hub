import os
import logging
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

def create_report(results, config):
    output_path = config['paths']['output']
    project_name = config.get('project_name', 'Report')
    period = config.get('report_period', 'All Time')
    data_type = config.get('data_type', 'general')
    
    excel_path = os.path.join(output_path, 'report.xlsx')
    pdf_path = os.path.join(output_path, 'report.pdf')
    
    # 1. Create Excel
    with pd.ExcelWriter(excel_path) as writer:
        for sheet_name, df in results.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    logging.info(f"Excel report saved to {excel_path}")
    
    # 2. Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16, style='B')
    pdf.cell(200, 10, txt=project_name, ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Period: {period}", ln=True, align='C')
    pdf.ln(10)
    
    if data_type == 'accounting':
        gl = results['general_ledger']
        
        # Create a chart
        chart_path = os.path.join(output_path, 'balances_chart.png')
        plt.figure(figsize=(10, 6))
        plt.bar(gl['Account'], gl['Balance'], color=['green' if b >= 0 else 'red' for b in gl['Balance']])
        plt.title('Account Balances')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()
        
        pdf.set_font("Arial", size=14, style='B')
        pdf.cell(200, 10, txt="Trial Balance Summary", ln=True)
        pdf.set_font("Arial", size=10)
        
        # Table Header
        pdf.cell(60, 10, "Account", border=1)
        pdf.cell(40, 10, "Debit", border=1)
        pdf.cell(40, 10, "Credit", border=1)
        pdf.cell(40, 10, "Balance", border=1, ln=True)
        
        for _, row in gl.iterrows():
            pdf.cell(60, 10, str(row['Account']), border=1)
            pdf.cell(40, 10, f"${row['Debit']:.2f}", border=1)
            pdf.cell(40, 10, f"${row['Credit']:.2f}", border=1)
            pdf.cell(40, 10, f"${row['Balance']:.2f}", border=1, ln=True)
            
        pdf.ln(10)
        pdf.image(chart_path, w=170)
        
    else:
        pdf.cell(200, 10, txt="Data Summary (See Excel for details)", ln=True)
        
    pdf.output(pdf_path)
    logging.info(f"PDF report saved to {pdf_path}")
