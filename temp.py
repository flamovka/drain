from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('lang=en')
driver = webdriver.Chrome('d:/Work/pro1/chromedriver.exe', chrome_options=options)  # Optional argument, if not specified will search path.
# to change zoom but Submit does not work
driver.get('chrome://settings/')
driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.45);')
driver.get('https://payproglobal.com/knowledge-base/developer-tools/url-parameters/')
driver.implicitly_wait(4)

try:
    data=driver.find_element_by_xpath('//*[@id="large-header"]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[5]/div[1]').text
    print(data)
except Exception as exception:
    print(exception.__class__.__name__)
finally: driver.quit()
