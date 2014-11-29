#!/usr/bin/python

import base64
import time
from selenium import webdriver

SCORE_FILE = '/var/www/scores'

def visitSite(link):
    flag = "tesseract2014{LetsJustAllUseCarrierPigeons}"
    driver = webdriver.PhantomJS()
    driver.get("http://ctf1.mit.edu/highscore.php")
    driver.add_cookie({'name':'isadmin', 'value':'true', 'path':'/'})
    driver.add_cookie({'name':'flag', 'value':flag, 'path':'/'})
    driver.get(link)
    return '+'

while True:
    f = open(SCORE_FILE)
    data = f.read().split('\n')
    f.close()
    newdata = ""
    for l in data:
        real = base64.b64decode(l).split(':::SECRET:::')
        if real[-1] == '0':
            real[-1] = visitSite(real[-2])
        newdata += base64.b64encode(':::SECRET:::'.join(real)) + "\n"
    
    f = open(SCORE_FILE, 'w')
    f.write(newdata)
    f.close()
        

    time.sleep(10)
