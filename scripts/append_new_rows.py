import pandas as pd

def main():

    # File paths
    original_file_path = '../data/last_run_inspections_citations.csv'
    new_rows_file_path = '../data/new_rows/new_inspections_citations.csv'

    # Load datasets
    df_original = pd.read_csv(original_file_path)
    new_rows = pd.read_csv(new_rows_file_path)
    df_new = pd.read_csv('../aphis-inspection-reports/data/combined/inspections-citations.csv')

    # Print sanity check
    print("----------------------------------------------------------------------------")
    print("Sanity Check for 'append_new_rows.py':")
    print()
    print(f"Shape of last run inspections-citations data: {df_original.shape}")
    print(f"Shape of expected dataset (from new inspections-citations): {df_new.shape}")

    # Write new rows to last_run_inspections_citations
    new_rows.to_csv(original_file_path, mode='a', index=False, header=False)

    df_combined = pd.read_csv(original_file_path)
    print(f"Shape of combined data: {df_combined.shape}")
    print("Ensure the combined dataset matches the expected shape above.")
    print("----------------------------------------------------------------------------")


if __name__ == "__main__":
    main()