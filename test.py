from selenium import webdriver
from selenium.webdriver.common.keys import Keys

''' 
ebdriver Chrome下载地址：http://chromedriver.storage.googleapis.com/index.html?path=2.25
'''
driver = webdriver.Chrome('/Users/liuyuancheng/PycharmProjects/python-selenium-demo/chromedriver')
driver.get("http://www.baidu.com")
assert u"百度" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()