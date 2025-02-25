import pandas as pd
import os
import argparse
import shutil

def append_new_rows(original_file_path, new_rows_file_path, combined_file_path=None):
    """
    Appends new rows to the original file and prints shape details.
    
    Parameters:
        original_file_path (str): Path to the original dataset.
        new_rows_file_path (str): Path to the new rows dataset.
        combined_file_path (str, optional): Path to a new dataset to append. Defaults to None.
    """
    try:
        # Check if the original file exists
        if not os.path.exists(original_file_path):
            print(f"Original file does not exist at {original_file_path}. Creating it with headers from {new_rows_file_path}.")
            # Load new rows to extract headers
            new_rows = pd.read_csv(new_rows_file_path)
            new_rows.iloc[0:0].to_csv(original_file_path, index=False)  # Write only the header
            print(f"File created at {original_file_path} with headers from {new_rows_file_path}.")
        
        # Load datasets
        df_original = pd.read_csv(original_file_path)
        new_rows = pd.read_csv(new_rows_file_path)

        # Print sanity check
        print("----------------------------------------------------------------------------")
        print("Sanity Check for 'append_new_rows.py':")
        print()
        print(f"Reading original file from: {original_file_path}")
        print(f"Reading new rows file from: {new_rows_file_path}")
        print(f"Combined file path: {combined_file_path}")
        print()
        print(f"Shape of original dataset: {df_original.shape}")
        print(f"Shape of new rows dataset: {new_rows.shape}")

        # Check that columns match 
        if not df_original.empty and list(df_original.columns) != list(new_rows.columns):
            raise ValueError("Column mismatch between original dataset and new rows dataset.")

        # Append new rows to the original dataset
        df_combined = pd.concat([df_original, new_rows], ignore_index=True)

        # Save the combined dataset
        output_path = combined_file_path
        df_combined.to_csv(output_path, index=False)

        print(f"Shape of combined dataset after appending: {df_combined.shape}")

        print("----------------------------------------------------------------------------")
        print("Appending operation completed successfully.")
        print("----------------------------------------------------------------------------")

    except Exception as e:
        # Log the error details
        print("----------------------------------------------------------------------------")
        print("An error occurred during the append operation:")
        print(f"Error: {e}")
        print("----------------------------------------------------------------------------")
        raise

def main():
    # Define command-line arguments
    parser = argparse.ArgumentParser(description="Append new rows to an existing dataset.")
    parser.add_argument('--original_file_path', type=str, required=True,
                        help="Path to the dataset to which new rows will be appended.")
    parser.add_argument('--new_rows_file_path', type=str, required=True,
                        help="Path to the new rows dataset.")
    parser.add_argument('--combined_file_path', type=str, default=None,
                        help="Optional: Path to save the combined dataset.")

    args = parser.parse_args()

    # Execute the append operation
    append_new_rows(args.original_file_path, args.new_rows_file_path, args.combined_file_path)


if __name__ == "__main__":
    main()