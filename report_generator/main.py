import yaml
import logging
import os
from src.load_data import load_and_validate
from src.process import process_data
from src.generate_report import create_report

def main():
    # Setup logging
    os.makedirs('logs', exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/app.log'),
            logging.StreamHandler()
        ]
    )
    
    logging.info("Starting report generation process...")
    
    try:
        # Load config
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
            
        # 1. Load Data
        df = load_and_validate(config)
        
        # 2. Process Data
        results = process_data(df, config)
        
        # 3. Generate Report
        create_report(results, config)
        
        logging.info("Report generation completed successfully!")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
