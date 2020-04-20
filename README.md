# PDBJ-scraper
Small tools to bulk-submission, scraping and stat data from [PDBJ.org](https://pdbj.org/)  
https://github.com/Song-Liyang/PDBJ-scraper  
This program was written by Song Liyang (songly@pku.edu.cn), Peking University.

[PDBJ](https://pdbj.org/)(Protein Data Bank Japan) is a database of experimentally determined protein structures.

### Usage

##### Data fetching
[pdbj_open.py](https://github.com/Song-Liyang/PDBJ-scraper/blob/master/pdbj_open.py) is the web scraper to download data from each query link.  

PDBJ-scraper need WebDriver to connect with PDBJ server. Please check your Chrome browser version and download related [ChromeDriver](https://chromedriver.chromium.org/) to your Python directory.  
Before use, please specify these parameters in the script:

```
FILEDIR = "D://pdbj_bot//test"
INPUT = "StrucNavi_PDBj_link.txt"
```
The input file is a `.txt` file with a list of PDBJ query link, for example:
```
https://pdbj.org/struc-navi?jobid=SN-28892&query=3ujiH
```
is a query for "3ujiH".

All of the "Structure navigator results" data from this website will be saved in `./xml/` file folder.

##### Data stat
[pdbj_stat.py](https://github.com/Song-Liyang/PDBJ-scraper/blob/master/pdbj_stat.py) is a tool to parse and generate a summary from xml files above.
Before use, please specify these parameters in the script:
```
DATADIR = "D://pdbj_bot//test//xml"     # dir that stores fetched xml file, see readme
SAVEFILE = "D://pdbj_bot//test//summary.csv"    # output csv table
MIN_SCORE = 100    # entries has score under this will be omitted
MAX_ENTRY = 30      # save at most numbers of entries from each file
```
