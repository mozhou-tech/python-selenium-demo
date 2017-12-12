from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import config.selenium as config


driver = webdriver.Chrome(config.base.chrome_driver_path) # 改用本地的Path
driver.get("http://www.baidu.com")
assert u"百度" in driver.title
print(driver.title)
elem = driver.find_element_by_class_name("s_ipt")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)

# assert "No results found." not in driver.page_source
driver.quit()