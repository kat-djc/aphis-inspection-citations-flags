import pandas as pd
import re
import os
from typing import List, Dict, Union

class RuleBasedClassifier:
    def __init__(self):
        # Positive rules - if satisfied, classify as 1
        self.positive_rules = {
            'temperature_value': r'\b(?!180\b)\d+(\.\d+)?\s*(f|degrees|fahrenheit|deg f|celsius)\b',
            'general_terms': r'\b(climatic|ambient temperature|temperature extremes|atmospheric temperature)\b',
            'heat_terms': r'\b(extreme heat|heat index|heat warning|excessive heat|hot weather|heat stroke|heat stress)\b',
            'cold_terms': r'\b(extreme cold|cold temperature|cold weather|low temperature|cold stress|frostbite|hyperthermia|hypothermic)\b',
            'weather_sources': r'\b(weather service|accuweather|noaa)\b'
        }

        # Negative rules - if satisfied, override to 0
        self.negative_rules = {
            'no_adult': r'a responsible adult was not available to accompany aphis officials'
        }

    def preprocess_text(self, text: str) -> str:
        """
        Preprocess text by lowercasing and normalizing spaces.

        Args:
            text: Input text to preprocess

        Returns:
            Preprocessed text
        """
        if not isinstance(text, str):
            return ""

        # Convert to lowercase
        text = text.lower()

        # Normalize spaces (split and rejoin to remove multiple spaces)
        text = ' '.join(text.split())

        return text

    def apply_rules(self, text: str) -> Dict[str, Union[int, List[str]]]:
            """
            Apply both positive and negative rules to text and return classification with explanation.
            
            Args:
                text: Input text to classify
                
            Returns:
                Dictionary containing classification and matched rules
            """
            # Preprocess the text
            text = self.preprocess_text(text)
            
            if not text:
                return {
                    'classification': 0,
                    'matched_positive': [],
                    'matched_negative': [],
                    'explanation': 'Invalid input'
                }
            
            # Track which rules were satisfied
            matched_positive = []
            matched_negative = []
            
            # Check positive rules
            is_positive = False
            for rule_name, pattern in self.positive_rules.items():
                if re.search(pattern, text):
                    matched_positive.append(rule_name)
                    is_positive = True
            
            # If no positive rules were satisfied, return early
            if not is_positive:
                return {
                    'classification': 0,
                    'matched_positive': [],
                    'matched_negative': [],
                    'explanation': 'No positive rules matched'
                }
            
            # Check negative rules
            for rule_name, pattern in self.negative_rules.items():
                if re.search(pattern, text):
                    matched_negative.append(rule_name)
            
            # Determine final classification
            final_classification = 1 if matched_positive and not matched_negative else 0
            
            # Create explanation
            if matched_negative:
                explanation = f"Initially matched positive rules {matched_positive} but overridden by negative rules {matched_negative}"
            else:
                explanation = f"Matched positive rules: {matched_positive}"
            
            return {
                'classification': final_classification,
                'matched_positive': matched_positive,
                'matched_negative': matched_negative,
                'explanation': explanation
            }

def classify_inspection_narratives(new_inspections_citations):
    """
    Apply classification rules to a DataFrame of inspection narratives.

    Args:
        new_inspections_citations: DataFrame containing narratives to classify

    Returns:
        DataFrame with classification results added
    """
    classifier = RuleBasedClassifier()

    # Create result DataFrame with all columns from original plus new classification columns
    results_df = new_inspections_citations.copy()

    # Apply classification to each row
    results = results_df['narrative'].apply(classifier.apply_rules)

    # Add classification columns
    results_df['extreme_temperatures_flag'] = results.apply(lambda x: x['classification'])
    results_df['classification_explanation'] = results.apply(lambda x: x['explanation'])
    results_df['matched_positive_rules'] = results.apply(lambda x: x['matched_positive'])
    results_df['matched_negative_rules'] = results.apply(lambda x: x['matched_negative'])

    return results_df

def get_latest_file(directory: str, prefix: str, extension: str) -> str:
    """
    Find the latest file in a directory matching a prefix and extension, with debugging output.

    Args:
        directory: Directory to search
        prefix: File prefix to match
        extension: File extension to match

    Returns:
        Path to the latest matching file
    """
    print(f"Looking for files in directory: {directory}")
    print(f"Prefix: {prefix}, Extension: {extension}")
    
    files = [
        os.path.join(directory, f) for f in os.listdir(directory)
        if f.startswith(prefix) and f.endswith(extension)
    ]
    print("Matching files found:", files)

    if not files:
        raise FileNotFoundError(f"No files found with prefix '{prefix}' and extension '{extension}' in '{directory}'.")

    latest_file = max(files, key=os.path.getmtime)
    print("Latest file selected:", latest_file)
    print()
    return latest_file


if __name__ == "__main__":
    try: 
        # Locate the latest file with a timestamp
        directory = '../data/flagging_process/new_rows/'

        # Check if the directory exists and print its contents
        if os.path.exists(directory):
            print(f"Contents of the directory '{directory}':")
            for file_name in os.listdir(directory):
                print(file_name)
                print()
        else:
            print(f"The directory '{directory}' does not exist.")
            print()

        prefix = 'inspections_citations_new_rows_'
        extension = '.csv'
        latest_file = get_latest_file(directory, prefix, extension)
        print(f"Reading latest file: {latest_file}")
        print()

        # Load the latest data
        new_inspections_citations = pd.read_csv(latest_file)

        # Classify
        classified_df = classify_inspection_narratives(new_inspections_citations)

        # Write classified_df to initial_flagged
        output_file = '../data/flagging_process/extreme_temperatures/initial_flagged.csv'
        classified_df.to_csv(output_file, index=False)
        print(f"Classified data saved to {output_file}")

        # Print sanity check
        print("----------------------------------------------------------------------------")
        print("Sanity Check for 'flag_extreme_temperatures.py':")
        print()
        print(f"Total records: {len(classified_df)}")
        print(f"Records flagged for temperature issues: {classified_df['extreme_temperatures_flag'].sum()}")
        print(f"Percentage flagged: {(classified_df['extreme_temperatures_flag'].sum() / len(classified_df) * 100):.2f}%")
        print("----------------------------------------------------------------------------")

        # Print a few examples of flagged records
        print("\nExample Matched Records:")
        matched_examples = classified_df[classified_df['extreme_temperatures_flag'] == 1].head()
        for _, row in matched_examples.iterrows():
            print(f"Narrative: {row['narrative'][:200]}...")
            print(f"Matched Rules: {row['matched_positive_rules']}")
            print(f"Classification Explanation: {row['classification_explanation']}")

    except Exception as e:
        print(f"Error: {e}")