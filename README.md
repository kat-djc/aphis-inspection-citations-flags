# APHIS Inspection Reports Flags
This repository contains inspection reports originally published by the US Department of Agriculture's [Animal and Plant Health Inspection Service](https://www.aphis.usda.gov/aphis/home/) (APHIS), collated by the Data Liberation Project's [APHIS Inspection Report Scraper]([url](https://github.com/data-liberation-project/aphis-inspection-reports)), with added flags for phenomenons of public interest. The repository also contains the scripts for creating these flags.

## Background
The Data Liberation Project's APHIS Inspection Report Scraper extracts and collects data from all [publicly-available inspection reports](https://efile.aphis.usda.gov/PublicSearchTool/s/inspection-reports). 

Each [inspection's citation]([url](https://github.com/data-liberation-project/aphis-inspection-reports/blob/main/data/combined/inspections-citations.csv)) includes a "narrative" column containing text details written by an APHIS inspector. The narrative column is highly informative and critical to understanding the story behind each citation. Flagging recurring themes will aid understanding of the APHIS data and may lead to more in-depth investigations. 

## Current Flags
This project is ongoing, with current flag logic being updated and new flags being proposed and created. The flags currently available are: 
 * Extreme Temperatures
   * With climates rapidly changing, failures to sufficiently protect animals from both low and high temperatures may become more common. This flag captures narratives related to extreme ambient temperatures and their consequences on animals.
 * Air Transport
   * Some of the most frequent APHIS inspection sites are airlines. While being transported, animals can be subject to unsafe conditions, lack of food and water, or otherwise improper handling. Investigation into report narratives could reveal critical areas of improvement for airlines.

## Flagged Citations 
The [flag script outputs]([url](https://github.com/kat-djc/aphis-inspection-reports-flags/tree/main/flagged_citations)) are copies of the inspections-citations CSV file, with new columns using the prefix 'flag_'. 
  * Columns with the prefix 'flag_cond' are indicator columns for the conditions used to assign the flag. Conditions are specific to each flag and outlined in the Jupyter Notebooks that generate the CSV files.
  
## Future Directions
* The following are potential future flags:
    * Absent/incorrectly written programs of veterinary care
    * Flaws in animal enclosures/physical environment
    * Accumulation of filth in enclosure, general lack of sanitation
    * Unauthorized sale or exhibition of animals
    * Expired medications
      
## Licensing 
The original APHIS reports are public domain. The Data Liberation Project–generated CSV files are available under Creative Commons’ CC BY-SA 4.0 license terms. This repository’s code is available under the MIT License terms.

## Questions?
File an issue in this repository or email Jeremy Singer-Vine at jsvine@gmail.com.

Code contributed by Data Liberation Project volunteer Kat de Jesus Chua, reachable at kathdjc@gmail.com.
