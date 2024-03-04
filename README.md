# Narrative Flagging
This repository contains citations with code for creating various flags for inspections data from USDA's Animal and Plant Health Inspection Service. 

## Motivation


## Flagged Citations CSVs
Generated CSV files are copies of inspections-citations CSV, with new columns have the prefix 'flag_'.
  * Indicator columns for conditions. Conditions are specific to each flag and outlined in the Jupyter Notebooks that generate the CSVs. 
  * Flag columns is the name of the script, for example, the overheating flag is 'flag_overheating'
  
## Future Directions
* The APHIS inspection report data is continually updated. The keywords used in the heat/temperature flag should be reviewed and refined periodically, in case of data shift. The following are flags we will be working on. 
    * Transport of animals
    * Absent/incorrectly written programs of veterinary care
    * Flaws in animal enclosures/physical environment
    * Inspection failure due to unavailable "responsible adult"
    * Accumulation of filth in enclosure, general lack of sanitation
    * Unauthorized sale or exhibition of animals
    * Expired medications
    * Incomplete inventory of animals
      
# Licensing 
The Data Liberation Project–generated CSV files are available under Creative Commons’ CC BY-SA 4.0 license terms. This repository’s code is available under the MIT License terms.

Code contributed by Data Liberation Project volunteer Kat de Jesus Chua. 
