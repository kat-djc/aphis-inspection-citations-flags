import pandas as pd

def main():

    df_last_run_inspections_citations = pd.read_csv('../data/last_run_inspections_citations.csv')

    df_inspections_citations_new_rows = pd.read_csv('../data/new_rows/new_inspections_citations.csv')

    df_inspections_citations = pd.read_csv('../data/raw/aphis-inspection-reports/data/combined/inspections-citations.csv')

    df_combined = pd.concat([df_original, df_new_rows])

    print("----------------------------------------------------------------------------")
    print("Validation of append_flagged_rows.py logic...")
    print()
    print("Last run inspections-citations shape:", df_last_run_inspections_citations.shape)
    print("Combined dataframe shape:", df_combined.shape)
    print("This should match the above shape:", df_inspections_citations.shape)
    print()
    print("----------------------------------------------------------------------------")

if __name__ == "__main__":
    main()