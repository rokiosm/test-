from selenium import webdriver

driver = webdriver.Chrome('/Users/nusys/Downloads/chromedriver_mac64/chromedriver')
driver.implicitly_wait(3)

driver.get('https://google.com')
