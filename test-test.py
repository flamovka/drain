import time
from selenium import webdriver

driver = webdriver.Chrome('d:/Work/pro1/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://store.payproglobal.com/checkout?products[1][id]=48467&page-template=2339&use-test-mode=true&secret-key=ZugnJQby_5');
element1 = driver.find_element_by_name("billing-first-name")
#element1.clear()
element1.send_keys('Northen')
element2 = driver.find_element_by_name("billing-last-name")
element2.send_keys('Star')
# element1.submit() # crashing all checkout submiting
# if element1 return ('error-message'):
#     element1.clear()
#     else
driver.find_element_by_name("submit-button").click()
# driver.current_window_handle()
time.sleep(5) # Let the user actually see something!
driver.quit()