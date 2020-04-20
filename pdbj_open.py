from selenium import webdriver
import os


FILEDIR = "D://pdbj_bot//20200331"
INPUT = "StrucNavi_PDBj_link.txt"
os.makedirs(f'{FILEDIR}//xml', exist_ok=True)

inputfile = open(f'{FILEDIR}/{INPUT}')
inputlines = inputfile.readlines()
inputfile.close()

def open_driver(inputline):
    jobid = inputline.split('=')[-2].split('&')[0]
    query = inputline.split('=')[-1]
    url = "https://pdbj.org/stnavix/result/%s/%s_aqout_1.xml" % (jobid,query)
    print(url)

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    return

for inputline in inputlines:
    print(inputline)
    open_driver(inputline)
