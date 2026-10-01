import logging
import pandas as pd
import os

def process_data(df, config):
    data_type = config.get('data_type', 'general')
    processed_path = config['paths']['processed_data']
    
    logging.info(f"Processing data as type: {data_type}")
    
    results = {}
    
    if data_type == 'accounting':
        # Ensure Debit and Credit are numeric
        df['Debit'] = pd.to_numeric(df['Debit'], errors='coerce').fillna(0)
        df['Credit'] = pd.to_numeric(df['Credit'], errors='coerce').fillna(0)
        
        total_debit = df['Debit'].sum()
        total_credit = df['Credit'].sum()
        
        logging.info(f"Total Debits: {total_debit}, Total Credits: {total_credit}")
        
        if abs(total_debit - total_credit) > 0.01:
            logging.error("Trial Balance Error: Debits do not equal Credits!")
            raise ValueError(f"Debits ({total_debit}) != Credits ({total_credit})")
            
        # General Ledger
        gl = df.groupby('Account').agg({'Debit': 'sum', 'Credit': 'sum'}).reset_index()
        gl['Balance'] = gl['Debit'] - gl['Credit']
        
        results['journal_entries'] = df
        results['general_ledger'] = gl
        
        # Save processed data
        df.to_csv(os.path.join(processed_path, 'journal_entries.csv'), index=False)
        gl.to_csv(os.path.join(processed_path, 'general_ledger.csv'), index=False)
    else:
        # General processing
        summary = df.describe(include='all').reset_index()
        results['summary'] = summary
        results['data'] = df
        summary.to_csv(os.path.join(processed_path, 'summary.csv'), index=False)
        
    return results
