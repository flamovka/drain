import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('d:/Work/pro1/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://store.payproglobal.com/checkout?products[1][id]=48467&page-template=2339&use-test-mode=true&secret-key=ZugnJQby_5');
# driver.send_keys(Keys.CONTROL, "-")
# driver.find_element_by_xpath(".//select[@id='zoomLevel']/option[@value='0.66']")
# driver.execute_script("$('#zoom_out').click(function() { zoom_page(-40,$(this)) });")
# driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL,Keys.SUBTRACT)
# driver.send_keys(Keys.CONTROL, "-")
element1 = driver.find_element_by_name("billing-first-name")
element1.clear()
element1.send_keys('Northen')
element2 = driver.find_element_by_name("billing-last-name")
element2.clear()
element2.send_keys('Star')
element3 = driver.find_element_by_name("billing-email")
element3.clear()
element3.send_keys('olga.tugay@payproglobal.com')
element4 = driver.find_element_by_name("billing-city")
element4.clear()
element4.send_keys('Ferelden')
element5 = driver.find_element_by_name("billing-address")
element5.clear()
element5.send_keys('rue de la Paix')
element6 = driver.find_element_by_name('products[1][qty]')
element6.send_keys(Keys.ARROW_UP)

# element7 = int(driver.find_element_by_class_name('col-sm-2 hidden-xs text-center'))
# element8 = int(driver.find_element_by_class_name('order-total text-right'))
# element8 = element7 * element6
#import selenium.webdriver.common.Keys
# from selenium.webdriver import ActionChains
# action_chains = ActionChains(driver)
# action_chains.drag_and_drop(element6, value=2).perform()

currency = Select(driver.find_element_by_xpath("//select[@name='currency']"))
currency.select_by_value('CAD')
language = Select(driver.find_element_by_xpath("//select[@name='language']"))
language.select_by_value('en')
country = Select(driver.find_element_by_xpath("//select[@name='billing-country']"))
country.select_by_value('FR')
# driver.find_element_by_name("submit-button").click()
time.sleep(14) # Let the user actually see something!
driver.close()