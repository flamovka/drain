from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()


# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome('d:/Work/pro1/chromedriver.exe')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/xhtml');
# time.sleep(2) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('Cflame loves cats')
# search_box.submit()
# time.sleep(8) # Let the user actually see something!
# driver.quit()