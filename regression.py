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
driver.get('https://store.site.com/checkout?page-template=2339&products[1][agreement-id]=5334&products[1][id]=' + str(productID1) + test) #'+'&products[2][id]=' + str(productID2)
time.sleep(4)

try:
    # BILLING BLOCK
    driver.find_element_by_name("billing-first-name").send_keys('October')
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
    driver.find_element_by_name('cc-number').send_keys('***********')
    driver.find_element_by_name('cc-expire-month').send_keys('09')
    driver.find_element_by_name('cc-expire-year').send_keys('21')
    driver.find_element_by_name('cc-cvv').send_keys('836')
    driver.find_element_by_name("submit-button").click()
    time.sleep(4)
    # print('after-submit')
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

    # CP ENTERING FOR PARAMETERS ??
    coupon_amount = 0.75  # CP asD5D57 coupon 75%
    # 53134 aff_comm=0.42, part_comm1=0.44
    # 51385 aff_comm=0.14, part_comm2=0.44
    # 48467 aff_comm=0.17, part_comm1=0.37, part_comm2=0.11
    aff_comm = 0.17 # affiliate 5333 42% initial first campaign
    part_comm1 = 0.37   # Technical affiliate test 44% Yulia  0% and Olenka test 0%
    part_comm2 = 0.11
    part_comm3 = 0.00

    # ENTERING ADMIN PANEL FOR PARAMETERS ??
    vendorID = 155964
    #driver.get('https://admin.site.com/VendorAccounts/GeneralInfo/' + str(vendorID))
    comm_amount = 0.053  # for vendor 155964 fee = 5.3%
    #comm_amount = driver.find_element_by_xpath('//*[@id="select2-Account_CommissionConfigurationId-container"]')
    #driver.get('https://admin.site.com/Taxes')
    tax_amount = 0.05  # tax for TW 5%

    # ENTERING ADMIN PANEL FOR ORDER
    driver.get('https://admin.site.com/Orders/Details/' + str(order_id))
    time.sleep(2)
    login = driver.find_element_by_name('username')
    login.send_keys('olga.tugay')
    password = driver.find_element_by_name('password')
    password.send_keys('password')
    driver.find_element_by_class_name('pull-right').click()
    # PART WITH CALCULATION ORDER COMMISSION
        # FROM ORDER
    #order_total = driver.find_element_by_xpath('//*[@id="tab-order-general-info"]/div/div[1]/div[1]/div[2]/strong').text
    order_total = driver.find_element_by_xpath('//td[text()="Total"]')
    # print('order_total', order_total)
    order_subtotal = driver.find_element_by_xpath('//*[@id="tab-order-general-info"]/div/div[2]/div[1]/div[2]').text
    # print('order_subtotal', order_subtotal)
    total_tax = driver.find_element_by_xpath('//*[@id="tab-order-general-info"]/div/div[8]/div[1]/div[2]').text
    # print('total_tax', total_tax)
    full_date = driver.find_element_by_css_selector(
        '#tab-order-general-info > div > div:nth-child(10) > div:nth-child(1) > div:nth-child(2)').text
    #absorbed_tax = driver.find_element_by_name('total-absorbed-tax')
    before_discount = driver.find_element_by_xpath('//*[@id="tab-order-general-info"]/div/div[3]/div[1]/div[2]').text
    # print('before_discount', before_discount)
    total_discounted = driver.find_element_by_xpath('//*[@id="tab-order-general-info"]/div/div[3]/div[2]/div[2]').text
    # print('total_discounted', total_discounted)
    total_commission = driver.find_element_by_xpath('//*[@id="tab-order-general-info"]/div/div[8]/div[2]/div[2]').text
    #money_received = driver.find_element_by_name('money-received')
    # print('total_commission', total_commission)
    vendor_partners = driver.find_element_by_xpath('//*[@id="tab-order-general-info"]/div/div[15]/div[2]/div[2]').text
    # print('vendor_partners', vendor_partners)
    driver.execute_script("$('[href=\"#tab-order-items-info\"]').tab('show')")
    vendor_part = driver.find_element_by_xpath('//*[@id="tab-order-items-info"]/div[2]/div/table/tbody/tr/td[17]').text
    # print('vendor_part', vendor_part)
    affiliate_part = driver.find_element_by_xpath('//*[@id="tab-order-items-info"]/div[2]/div/table/tbody/tr/td[18]').text
    # print('affiliate_part', affiliate_part)
    partner_part = driver.find_element_by_xpath('//*[@id="tab-order-items-info"]/div[2]/div/table/tbody/tr/td[19]').text
    # print('partner_part', partner_part)
    list_AP = [order_total, order_subtotal, total_tax, before_discount, total_discounted,
               total_commission, vendor_partners, vendor_part, affiliate_part, partner_part]
    # print(list_AP)
    date = re.search('[\d][\d]/[\d][\d]', full_date).group(0).replace('/', '-')
    print('date', date)

    # CALCULATION FROM PARAMETERS
    price = round(item_price * qty, 2)
    print('price', price)
    discounted = round((coupon_amount * price), 2)
    sub = round((price - discounted), 2)
    tax = round((sub * tax_amount), 2)
    total = round(sub + tax, 2)
    commission = round((total * comm_amount), 2)
    balance = round(sub - commission, 2)
    # balance = 0.00  # for test orders
    affiliate = round(sub * aff_comm, 2)
    partner = round(sub * part_comm1 + sub * part_comm2 + sub * part_comm3, 2)
    vendor = round(balance - affiliate - partner, 2)
    # vendor = round(sub - commission - affiliate - partner, 2)  # for test orders
    listCal = [total, sub, tax, price, discounted,
               commission, balance, vendor, affiliate, partner]
    dictCal = {'total [0]': listCal[0], 'sub [1]': listCal[1], 'tax [2]': listCal[2], 'price [3]': listCal[3],
               'discounted [4]': listCal[4], 'commission [5]': listCal[5],
               'vendor and partners balance [6]': listCal[6],
               'vendor part [7]': listCal[7], 'affiliate part [8]': listCal[8], 'partner part [9]': listCal[9]}
    print('dictCal', dictCal)
    for i in range(len(list_AP)):
        list_AP[i] = float(re.search('[+-]?[\d,]+(?:\.\d+)?', list_AP[i]).group(0).replace(',', ''))
        if abs(list_AP[i] - listCal[i]) <= 0.011:
            rez = ('TRUE! The calculated parameters amount is the same as displayed in orders', [i])
        else:
            rez = ('FALSE! Something is wrong with calculation, check it out', [i])
            break
            # print('list_ap without currency', list_AP)
    dict_AP = {'order_total [0]': list_AP[0], 'order_subtotal [1]': list_AP[1], 'total_tax [2]': list_AP[2],
               'before_discount [3]': list_AP[3], 'total_discounted [4]': list_AP[4], 'total_commission [5]': list_AP[5],
               'vendor_partners [6]': list_AP[6], 'vendor_part [7]': list_AP[7], 'affiliate_part [8]': list_AP[8],
               'partner_part [9]': list_AP[9]}
    print(rez)
    print('dict_AP', dict_AP)
    time.sleep(4)
    # REFUND INITIATION
    driver.find_element_by_id('full-refund-order-button').click()
    time.sleep(4)
    print('ref_button')
    #driver.find_element_by_name('UseRealPaymentGatewayTransaction').click()
    #time.sleep(2)
    # no suspend for subscription
    driver.find_element_by_xpath('//*[@id="full-refund-order-modal"]/div/div/div[3]/form/div/div[1]/div[3]').click()
    time.sleep(4)
    print('no-suspend')
    driver.execute_script("$('#full-refund-order-modal [name=RemarkText]').val('regression: purchase and refund')")
    time.sleep(2)
    driver.execute_script("$('#full-refund-order-modal [type=submit]').click()")
    time.sleep(4)

    # ADD PART WITH CALCULATION ORDERTOTAL=TOTAL REFUNDED (AP) AND NET REVENUE=PAYPRO FEE (CP)
    rebalance = - commission
    # rebal = 0.00    # for test orders
    reaff = repart = 0.00
    listRefunded = [total, sub, tax, rebalance, rebalance, reaff, repart]
    # listRefunded[3] = rebal     # for test orders
    ref_total = driver.find_element_by_xpath('//*[@id="tab-order-general-info"]/div/div[2]/div[2]/div[2]/span[1]').text
    re_sub = driver.find_element_by_xpath('//*[@id="tab-order-general-info"]/div/div[2]/div[2]/div[2]/span[2]').text
    re_tax = driver.find_element_by_xpath('//*[@id="tab-order-general-info"]/div/div[2]/div[2]/div[2]/span[3]').text
    ref_vpartners = driver.find_element_by_xpath('//*[@id="tab-order-general-info"]/div/div[15]/div[2]/div[2]').text
    driver.execute_script("$('[href=\"#tab-order-items-info\"]').tab('show')")
    ref_vendor = driver.find_element_by_xpath('//*[@id="tab-order-items-info"]/div[2]/div/table/tbody/tr/td[17]').text
    ref_affiliate = driver.find_element_by_xpath('//*[@id="tab-order-items-info"]/div[2]/div/table/tbody/tr/td[18]').text
    ref_partner = driver.find_element_by_xpath('//*[@id="tab-order-items-info"]/div[2]/div/table/tbody/tr/td[19]').text
    list_ref = [ref_total, re_sub, re_tax, ref_vpartners, ref_vendor, ref_affiliate, ref_partner]
    print('list_ref is printed next go to TYpe ERror', list_ref)
    for i in range(len(list_ref)):
        list_ref[i] = float(re.search('[+-]?[\d,]+(?:\.\d+)?', list_ref[i]).group(0).replace(',', ''))
        if abs(list_ref[i] - listRefunded[i]) <= 0.011:
            res = ('TRUE! The calculated refund amount is the same as displayed in orders', [i])
        else:
            res = ('FALSE! Something is wrong with refund calculation, check it out', [i])
            break

    dict_ref = {'total_refunded [0]': list_ref[0], 'refunded_subtotal [1]': list_ref[1], 'refunded_tax [2]': list_ref[2],
                'refunded_vendor&partners [3]': list_ref[3], 'refunded_vendor_part [4]': list_ref[4],
                'refunded_affiliate_part [5]': list_ref[5], 'refunded_partner_part [6]': list_ref[6]}
    dictRefunded = {'total [0]': listRefunded[0], 'subtotal [1]': listRefunded[1], 'tax [2]': listRefunded[2],
                    'commission negative [3]': listRefunded[3], 'vendor balance [4]': listRefunded[4],
                    'zero from affiliate [5]': listRefunded[5], 'zero from partner [6]': listRefunded[6]}
    print('dict_ref', dict_ref)
    print('dictRefunded', dictRefunded)
    print(res)
    with open('d:/Work/Autotests/09_19/'+str(order_id)+'-'+str(date)+'.txt', 'w') as i:
        i.write(str(order_id))
        i.write('\n')
        for key, val in dict_AP.items():
            i.write('{}:{},\n'.format(key, val))
        i.write('\n')
        for key, val in dictCal.items():
            i.write('{}:{},\n'.format(key, val))
        i.write('\n')
        i.write(str(rez))
        i.write('\n')
        i.write('\n')
        for key, val in dict_ref.items():
            i.write('{}:{},\n'.format(key, val))
        i.write('\n')
        for key, val in dictRefunded.items():
            i.write('{}:{},\n'.format(key, val))
        i.write('\n')
        i.write(str(res))
        i.write('\n')
        i.write(str(full_date))
    print('Regression test ended')
except Exception as exception:
    print(exception.__class__.__name__)
finally: driver.close()