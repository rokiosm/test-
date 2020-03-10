from selenium import webdriver
import os
import time

global(browser)

browser = webdriver.Chrome(
    os.getcwd() + "/chromedriver"
)

browser.get("instagram.com")
time.sleep(5)
browser.close()


