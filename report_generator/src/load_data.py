import os
import pandas as pd
import logging

def load_and_validate(config):
    raw_path = config['paths']['raw_data']
    data_type = config.get('data_type', 'general')
    req_cols = config.get('required_columns', {}).get(data_type, [])
    
    all_data = []
    
    if not os.path.exists(raw_path):
        logging.error(f"Raw data path {raw_path} does not exist.")
        raise FileNotFoundError(f"Raw data path {raw_path} does not exist.")
        
    for file in os.listdir(raw_path):
        filepath = os.path.join(raw_path, file)
        try:
            if file.endswith('.csv'):
                df = pd.read_csv(filepath)
            elif file.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(filepath)
            else:
                continue
                
            # Validate columns
            missing_cols = [c for c in req_cols if c not in df.columns]
            if missing_cols:
                logging.error(f"File {file} missing columns: {missing_cols}")
                continue
                
            # Check for empty values
            if df.isnull().values.any():
                logging.warning(f"File {file} contains missing values. Dropping rows with missing values in required columns.")
                df.dropna(subset=req_cols, inplace=True)
                
            # Check for duplicates
            if df.duplicated().any():
                logging.warning(f"File {file} contains duplicate rows. Removing duplicates.")
                df.drop_duplicates(inplace=True)
                
            all_data.append(df)
            logging.info(f"Successfully loaded and validated {file}")
            
        except Exception as e:
            logging.error(f"Error loading {file}: {e}")
            
    if not all_data:
        raise ValueError("No valid data loaded from raw directory.")
        
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df
