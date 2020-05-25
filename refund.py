import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('d:/Work/pro1/chromedriver.exe')  # Optional argument, if not specified will search path.
# to change zoom but Submit does not work
# driver.get('chrome://settings/')
# driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.45);')
driver.get('https://store.payproglobal.com/checkout?products[1][id]=51385&page-template=2339')

try:
    # BILLING BLOCK
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
    # PRODUCT BLOCK
    element6 = driver.find_element_by_name('products[1][qty]')
    element6.send_keys(Keys.ARROW_UP)
    time.sleep(4)
    driver.execute_script("$('.coupon-block').find('label').click()")
    driver.execute_script("$('.coupon-data').removeClass('hidden')")
    driver.find_element_by_name('coupon-code-to-add').send_keys('wer234')
    # CURRENCY & LANGUAGE
    currency = Select(driver.find_element_by_xpath("//select[@name='currency']"))
    currency.select_by_value('USD')
    language = Select(driver.find_element_by_xpath("//select[@name='language']"))
    language.select_by_value('en')
    time.sleep(3)
    # CORPORATE AND LICENCE
    driver.execute_script("$('.corporate-block').find('label').click()")
    driver.execute_script("$('.licensee-block').find('label').click()")
    time.sleep(5)
    country = Select(driver.find_element_by_xpath("//select[@name='billing-country']"))
    country.select_by_value('NO')
    time.sleep(8)
    driver.find_element_by_name('billing-company-name').send_keys('Avogadros')
    driver.find_element_by_name('license-name').send_keys('fandango')
    driver.find_element_by_name('license-email').send_keys('fan@i.ua')
    time.sleep(2)
    # CARD
    driver.find_element_by_name('cc-number').send_keys('5300722329740240')
    driver.find_element_by_name('cc-expire-month').send_keys('09')
    driver.find_element_by_name('cc-expire-year').send_keys('21')
    driver.find_element_by_name('cc-cvv').send_keys('836')
    time.sleep(2)
    driver.find_element_by_name("submit-button").click()
    time.sleep(4)
    # TY PAGE
    driver.execute_script("$('.order-id').removeClass('hidden')")
    time.sleep(2)
    order_id = driver.find_element_by_class_name('order-id').text
    driver.get('https://ccadmin1.payproglobal.com/Orders/Details/' + str(order_id))
    time.sleep(4)
    # ENTERING ADMIN PANEL
    login = driver.find_element_by_name('username')
    login.send_keys('olga.tugay')
    password = driver.find_element_by_name('password')
    password.send_keys('4all&all')
    driver.find_element_by_class_name('pull-right').click()
    time.sleep(2)
    # REFUND INITIATION
    driver.find_element_by_id('full-refund-order-button').click()
    time.sleep(2)
    driver.execute_script("$('#full-refund-order-modal [name=RemarkText]').val('regression: purchase and refund')")
    time.sleep(2)
    driver.execute_script("$('#full-refund-order-modal [type=submit]').click()")
    time.sleep(4)
    # ADD PART WITH CALCULATION ORDERTOTAL=TOTAL REFUNDED (AP) AND NET REVENUE=PAYPRO FEE (CP)
    zed=driver.find_element_by_class_name('col-md-6').text()
    print('The first one of table', zed)

    # CP ENTERING

    # driver.get('https://cc.payproglobal.com/Orders/Details/' + str(order_id))
    # login = driver.find_element_by_name('Username')
    # login.send_keys('Olga.Tugay')
    # password = driver.find_element_by_name('Password')
    # password.send_keys('7justice')
    # password.send_keys(Keys.ENTER)
    # time.sleep(3)

except Exception as exception:
    print(exception.__class__.__name__)
finally: driver.close()
