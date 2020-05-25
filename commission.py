import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('d:/Work/pro1/chromedriver.exe')  # Optional argument, if not specified will search path.
# to change zoom but Submit does not work
# driver.get('chrome://settings/')
# driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.45);')
driver.get('https://store.payproglobal.com/checkout?products[1][id]=49600&page-template=2339')

try:
    #BILLING BLOCK
    driver.find_element_by_name("billing-first-name").send_keys('Northen')
    driver.find_element_by_name("billing-last-name").send_keys('Star')
    driver.find_element_by_name("billing-email").send_keys('olga.tugay@payproglobal.com')
    driver.find_element_by_name("billing-city").send_keys('Ferelden')
    driver.find_element_by_name("billing-address").send_keys('rue de la Paix')
    #CURRENCY & LANGUAGE
    currency = Select(driver.find_element_by_xpath("//select[@name='currency']"))
    currency.select_by_value('USD')
    language = Select(driver.find_element_by_xpath("//select[@name='language']"))
    language.select_by_value('en')
    country = Select(driver.find_element_by_xpath("//select[@name='billing-country']"))
    country.select_by_value('NO')
    #CARD
    driver.find_element_by_name('cc-number').send_keys('5300722329740240')
    driver.find_element_by_name('cc-expire-month').send_keys('09')
    driver.find_element_by_name('cc-expire-year').send_keys('21')
    driver.find_element_by_name('cc-cvv').send_keys('836')
    time.sleep(2)
    driver.find_element_by_name("submit-button").click()
    time.sleep(4)
    #TY PAGE
    driver.execute_script("$('.order-id').removeClass('hidden')")
    time.sleep(2)
    order_id = driver.find_element_by_class_name('order-id').text
    driver.get('https://ccadmin1.payproglobal.com/Orders/Details/' + str(order_id))
    time.sleep(4)
    #ENTERING ADMIN PANEL
    login = driver.find_element_by_name('username')
    login.send_keys('olga.tugay')
    password = driver.find_element_by_name('password')
    password.send_keys('4all&all')
    driver.find_element_by_class_name('pull-right').click()
    time.sleep(2)
    #COMMISSION CALCULATING

    # REFUND INITIATION
    driver.find_element_by_id('full-refund-order-button').click()
    time.sleep(2)
    driver.execute_script("$('#full-refund-order-modal [name=RemarkText]').val('regression: purchase and refund')")
    time.sleep(2)
    driver.execute_script("$('#full-refund-order-modal [type=submit]').click()")
    time.sleep(4)
    # ADD PART WITH CALCULATION ORDERTOTAL=TOTAL REFUNDED (AP) AND NET REVENUE=PAYPRO FEE (CP)

except Exception as exception:
    print(exception.__class__.__name__)
finally: driver.close()