import pandas as pd

def main():
    # Load datasets
    df_last_run_inspections_citations = pd.read_csv('../data/last_run_inspections_citations.csv')
    df_inspections_citations_new_rows = pd.read_csv('../data/new_rows/new_inspections_citations.csv')
    df_inspections_citations = pd.read_csv('../aphis-inspection-reports/data/combined/inspections-citations.csv')

    # Combine datasets
    df_combined = pd.concat([df_last_run_inspections_citations, df_inspections_citations_new_rows])

    # Print validation results
    print("----------------------------------------------------------------------------")
    print("Sanity check for 'append_flagged_rows.py':")
    print()
    print(f"Shape of last run inspections-citations data: {df_last_run_inspections_citations.shape}")
    print(f"Shape of combined dataset: {df_combined.shape}")
    print(f"Shape of expected dataset (from inspections-citations): {df_inspections_citations.shape}")
    print()
    print("Ensure the combined dataset matches the expected shape above.")
    print("----------------------------------------------------------------------------")

if __name__ == "__main__":
    main()