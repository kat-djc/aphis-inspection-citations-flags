import pandas as pd
from datetime import datetime
import sys
import os

def extract_new_rows(original_df, new_df):
    """
    Extract new rows from new_df that are not in original_df, assuming that the new rows
    are at the bottom of the new_df.

    Parameters:
    original_df (pd.DataFrame): The original dataframe.
    new_df (pd.DataFrame): The refreshed dataframe, where new rows are at the bottom.
    
    Returns:
    pd.DataFrame: DataFrame containing the new rows.
    """
    # Find the difference in the number of rows
    new_rows = new_df.iloc[len(original_df):]
    
    return new_rows

def main():
    # File paths
    original_file_path = '../data/output/inspections_citations_latest.csv'
    new_file_path = '../aphis-inspection-reports/data/combined/inspections-citations.csv'

    try:
        # Check if the original file exists
        if not os.path.exists(original_file_path):
            print(f"Original file does not exist at {original_file_path}. Creating it with headers from {new_file_path}.")
            # Load new file and save only the headers
            new_df = pd.read_csv(new_file_path)
            new_df.iloc[0:0].to_csv(original_file_path, index=False)  # Write only the header
            print(f"File created at {original_file_path} with headers from {new_file_path}.")

        # Load dataframes
        df_original = pd.read_csv(original_file_path)
        df_new = pd.read_csv(new_file_path)

        # Extract new rows
        new_rows = extract_new_rows(df_original, df_new)

        # Print sanity check
        print("----------------------------------------------------------------------------")
        print("Sanity Check for 'extract_new_rows.py':")
        print()
        print(f"Shape of inspections_citations_latest: {df_original.shape}")
        print(f"Shape of inspections-citations from APHIS: {df_new.shape}")
        print(f"Shape of extracted new rows: {new_rows.shape}")

        # Check if there are new rows
        if new_rows.shape[0] == 0:
            print("No new data. All flagged datasets are up to date.")
            sys.exit(0)  # Exit the script with a success status
        
        # Generate a timestamp for the filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_rows_file_path = f"../data/flagging_process/new_rows/inspections_citations_new_rows_{timestamp}.csv"
        
        # Print the generated file path
        print(f"Generated file path: {new_rows_file_path}")

        # Save new rows to a timestamped CSV file
        new_rows.to_csv(new_rows_file_path, index=False)

        print()
        print(f"New rows saved to: {new_rows_file_path}")
        print("----------------------------------------------------------------------------")

    except Exception as e:
        # Log the error details
        print("An error occurred during the extract new rows operation:")
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    main()
