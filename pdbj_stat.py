import xml.etree.cElementTree as ET
import requests
import re
import os
import pandas as pd

DATADIR = "D://pdbj_bot//test//xml"     # dir that stores fetched xml file, see readme
SAVEFILE = "D://pdbj_bot//test//summary.csv"    # output csv table
MIN_SCORE = 100    # entries has score under this will be omitted
MAX_ENTRY = 30      # save at most numbers of entries from each file

# get description title of a certain template from PDBJ server
def get_title(template):
    url = f"https://pdbj.org/rest/displayPDBfile?format=mmjson-plus-noatom&id={template}"
    connection_attempts = 0
    while connection_attempts < 4:    # attempt 4 times to fetch the title
        try:
            r = requests.get(url,timeout=120).text
            pattern = re.compile(r'"title":\[.*?\]')
            result = pattern.findall(r)[1]
            str = result.split("\"")[3]
            return str
        except Exception as Ex:
            connection_attempts += 1
            print(f'Error fetching title of {template}.Attempt #{connection_attempts}.')
    return f"Fail to get title! Template name {template} maybe obsolete"


# main
filelist = os.listdir(DATADIR)
df = pd.DataFrame(columns=['query', 'template', 'nerScore', 'nerRatio', 'sequenceId', 'RMSD', 'score', 'title'])
rowNum = 1

for file in filelist:
    filename = file
    query = filename.rstrip("_aqout_1.xml")
    xml_file = f'{DATADIR}//{filename}'
    print(f"processing xml file {xml_file}")
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for i in range(1, MAX_ENTRY + 1):
        if int(root[i][6].text) < MIN_SCORE:
            pass
        else:
            template = list(root[i][0].attrib.values())[0]
            chain = root[i][0][0].text
            name = template + chain
            nerScore = root[i][1].text
            nerRatio = root[i][2].text
            sequenceId = root[i][3].text
            caRMSD = root[i][4].text
            align = root[i][5].text
            link = f'https://pdbj.org/stnavix/{align}'
            score = root[i][6].text
            title = get_title(template)
            df.loc[rowNum] = (query, name, nerScore, nerRatio, sequenceId, caRMSD, score, title)
            rowNum += 1


df.to_csv(f'{SAVEFILE}', index=False)
print(f"csv file saved as {SAVEFILE}")
