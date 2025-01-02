import pandas as pd

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
    # If unique_col is provided, compare based on that column.
    if unique_col:
        # Use a left anti join to get rows from new_df that are not in original_df
        new_rows = new_df[~new_df[unique_col].isin(original_df[unique_col])]
    else:
        # If no unique column, compare the entire row
        new_rows = pd.concat([new_df, original_df]).drop_duplicates(keep=False)

    return new_rows

def main():
    # Example usage:
    # Assuming 'df_original' and 'df_new' are the dataframes you are comparing
    # You can load your dataframes from CSV or other sources here

    df_original = pd.read_csv('../data/last_run_inspections_citations.csv')

    df_new = pd.read_csv('../data/raw/aphis-inspection-reports/data/combined/inspections-citations.csv')

    # Extracting the new rows based on the shape of original_df
    new_rows = extract_new_rows(df_original, df_new)

    new_rows.to_csv("../data/new_rows/new_inspections_citations.csv")

    # Output the new rows
    print("----------------------------------------------------------------------------")
    print("Validation of extract_new_rows.py logic...")
    print()
    print("new_rows.shape:", new_rows.shape)
    print()
    print("----------------------------------------------------------------------------")

if __name__ == "__main__":
    main()