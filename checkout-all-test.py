import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('d:/Work/pro1/chromedriver.exe')  # Optional argument, if not specified will search path.
# driver.get('chrome://settings/')
# Change zoom of page provokes not submitting page for undefined reason
# driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.6);')
# It should get visible area of screen
# driver.execute_script("return arguments[0].scrollIntoView();", element)
driver.get('https://store.payproglobal.com/checkout?products[1][id]=48470&page-template=2339&'
           'use-test-mode=true&secret-key=ZugnJQby_5')

try:
    # TEST MODE no need to fill certain fields
    # QUANTITY of items
    quantity = driver.find_element_by_name('products[1][qty]')
    quantity.send_keys(Keys.ARROW_UP)
    # quantity.send_keys(Keys.ARROW_UP)
    value = float(quantity.get_attribute('value'))
    print('value=', value)
    # CURRENCY
    # currency = Select(driver.find_element_by_xpath("//select[@name='currency']"))
    # currency.select_by_value('USD')
    time.sleep(4)
    # PRICE check if correct multiplying
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
    # COUPON add discount
    driver.execute_script("$('.coupon-block').find('label').click()")
    driver.execute_script("$('.coupon-data').removeClass('hidden')")
    driver.find_element_by_name('coupon-code-to-add').send_keys('wer234')
    # CURRENCY
    currency = Select(driver.find_element_by_xpath("//select[@name='currency']"))
    currency.select_by_value('CAD')
    # LANGUAGE
    language = Select(driver.find_element_by_xpath("//select[@name='language']"))
    language.select_by_value('en')
    time.sleep(3)
    # BUSINESS PURCHASE and LICENSE TO blocks interrupted with COUNTRY for refresh
    driver.execute_script("$('.corporate-block').find('label').click()")
    driver.execute_script("$('.licensee-block').find('label').click()")
    time.sleep(5)
    country = Select(driver.find_element_by_xpath("//select[@name='billing-country']"))
    country.select_by_value('FR')
    time.sleep(8)
    driver.find_element_by_name('billing-company-name').send_keys('Avogadros')
    # driver.find_element_by_name('billing-tax-number').send_keys('1234567')
    driver.find_element_by_name('license-name').send_keys('fandango')
    driver.find_element_by_name('license-email').send_keys('fan@i.ua')
    # CUSTOM FIELDS
    driver.find_element_by_class_name('custom-fields').text
    # SUBMIT the form
    driver.find_element_by_name("submit-button").click()
    time.sleep(3)

except Exception as exception:
    # ERRORS handler
    print(exception.__class__.__name__)
    # there should be code for store errors in some place(?)

    # EXIT automode
finally: driver.close()



