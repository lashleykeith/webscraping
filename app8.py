import urllib.request
from bs4 import BeautifulSoup as bs
#import re
import os.path
import shutil
import csv
import re

from contextlib import closing
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait

import base64

#headers = {}
#headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

playernames = []

with(open("gabes_data.csv")) as filename:
    contents = csv.reader(filename)
    for row in contents:
        if row: # not empty row
            name = row[0].strip()
            if name and name != "PlayerName":
                playernames.append(name)


with closing(Firefox()) as browser:
    for footballplayer in playernames:

        url = "https://www.google.com/search?source=lnms&tbm=isch&q=nfl%20" + footballplayer

        browser.get(url)
 
        WebDriverWait(browser, timeout=10)

        page_source = browser.page_source
        soup = bs(page_source, "html.parser")

        #images = [a['src'] for a in soup.find_all("img", {"src": re.compile("om")})]
        images = [a['src'] for a in soup.find_all("img", {"src": re.compile("base64")})]

        for number, url in enumerate(images[:5], 1):
            
            filename = "nfl_%s_img_%s.jpg" %(footballplayer, number)
            print('filename:', filename)
            
            if url.startswith('http'):
                with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
                    
            elif url.startswith('//'):
                print('src:', parts[0])
                url = 'https:' + url
                with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
                    
            elif url.startswith('data'):
                parts = url.split(',')
                print('src:', parts[0])
               
                data = base64.b64decode(parts[1])
                with open(filename, 'wb') as out_file:
                    out_file.write(data)
                    
            else:
                print('unknow src:', url)
                
    input('\nPress ENTER to close ')
