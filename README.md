# APHIS Inspection Reports Flags
This repository contains inspection reports published by the [US Department of Agriculture's Animal and Plant Health Inspection Service]([url](https://www.aphis.usda.gov/aphis/home/)), with added flags for phenomenons of public interest. It also contains the scripts for creating these flag columns. 

# Background
The Data Liberation Project's [APHIS Inspection Report Scraper](https://github.com/data-liberation-project/aphis-inspection-reports) extracts data from all [publicly-available inspection reports](https://efile.aphis.usda.gov/PublicSearchTool/s/inspection-reports) published by the US Department of Agriculture's [Animal and Plant Health Inspection Service](https://www.aphis.usda.gov/aphis/home/) (APHIS).

Each [inspection's citation]([url](https://github.com/data-liberation-project/aphis-inspection-reports/blob/main/data/combined/inspections-citations.csv)) include a "narrative" column containing text written by APHIS inspectors. Flagging recurring themes in the citation narratives will aid better understanding of the APHIS inspections report data, and potentially lead to more in-depth investigations. 

# Current Flags
This project is ongoing, with current flag logic being updated, and new flags being proposed and created. The flag columns currently available are: 
 * Extreme Temperatures:
   * With climates rapidly changing, failures to sufficiently protect animals from both low and high temperatures may become more common. This flag captures narratives related to extreme ambient temperatures and their consequences on animals.
 * Air Transport:
   * We noticed that the most frequent APHIS inspection sites were airlines. While being transported, animals can be subject to unsafe conditions, lack of food and water, or otherwise improper handling. Investigation into report narratives could reveal critical areas of improvement for airlines.

## Flagged Citations 
Generated CSV files are copies of the inspections-citations CSV, with new columns using the prefix 'flag_'.
  * Indicator columns for conditions. Conditions are specific to each flag and outlined in the Jupyter Notebooks that generate the CSV files. 
  * Flag columns is the name of the script, for example, the overheating flag is 'flag_overheating'

  
## Future Directions
* The following are potential future flags:
    * Absent/incorrectly written programs of veterinary care
    * Flaws in animal enclosures/physical environment
    * Accumulation of filth in enclosure, general lack of sanitation
    * Unauthorized sale or exhibition of animals
    * Expired medications
      
# Licensing 
The original APHIS reports are public domain. The Data Liberation Project–generated CSV files are available under Creative Commons’ CC BY-SA 4.0 license terms. This repository’s code is available under the MIT License terms.

Code contributed by Data Liberation Project volunteer Kat de Jesus Chua. 
