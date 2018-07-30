from bs4 import BeautifulSoup
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

from contextlib import closing
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait




import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'



##
##data = urllib.request.urlopen("https://www.tcsheriff.org/inmate-jail-info/ice-listing")
##
##datastring = data.read()
##
##soup = BeautifulSoup(datastring, "html.parser")
##
######print(soup.get_text())

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
##print(playernames[0:15])

##
##raise KeyboardInterrupt

##footballplayer = "Joe Montana"

for footballplayer in playernames:
##    url = ("https://www.google.com/search?q=nfl+%s&biw=1920&bih=1009&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi338XG0-3KAhVGvYMKHaqRCUEQ_AUIBigB" %(footballplayer))

    url = "https://www.google.com/search?q=nfl%20"+footballplayer+"&source=lnms&tbm=isch"

    # use firefox to get page with javascript generated content
    with closing(Firefox()) as browser:
        browser.get(url)
    ##     button = browser.find_element_by_name('.pdf')
    ##     button.click()
    # wait for the page to load
        WebDriverWait(browser, timeout=10) ##.until(
    ##         lambda x: x.find_element_by_id('.pdf'))
    # store it to string variable
        page_source = browser.page_source
        page_source = page_source[page_source.find("Search Results"):]
##        browser.get("http://www.uchicago.edu")

    soup = BeautifulSoup(page_source, "html.parser")


    ##print(soup.get_text())

##    pdflist= []
##
##    docnamelist = []

    images = [a['src'] for a in soup.find_all("img", {"src": re.compile("om")})]

    skipped_imgs=0
    item = 0

    images2=images[0:5]

##    for i in range(5):
##        print(images[i])

    for img in images2:
        
    ##        if not os.path.exists("%s" %(img)):
        print("adding %s to folder" %(img[0:100]))
        with urllib.request.urlopen(img) as response, open("nfl_%s_img_%s.jpg" %(footballplayer, item), 'wb') as out_file:
##            print(img)
            shutil.copyfileobj(response, out_file)
        item +=1
##        time.sleep(random.random())
    ##        else:
    ##            skipped_imgs = skipped_imgs + 1

