import pandas as pd
import re
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

# Apply classification to the new_inspections_citations
def classify_inspection_narratives():
  
    classifier = RuleBasedClassifier()
    
    # Create result DataFrame with all columns from original plus new classification columns
    results_df = new_inspections_citations.copy()
    
    # Apply classification to each row
    results = results_df['narrative'].apply(classifier.apply_rules)
    
    # Add classification columns
    results_df['temperature_flag'] = results.apply(lambda x: x['classification'])
    results_df['classification_explanation'] = results.apply(lambda x: x['explanation'])
    results_df['matched_positive_rules'] = results.apply(lambda x: x['matched_positive'])
    results_df['matched_negative_rules'] = results.apply(lambda x: x['matched_negative'])
    
    return results_df

if __name__ == "__main__":
    # Read the data
    data_path = "../data/new_rows/new_inspections_citations.csv"
    new_inspections_citations = pd.read_csv(data_path)
    
    # Run classification
    classified_df = classify_inspection_narratives()
    
    # Print sanity check
    print("----------------------------------------------------------------------------")
    print("\n Sanity Check for 'flag_extreme_temperatures.py':")
    print()
    print(f"Total records: {len(classified_df)}")
    print(f"Records flagged for temperature issues: {classified_df['temperature_flag'].sum()}")
    print(f"Percentage flagged: {(classified_df['temperature_flag'].mean() * 100):.2f}%")
    print("----------------------------------------------------------------------------")
    
   # Print a few examples of flagged records
    print("\nExample Matched Records:")
    matched_examples = classified_df[classified_df['temperature_flag'] == 1].head()
    for _, row in matched_examples.iterrows():
        print(f"\nNarrative: {row['narrative'][:200]}...")  
        print(f"Matched Rules: {row['matched_positive_rules']}")
        print(f"Classification Explanation: {row['classification_explanation']}")

    # Write classified_df to intial_flagged
    classified_df.to_csv('../data/flagged/extreme_temperatures/initial_flagged.csv', index=False)