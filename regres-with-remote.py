import re

# CP ENTERING FOR PARAMETERS ??
coupon_amount = 0.75  # CP asD5D57 coupon 75%
# 53134 aff_comm=0.42, part_comm1=0.44
# 51385 aff_comm=0.14, part_comm2=0.44
# 48467 aff_comm=0.17, part_comm1=0.37, part_comm2=0.11
aff_comm = 0.17 # affiliate 5333 42% initial first campaign
part_comm1 = 0.37   # Technical affiliate test 44% Yulia Skirdina 0% and Olenka test 0%
part_comm2 = 0.11
part_comm3 = 0.00

# ENTERING ADMIN PANEL FOR PARAMETERS ??
vendorID = 155964
#driver.get('https://ccadmin1.payproglobal.com/VendorAccounts/GeneralInfo/' + str(vendorID))
comm_amount = 0.053  # for vendor 155964 fee = 5.3%
#comm_amount = driver.find_element_by_xpath('//*[@id="select2-Account_CommissionConfigurationId-container"]')
#driver.get('https://ccadmin1.payproglobal.com/Taxes')
tax_amount = 0.05  # tax for TW 5%
item_price =3.23
qty =1
order_id =18337448
# PART WITH CALCULATION ORDER COMMISSION
    # FROM ORDER
order_total =0.85
order_subtotal =0.81
total_tax =0.04
full_date ='11/28'
#absorbed_tax = driver.find_element_by_name('total-absorbed-tax')
before_discount =3.23
total_discounted =2.42
total_commission =0.05
vendor_partners =0.76
vendor_part =0.24
affiliate_part =0.13
partner_part =0.39
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
    # list_AP[i] = re.search('[+-]?[\d,]+(?:\.\d+)?', list_AP[i]).group(0).replace(',', '')
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

# ADD PART WITH CALCULATION ORDERTOTAL=TOTAL REFUNDED (AP) AND NET REVENUE=PAYPRO FEE (CP)
rebalance = - commission
# rebal = 0.00    # for test orders
reaff = repart = 0.00
listRefunded = [total, sub, tax, rebalance, rebalance, reaff, repart]
# listRefunded[3] = rebal     # for test orders
ref =0.85
re_sub =0.81
re_tax =0.04
ref_vpartners =-0.05
ref_vendor =-0.05
ref_affiliate =0.00
ref_partner =0.00
list_ref = [ref, re_sub, re_tax, ref_vpartners, ref_vendor, ref_affiliate, ref_partner]
print('list_ref is printed next go to TYpe ERror', list_ref)
for i in range(len(list_ref)):
    # list_ref[i] = re.search('[+-]?[\d,]+(?:\.\d+)?', list_ref[i]).group(0).replace(',', '')
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
with open('d:/Work/PayProGlobal/Autotests/'+str(order_id)+'-'+str(date)+'.txt', 'w') as i:
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
