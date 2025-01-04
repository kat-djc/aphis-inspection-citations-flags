import pandas as pd
from datetime import datetime

def extract_new_rows(original_df, new_df, unique_col=None):
    """
    Extract new rows from new_df that are not in original_df.

    Parameters:
    original_df (pd.DataFrame): The original dataframe.
    new_df (pd.DataFrame): The new dataframe to compare with.
    unique_col (str, optional): The column that uniquely identifies each row (default is None).
    
    Returns:
    pd.DataFrame: DataFrame containing the new rows.
    """
    # If unique_col is provided, compare based on that column
    if unique_col:
        # Use a left anti join to get rows from new_df that are not in original_df
        new_rows = new_df[~new_df[unique_col].isin(original_df[unique_col])]
    else:
        # If no unique column, compare the entire row
        new_rows = pd.concat([new_df, original_df]).drop_duplicates(keep=False)

    return new_rows

def main():
    # File paths
    original_file_path = '../data/output/inspections_citations_latest.csv'
    new_file_path = '../aphis-inspection-reports/data/combined/inspections-citations.csv'

    # Load dataframes
    df_original = pd.read_csv(original_file_path)
    df_new = pd.read_csv(new_file_path)

    # Extract new rows
    new_rows = extract_new_rows(df_original, df_new)

    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_rows_file_path = f"../data/flagging_process/new_rows/inspections_citations_new_rows_{timestamp}.csv"
    
    # Print the generated file path
    print(f"Generated file path: {new_rows_file_path}")

    # Save new rows to a timestamped CSV file
    new_rows.to_csv(new_rows_file_path, index=False)

    # Print sanity check
    print("----------------------------------------------------------------------------")
    print("Sanity Check for 'extract_new_rows.py':")
    print()
    print(f"Shape of inspections_citations_latest: {df_original.shape}")
    print(f"Shape of inspections-citations from APHIS: {df_new.shape}")
    print()
    print(f"Shape of extracted new rows: {new_rows.shape}")
    print(f"New rows saved to: {new_rows_file_path}")
    print("----------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
