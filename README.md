# Narrative Flagging
The Data Liberation Project's [APHIS Inspection Report Scraper]([url](https://github.com/data-liberation-project/aphis-inspection-reports)) collects all publicly-available inspection reports published by the [US Department of Agriculture's Animal and Plant Health Inspection Service]([url](https://www.aphis.usda.gov/aphis/home/)). 

This repository contains CSV files with various flag columns, as well as the scripts used for creating these flag columns. Flag columns available: 
 * Overheating
 * Air Transit 

## Motivation
The narrative column contains important details to the inspection. Flagging phenomenons that have an identifiable public interest element that may spark future journalistic investigations. 

## Flagged Citations 
Generated CSV files are copies of inspections-citations CSV, with new columns have the prefix 'flag_'.
  * Indicator columns for conditions. Conditions are specific to each flag and outlined in the Jupyter Notebooks that generate the CSVs. 
  * Flag columns is the name of the script, for example, the overheating flag is 'flag_overheating'
  
## Future Directions
* The APHIS inspection report data is continually updated. The keywords used in the heat/temperature flag should be reviewed and refined periodically, in case of data shift.
* The following are potential future flags to be implemented: 
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
