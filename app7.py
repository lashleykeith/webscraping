from bs4 import BeautifulSoup as bs
import urllib
from urllib import request
import re
import csv
import os.path
import time
import datetime
import codecs
import urllib.request
import shutil
import PyPDF2
import random
##from pdfminer3k import PDFParser

import xlrd
import random

from contextlib import closing
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait




import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'


playernames = []
with(open("gabes_data.csv")) as filename:
    contents = csv.reader(filename)
    for row in contents:
        if row==[]:
            continue
        if row[0].strip()=="PlayerName":
            continue
        if row[0].strip()=="":
            continue
        playernames.append(row[0].strip())


for footballplayer in playernames:

    url = "https://www.google.com/search?q=nfl%20"+footballplayer+"&source=lnms&tbm=isch"

    with closing(Firefox()) as browser:
        browser.get(url)
 
        WebDriverWait(browser, timeout=10) ##.until(

        page_source = browser.page_source
        page_source = page_source[page_source.find("Search Results"):]

    soup = bs(page_source, "html.parser")



    images = [a['src'] for a in soup.find_all("img", {"src": re.compile("om")})]

    skipped_imgs=0
    item = 0

    images2=images[0:5]



    for img in images2:
        
        print("adding %s to folder" %(img[0:100]))
        with urllib.request.urlopen(img) as response, open("nfl_%s_img_%s.jpg" %(footballplayer, item), 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        item +=1
