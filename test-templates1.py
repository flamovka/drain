# BackupMediaTypeId BusinessPurchaseTypeId
# CombinationsTypeId CurrencyTypeId DownloadWarrantyTypeId
# LanguageTypeId LicenseToTypeId PromoTypeId
import time
import re
from cProfile import label
from logging import exception
from telnetlib import EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('d:/Work/pro1/chromedriver.exe')  # Optional argument, if not specified will search path.
# driver.execute_script('Runtime.getRuntime().exec("taskkill /F /IM chromedriver.exe /T")')
# driver.get('chrome://settings/')
# driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.6);')
driver.get('https://store.payproglobal.com/checkout?products[1][id]=48470&page-template=2339&'
           'use-test-mode=true&secret-key=ZugnJQby_5')

try:
    quantity = driver.find_element_by_name('products[1][qty]')
    #.__setattr__(3) does not work
    quantity.send_keys(Keys.ARROW_UP)
    quantity.send_keys(Keys.ARROW_UP)
    value = float(quantity.get_attribute('value'))
    print('value=', value)
    # currency = Select(driver.find_element_by_xpath("//select[@name='currency']"))
    # currency.select_by_value('USD')
    time.sleep(4)
    item_price = driver.find_element_by_class_name('item-price').text
    print('item-price=', item_price)
    item_price = re.findall('([-+]?[\d+,]?\d+.*\d+)', item_price)
    item_price = item_price[0].replace(',', '')
    print('item-price[0]=', item_price)

    time.sleep(4)
    price = driver.find_element_by_class_name('first-payment').text
    print('total=', price)
    price = re.findall('([-+]?[\d+,]?\d+.*\d+)', price)
    price = price[0].replace(',', '')
    print('total[0]=', price)
    if float(price) == float(item_price) * value:
        print('right price amount', price)
    else:
        print('wrong price amount', price)


    #import selenium.webdriver.common.Keys
    # from selenium.webdriver import ActionChains
    # actions = ActionChains(driver)
    # action_chains.drag_and_drop(element6, value=2).perform()
    # driver.execute_script("return arguments[0].scrollIntoView();", element)
    # get visible area of screen but only for one element
    driver.execute_script("$('.coupon-block').find('label').click()")
    driver.execute_script("$('.coupon-data').removeClass('hidden')")
    driver.find_element_by_name('coupon-code-to-add').send_keys('wer234')
    currency = Select(driver.find_element_by_xpath("//select[@name='currency']"))
    currency.select_by_value('CAD')
    language = Select(driver.find_element_by_xpath("//select[@name='language']"))
    language.select_by_value('en')
    time.sleep(3)
    driver.execute_script("$('.corporate-block').find('label').click()")
    driver.execute_script("$('.licensee-block').find('label').click()")
    time.sleep(5)
    country = Select(driver.find_element_by_xpath("//select[@name='billing-country']"))
    country.select_by_value('FR')
    time.sleep(8)
    driver.find_element_by_name('billing-company-name').send_keys('Avogadros')
    driver.find_element_by_name('license-name').send_keys('fandango')
    driver.find_element_by_name('license-email').send_keys('fan@i.ua')
    #CUSTOM FIELDS
    driver.find_element_by_class_name('custom-fields').text
    # driver.find_element_by_name('license-email').submit()
    # driver.execute_script("$('.coupon-data').removeClass('hidden')")
    # time.sleep(4) # Let the user actually see something!
    # driver.find_element_by_name('billing-tax-number').send_keys('1234567')
    # driver.find_element_by_xpath('.//coupon-block/label)').click()
    # time.sleep(6)
    driver.find_element_by_name("submit-button").click()
    time.sleep(8)

except Exception as exception:
    # Output unexpected Exceptions.
    # print(exception, False)
    print(exception.__class__.__name__)

    # there should be code for store errors in some place(?)
    # from PyQt5 import QtWidgets
    # QtWidgets.QMessageBox.critical(None,
    #                                "An exception was raised",
    #                                "Exception type: {}".format(t))


finally: driver.close()
# return ('False')


