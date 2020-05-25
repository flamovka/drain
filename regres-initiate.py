import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re

options = webdriver.ChromeOptions()
options.add_argument('lang=en')
driver = webdriver.Chrome('d:/Work/pro1/chromedriver.exe', chrome_options=options)  # Optional argument, if not specified will search path.
# to change zoom but Submit does not work
# driver.get('chrome://settings/')
# driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.45);')
# productID1 = 53134
#productID1 = 51385
productID1 = 48467
# test ='&use-test-mode=true&secret-key=ZugnJQby_5'  #for test order
test = '&use-test-mode=false'
driver.get('https://store.payproglobal.com/checkout?page-template=2339&products[1][agreement-id]=5334&products[1][id]=' + str(productID1) + test) #'+'&products[2][id]=' + str(productID2)
time.sleep(4)

try:
    # BILLING BLOCK
    driver.find_element_by_name("billing-first-name").send_keys('November')
    driver.find_element_by_name("billing-last-name").send_keys('Regression')
    driver.find_element_by_name("billing-email").send_keys('olga.tugay@payproglobal.com')
    driver.find_element_by_name("billing-city").send_keys('Oz')
    driver.find_element_by_name("billing-address").send_keys('rue de la Paix')
    # PRODUCT BLOCK
    quantity = driver.find_element_by_name('products[1][qty]')
    # quantity.send_keys(Keys.ARROW_UP)
    qty = float(quantity.get_attribute('value'))
    # print('qty=', qty)
    # NEED to change item_price for new_price: last in jQuery fro two items

    # CURRENCY & LANGUAGE & COUNTRY
    currency = Select(driver.find_element_by_xpath("//select[@name='currency']"))
    currency.select_by_value('UAH')
    language = Select(driver.find_element_by_xpath("//select[@name='language']"))
    language.select_by_value('en')
    country = Select(driver.find_element_by_xpath("//select[@name='billing-country']"))
    country.select_by_value('TW')  # tax = 5%
    # COUPON add discount
    driver.execute_script("$('.coupon-block').find('label').click()")
    time.sleep(2)
    driver.execute_script("$('.coupon-data').removeClass('hidden')")
    time.sleep(2)
    driver.find_element_by_name('coupon-code-to-add').send_keys('asD5D57')
    country = Select(driver.find_element_by_xpath("//select[@name='billing-country']"))
    country.select_by_value('TW')  # tax = 5%
    time.sleep(4)
    item_price = driver.find_element_by_class_name('item-price').text
    #print('item-price naked=', item_price)
    item_price = float(re.search('[+-]?[\d,]+(?:\.\d+)?', item_price).group(0).replace(',', ''))
    print('item-price', item_price)
    # price = driver.find_element_by_class_name('first-payment').text
    # print('total=', price)
    # if float(price) == float(item_price) * qty:
    #     print('right price amount on checkout=', price)
    # else:
    #     print('wrong price amount on checkout=', price)
    time.sleep(4)
    # CORPORATE AND LICENCE
    # driver.execute_script("$('.corporate-block').find('label').click()")
    # time.sleep(2)
    # driver.find_element_by_name('billing-company-name').send_keys('Avogadros')
    # driver.execute_script("$('.licensee-block').find('label').click()")
    # driver.find_element_by_name('license-name').send_keys('fandango')
    # driver.find_element_by_name('license-email').send_keys('fan@i.ua')

    # CARD
    driver.find_element_by_name('cc-number').send_keys('5300722329740240')
    driver.find_element_by_name('cc-expire-month').send_keys('09')
    driver.find_element_by_name('cc-expire-year').send_keys('21')
    driver.find_element_by_name('cc-cvv').send_keys('836')
    driver.find_element_by_name("submit-button").click()
    time.sleep(4)
    print('after-submit')
    # # PAYPAL
    # payment = Select(driver.find_element_by_xpath("//select[@name='payment-method']"))
    # payment.select_by_value('14')
    # time.sleep(6)
    # # driver.find_element_by_name('payment-method').send_keys('14')
    # driver.find_element_by_id('paypal').send_keys('helgatugay@gmail.com')
    # driver.find_element_by_name("submit-button").click()
    # time.sleep(4)
    # print('after-submit')
    # # PayPal autorization
    # driver.find_element_by_id('password').send_keys('7justice4all')
    # time.sleep(3)
    # driver.find_element_by_id("btnLogin").click()
    # time.sleep(12)
    # # PayPal wants to attach new card and all process stops here
    # driver.find_element_by_id('confirmButtonTop').click()
    # time.sleep(8)

    # TY PAGE
    # order_id = driver.find_element_by_xpath('//*[@id="checkout-form-container"]/div/div/div[1]/div[2]/div/div/p[2]').text
    # a = re.findall('[-+]?[\d+,]?\d+.*\d+', order_id)
    # order_id = a[0]
    # order_id = re.search('[\d]+', order_id.group(0))
    driver.execute_script("$('.order-id').removeClass('hidden')")
    order_id = driver.find_element_by_class_name('order-id').text
    print(order_id)
finally: driver.close()