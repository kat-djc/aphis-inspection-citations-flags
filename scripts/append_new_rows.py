import pandas as pd
import argparse

def append_new_rows(original_file_path, new_rows_file_path, combined_file_path=None):
    """
    Appends new rows to the original file and prints shape details.
    
    Parameters:
        original_file_path (str): Path to the original dataset.
        new_rows_file_path (str): Path to the new rows dataset.
        combined_file_path (str, optional): Path to a new dataset to append. Defaults to None.
    """

    # Load datasets
    df_original = pd.read_csv(original_file_path)
    new_rows = pd.read_csv(new_rows_file_path)
    print(f"Reading original file from: {original_file_path}")
    print(f"Reading new rows file from: {new_rows_file_path}")
    print(f"Combined file path: {combined_file_path}")


    # Print sanity check
    print("----------------------------------------------------------------------------")
    print("Sanity Check for 'append_new_rows.py':")
    print()
    print(f"Shape of original dataset: {df_original.shape}")
    print(f"Shape of new rows dataset: {new_rows.shape}")

    # Append new rows to the original dataset
    new_rows.to_csv(original_file_path, mode='a', index=False, header=False)

    # Load combined data (optional: if combined_file_path is provided, load that as well)
    if combined_file_path:
        df_combined = pd.read_csv(combined_file_path)
        print(f"Shape of combined data: {df_combined.shape}")
    else:
        # Reload the updated original file after appending
        df_combined = pd.read_csv(original_file_path)
    
    print(f"Shape of data after appending: {df_combined.shape}")
    print("Ensure the combined dataset matches the expected shape above.")
    print("----------------------------------------------------------------------------")


def main():
    
    parser = argparse.ArgumentParser(description="Update dataset with new rows dataset.")
    parser.add_argument('--original_file_path', type=str, help="Path to the dataset that will be updated with the new rows dataset")
    parser.add_argument('--new_rows_file_path', type=str, help="Path to the new rows dataset")
    parser.add_argument('--combined_file_path', type=str, help="Path to the combined dataset (optional)", default=None)

    args = parser.parse_args()

    # Call the function to append rows
    append_new_rows(args.original_file_path, args.new_rows_file_path, args.combined_file_path)


if __name__ == "__main__":
    main()
