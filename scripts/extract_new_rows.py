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
    # If unique_col is provided, compare based on that column
    if unique_col:
        # Use a left anti join to get rows from new_df that are not in original_df
        new_rows = new_df[~new_df[unique_col].isin(original_df[unique_col])]
    else:
        # If no unique column, compare the entire row
        new_rows = pd.concat([new_df, original_df])

    return new_rows

def main():
    # Load dataframes
    df_original = pd.read_csv('../data/last_run_inspections_citations.csv')
    df_new = pd.read_csv('../aphis-inspection-reports/data/combined/inspections-citations.csv')

    # Extract new rows
    new_rows = extract_new_rows(df_original, df_new)

    # Save new rows to a CSV file
    new_rows.to_csv("../data/new_rows/new_inspections_citations.csv", index=False)

    # Print sanity check
    print("----------------------------------------------------------------------------")
    print("Sanity Check for 'extract_new_rows.py':")
    print()
    print(f"Shape of last run's inspections-citations: {df_original.shape}")
    print(f"Shape of newest inspections-citations: {df_new.shape}")
    print()
    print(f"Shape of extracted new rows: {new_rows.shape}")
    print(f"Shape of expected results: {df_new.shape}")
    print("Ensure that the output aligns with the expected results.")
    print("----------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
