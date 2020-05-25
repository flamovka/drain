from selenium import webdriver
import time
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('d:/Work/pro1/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://store.payproglobal.com/checkout?products[1][id]=48470&page-template=11493&'
           'use-test-mode=true&secret-key=ZugnJQby_5')
try:
    w1=driver.find_element_by_class_name('custom-fields').text
    print(w1)
    # driver.find_element_by_class_name('custom-fields').click()
    # does not work - NoSuchElementException cause
    # check = Select(driver.find_element_by_xpath("//select[@name='custom-fields[10672][]']"))
    # check.select_by_value('Arthur')
    # print(check)
    # SUBMIT the form
    # driver.find_element_by_name("submit-button").click()
    time.sleep(3)

except Exception as exception:
    # ERRORS handler
    print(exception.__class__.__name__)
    # there should be code for store errors in some place(?)

    # EXIT automode
finally:
    driver.close()