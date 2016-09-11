#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random

# Chrome Profile
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=PATH") #Path to your chrome profile

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path='DRIVER_PATH', chrome_options=options)

# go to the google home page
driver.get(r"http://websearch.rakuten.co.jp")

# Scroll down to right of page
driver.execute_script("window.scrollTo(document.body.scrollWidth, 0);")

# Login (todo: run a check for logout element; if available, login)
"""login = driver.find_element_by_class_name('logout').click()
time.sleep(random.uniform(1,3))

username1 = driver.find_element_by_name('u')
username1.send_keys(r"USER")

password1 = driver.find_element_by_name('p')
password1.send_keys("PASS")
password1.submit()"""

# Search (todo: use BS to grab search terms)
dsearch = [#Search terms here]
searchbar0 = driver.find_element_by_class_name('sftxt')
searchbar0.send_keys(dsearch[0])
searchbar0.submit()


count = 1
while (count < 32):
    clearbtn = driver.find_element_by_id('cbtn').click()
    searchbar1 = driver.find_element_by_xpath('//*[@id="srchformtxt_qt"]')
    searchbar1.send_keys(dsearch[count])
    searchbar1.submit()
    time.sleep(random.uniform(1,5))
    count += 1

