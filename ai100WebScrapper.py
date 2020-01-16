#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import os
import wget

# 這裡原本是要用來檢查看他有沒有我要的東西的，之後改用別的方式
# def check_exists_by_xpath(xpath):
#     try:
#         driver.find_elements_by_xpath(xpath)
#     except NoSuchElementException:
#         return False
#     return True

# 更改下載預設路徑
options = webdriver.ChromeOptions()
destination = 'D:\\selenium\\ai100'  # 下載位置
prefs = {'download.default_directory': destination}
options.add_experimental_option('prefs', prefs)

# 登入網站
login_url = 'https://ai100-3.cupoy.com/'
driver = webdriver.Chrome(chrome_options=options) # 以特定option打開chrome
driver.get(login_url)
time.sleep(20)  # 停下來輸入賬密

d = 107  # 天數
for x in range(54, d+1):
    # 網址
    url0 = "https://ai100-3.cupoy.com/mission/D"
    url_pdf = url0 + str(x)  # 每一天pdf的網址
    sampleCode_url = 'https://ai100-3.cupoy.com/samplecodelist/D' + str(x)
    day = 'Day' + str(x)

    # open new window
    driver.execute_script("window.open('');")

    # Switch to the new window and open new url
    driver.switch_to.window(driver.window_handles[1])

    driver.get(url_pdf)  # 前往網址
    time.sleep(4)   # 讓他有足夠的時間load網頁

    # html_text = driver.page_source
    #
    # soup = BeautifulSoup(html_text, 'html.parser')
    #
    # q = (soup.select_one("a[href*=PDF]")).get('href')
    # pdf_url = "https:" + q
    # print("pdf_url:"+pdf_url)
    # driver.get(pdf_url)
    # driver.find_element_by_class_name('body').send_keys(Keys.CONTROL + 's')

    test1 = driver.find_elements_by_tag_name('iframe')  # 找到pdf的框架

    driver.switch_to.frame(0)  # 轉移控制權

    download_pdf_btn = driver.find_elements_by_id('download')[0].click()  # 找到下載按鈕並按下

    print("Pdf download: " + day)

    # cd進到資料夾讓他改名字
    os.chdir('D:\\selenium\\ai100')

    # 更改pdf名字
    time.sleep(2)  # 停一下讓他下載完
    os.rename('document.pdf', day+'.pdf')
    os.chdir('..')  # cd回來主程式的資料夾

    driver.close()  # 關閉分頁
    driver.switch_to.window(driver.window_handles[0])  # 把控制權交回給第一頁
    # ---------------------------- #
    # 接下來是下載範例檔

    driver.execute_script("window.open('');")

    # Switch to the new window and open new url
    driver.switch_to.window(driver.window_handles[1])

    driver.get(sampleCode_url)  # 前往網址
    time.sleep(4)  # 讓他有足夠的時間load網頁

    archive_download_btn = driver.find_elements_by_xpath("//a[contains(text(), '打包下載')]")[0].click() # 找到下載的按鈕
    print("Sample code download: " + day) # debug用的

    # check_AD = check_exists_by_xpath("//a[contains(text(), '打包下載')]")
    #
    # if check_AD:
    #     print("AD is true")
    #     archive_download_btnl = driver.find_elements_by_xpath("//a[contains(text(), '打包下載')]")
    #     for i in range(0, 2):
    #         archive_download_btn = driver.find_elements_by_xpath("//a[contains(text(), '打包下載')]")[i].click()
    #         print("File"+str(i)+"download complete.")
    # else:
    #     print("AD is false")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])  # 把控制權交回給第一頁
    time.sleep(2)  # 給他一點時間休息，不然會生氣