# -*- coding: utf-8 -*-
'''
浏览器控制
'''

from selenium import webdriver
from time import sleep
import config.selenium as config

print(config.base['chrome_driver_path'])
driver = webdriver.Chrome(config.base['chrome_driver_path'])
driver.maximize_window()
driver.get('http://www.baidu.com')
print('base_url: ', driver.current_url)

driver.find_element_by_id('kw').send_keys(u'selenium 灰蓝')
driver.find_element_by_id('su').click()
sleep(2)
print('after search: ', driver.current_url)

driver.back()
print('back to: ', driver.current_url)

driver.forward()
print('forward to: ', driver.current_url)

sleep(2)
driver.refresh()
print('refresh: ', driver.current_url)

sleep(2)
driver.quit()