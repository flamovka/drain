import time
from selenium import webdriver
import re
options = webdriver.ChromeOptions()
options.add_argument('lang=en')
driver = webdriver.Chrome('d:/testing tests/chromedriver.exe', chrome_options=options)
driver.get('https://tinder.com/app/recs')

try:
    connection = 0
    girlie_nick=[]
    if 'I like girl' == True and time.sleep(42) == True:
        connection=('Epic win!')
        girlie_nick.append()
    elif 'I like girl' == True and time.sleep(42) == False:
        connection=('Spend much time')
        girlie_nick.append()
    elif 'I like girl' == False and time.sleep(42) == True:
        connection=('Stop sleep girlie you\'ve even do not like!')
        girlie_nick.pop()
    elif 'I like girl' == False and time.sleep(42) == False:
        connection = ('Epic fail!')
        girlie_nick.remove()
    else: connection=('Weird enough')
    for i in range (len(girlie_nick)):
        girlie_nick[i]=re.search('[\w]+(\W+)?', girlie_nick[i].group(0).replace('\s', '')
        if girlie_nick[i] == 'flamovka':
            response = ('Wise choice')
            break
        else: connection = ('Wrong girl')
            continue
    else:
    print(connection)
    with open('D:/Home/my_princess.txt', 'w') as i:
        i.write('\n')
        i.write('\n')
        i.write(str(connection))
        i.write('\n')
        i.write(str(responce))
except Exception as exception:
    print(exception.__class__.__name__)
finally:
    driver.close()