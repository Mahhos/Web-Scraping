# from datetime import timedelta as TimeDelta
from datetime import date
from datetime import datetime as DateTime, timedelta as TimeDelta
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np 
import csv
#from bs4 import BeautifulSoup
from selenium import webdriver
import io
import unicodecsv as csv
from io import BytesIO
from cStringIO import StringIO
from selenium.webdriver.chrome.options import Options
import subprocess
 
 
cmdCommand1 = "taskkill /IM chromedriver.exe /f"
cmdCommand2 = "taskkill /IM chrome.exe /f"
sum=0
 
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + TimeDelta(n)
 
start_date = date(2017, 10, 29)
#end_date = date(2017, 11, 1)
end_date = date(2017, 11, 13)
sdate = date(2017, 11, 1)
wordlist = ["username", "password"]
for word in range(0, len(wordlist)):
    for i in daterange(start_date, end_date):
            sdate = sdate  + TimeDelta(days=4)
            edate = sdate + TimeDelta(days=4)
            if (int((date.today() - edate).days)) >= 0:
                # url = "https://crash-stats.mozilla.com/search/?user_comments=password&product=Firefox&product=SeaMonkey&product=Fennec&product=FennecAndroid&product=Thunderbird&date=%3E%3D"+str(sdate)+"T15%3A22%3A00.000Z&date=%3C"+str(edate)+"T15%3A22%3A00.000Z&_sort=-date&_facets=user_comments&_columns=product&_columns=date#facet-user_comments"
                # url = "https://crash-stats.mozilla.com/search/?user_comments=email&product=Firefox&product=SeaMonkey&product=Fennec&product=FennecAndroid&product=Thunderbird&date=%3E%3D"+str(sdate)+"T15%3A36%3A12.000Z&date=%3C"+str(edate)+"T15%3A36%3A12.000Z&_sort=-date&_facets=user_comments&_columns=product&_columns=date#facet-user_comments"
                url = "https://crash-stats.mozilla.com/search/?user_comments="+wordlist[word]+"&product=Firefox&product=SeaMonkey&product=Fennec&product=FennecAndroid&product=Thunderbird&date=%3E%3D"+str(sdate)+"T17%3A05%3A00.000Z&date=%3C"+str(edate)+"T17%3A05%3A00.000Z&_sort=-date&_facets=user_comments&_columns=product&_columns=date#facet-user_comments"
                chrome_path = r"C:\Users\Mahshid\Downloads\Compressed\chromedriver_win32\chromedriver.exe"
                encoding = 'utf-8'
                Chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                WINDOW_SIZE = "1920,1080"
                # url = "https://crash-stats.mozilla.com/search/?user_comments=password&product=Firefox&product=SeaMonkey&product=Fennec&product=FennecAndroid&product=Thunderbird&date=%3E%3D2017-09-25T20%3A36%3A12.000Z&date=%3C2017-09-28T20%3A36%3A12.000Z&_sort=-date&_facets=user_comments&_columns=product&_columns=date#facet-user_comments"
                chrome_options = Options() 
                chrome_options.add_argument("--headless") 
                chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
                chrome_options.binary_location = Chrome_path
                driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
               
                driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
                driver.maximize_window() #For maximizing window
                driver.implicitly_wait(20) #gives an implicit wait for 20 seconds
                driver.get(url)
                html = driver.page_source
                SMRtable = driver.find_element_by_xpath('//*[@id="facets-list-user_comments"]')
                source_code = SMRtable.get_attribute("outerHTML")
                #print source_code
                with open('fuck.csv', 'ab') as f:
                   writer = csv.writer(f, delimiter=' ')
                   count=0
                   for i in SMRtable.find_elements_by_xpath('.//tr'):
                       writer.writerow([(i.text)[2:-8].encode('utf-8').strip()])
                       count +=1
                   print "Word {w}: Date {first} and Count {second}".format(w = wordlist[word], first=edate, second=count)
                   sum = sum + count
                   driver.close()
                   f.close()
                   process1 = subprocess.Popen(cmdCommand1.split(), stdout=subprocess.PIPE)
                   process2 = subprocess.Popen(cmdCommand2.split(), stdout=subprocess.PIPE)
                   output, error = process1.communicate()
                   output, error = process2.communicate()
    print sum
    # process1 = subprocess.Popen(cmdCommand1.split(), stdout=subprocess.PIPE)
    # process2 = subprocess.Popen(cmdCommand2.split(), stdout=subprocess.PIPE)
    # output, error = process1.communicate()
    # output, error = process2.communicate()
     
               
                    #   writer.writerow([(i.text).encode('utf-8').strip()])
                    #   writer.writerows([i.text])