import re
ice = '2,000.30 UAh'
ice = re.findall('([-+]?[\d+,]?\d+.*\d+)', ice)
ice = ice[0].replace(',', '')
print('total[0]=', ice)
item_price = '1,000.150 ver'
item_price = re.findall('([-+]?[\d+,]?\d+.*\d+)', item_price)
item_price = item_price[0].replace(',', '')
value = 2.00
if float(ice) == float(item_price) * value:
    print('right price amount', ice)
else:
    print('wrong price amount', ice)