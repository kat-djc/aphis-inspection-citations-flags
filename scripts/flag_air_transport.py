import pandas as pd
import re
from typing import List, Dict, Union
import os
import glob


class RuleBasedClassifier:
    def __init__(self):
        # Positive rules - if satisfied, classify as 1
        self.positive_rules = {
            'airport_terms': r'\b(airport|airline|aircraft|international terminal|passenger terminal)\b',
            'transport_terms': r'\b(air transport|flight|air cargo)\b',
            'document_terms': r'\b(waybill|airway bill|awb)\b'
        }
        
        # Negative rules - if satisfied, override to 0
        self.negative_rules = {
            'no_adult': r'a responsible adult was not available to accompany aphis officials'
        }
    
    def preprocess_text(self, text: str) -> str:
        if not isinstance(text, str):
            return ""
        text = text.lower()
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

    results_df['air_transport_flag'] = results.apply(lambda x: x['classification'])
    results_df['classification_explanation'] = results.apply(lambda x: x['explanation'])
    results_df['matched_positive_rules'] = results.apply(lambda x: x['matched_positive'])
    results_df['matched_negative_rules'] = results.apply(lambda x: x['matched_negative'])
    return results_df


def get_latest_file(directory: str, prefix: str, extension: str) -> str:
    """
    Find the latest file in a directory matching a prefix and extension.

    Args:
        directory: Directory to search
        prefix: File prefix to match
        extension: File extension to match

    Returns:
        Path to the latest matching file
    """
    files = [
        os.path.join(directory, f) for f in os.listdir(directory)
        if f.startswith(prefix) and f.endswith(extension)
    ]
    if not files:
        raise FileNotFoundError(f"No files found with prefix '{prefix}' and extension '{extension}' in '{directory}'.")

    return max(files, key=os.path.getmtime)

if __name__ == "__main__":
    try:
        # Locate the latest file with a timestamp
        directory = '../data/flagging_process/new_rows'
        pattern = 'inspections_citations_new_rows_*.csv'
        latest_file = get_latest_file(directory, pattern)
        
        print(f"Reading latest file: {latest_file}")
        # Load the latest data
        new_inspections_citations = pd.read_csv(latest_file)

        # Classify
        classified_df = classify_inspection_narratives(new_inspections_citations)

        # Print sanity check
        print("----------------------------------------------------------------------------")
        print("Sanity Check for 'flag_air_tranport.py':")
        print()
        print(f"Total records: {len(classified_df)}")
        print(f"Records flagged as air transport: {classified_df['air_transport_flag'].sum()}")
        print(f"Percentage flagged: {(classified_df['air_transport_flag'].sum() / len(classified_df) * 100):.2f}%")
        print("----------------------------------------------------------------------------")

        # Print a few examples of flagged records
        print("Example Matched Records:")
        matched_examples = classified_df[classified_df['air_transport_flag'] == 1].head()
        for _, row in matched_examples.iterrows():
            print(f"Narrative: {row['narrative'][:200]}...")  
            print(f"Matched Rules: {row['matched_positive_rules']}")
            print(f"Classification Explanation: {row['classification_explanation']}")

        # Write classified_df to intial_flagged
        output_file = '../data/flagging_process/air_transport/initial_flagged.csv'
        classified_df.to_csv(output_file, index=False)
        print(f"Classified data saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")
