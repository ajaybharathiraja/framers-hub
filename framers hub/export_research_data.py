import os
import django
import pandas as pd
import warnings

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uzhavarhub_project.settings')
django.setup()

from backend.models import ResearchEvent, TAMSurvey

def export_data():
    events = ResearchEvent.objects.all().values(
        'user_id', 'user__username', 'user__role', 'event_type', 'timestamp', 'metadata'
    )
    surveys = TAMSurvey.objects.all().values(
        'user_id', 'perceived_usefulness', 'perceived_ease_of_use', 'comments', 'created_at'
    )
    
    if not events:
        print("WARNING: The ResearchEvent table is empty. Data is not ready for analysis.")
        return
        
    df_events = pd.DataFrame(list(events))
    df_events = df_events.rename(columns={'timestamp': 'event_timestamp'})
    
    if surveys:
        df_surveys = pd.DataFrame(list(surveys))
        df_surveys = df_surveys.rename(columns={'created_at': 'survey_timestamp'})
        df_surveys = df_surveys.drop_duplicates(subset=['user_id'], keep='last')
        
        # Merge on user_id
        df_merged = pd.merge(df_events, df_surveys, on='user_id', how='left')
    else:
        print("WARNING: The TAMSurvey table is empty.")
        df_merged = df_events
        df_merged['perceived_usefulness'] = None
        df_merged['perceived_ease_of_use'] = None
        df_merged['comments'] = None
        df_merged['survey_timestamp'] = None
        
    if len(df_merged) < 10:
        print(f"WARNING: The dataset has fewer than 10 rows ({len(df_merged)} rows). Data is not ready for robust analysis.")
        
    output_file = 'research_data_export.csv'
    df_merged.to_csv(output_file, index=False)
    print(f"Successfully exported data to {output_file}")

if __name__ == "__main__":
    export_data()
