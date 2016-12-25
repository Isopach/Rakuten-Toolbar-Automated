#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

# Chrome Profile
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=PATH") #Path to your chrome profile

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path='DRIVER_PATH', chrome_options=options)

# go to the rakuten search page
driver.get(r"http://websearch.rakuten.co.jp/Web?qt=%E3%81%BB%E3%82%93%E3%81%AE&x=0&y=0&col=OW&svx=101210&ref=top&hs=1")

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
dsearch = [u'ジーンズ',u'メイク',u'半袖',u'長袖',u'タンクトップ',u'フリース',u'ニットジャケット',u'スカート',u'トレーナー',u'クルーソックス',u'デニム',u'シューズ',u'レザー手袋',u'日本製',u'アンサンブル',u'ハイゲージ',u'レザークラフト',u'アップ',u'フレア',u'ロングカーディガン ',u'極細アクリル',u'キュプラ',u'ストレッチ',u'スキニーパンツ',u'ケース',u'シークレット',u'ナチュラル',u'ポッキリ',u'小物ケース',u'ツリー柄',u'半袖',u'ナチュラル'] #Fill in at least 32 search terms here
count = 1
while (count < 32):
    clearbtn = driver.find_element_by_id('cbtn').click()
    searchbar1 = driver.find_element_by_xpath('//*[@id="srchformtxt_qt"]')
    searchbar1.send_keys(dsearch[count])
    searchbar1.submit()
    time.sleep(random.uniform(1,5))
    count += 1

driver.quit()
