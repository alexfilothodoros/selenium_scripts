import requests
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options,
                          executable_path=r'/Users/alex/Downloads/chromedriver')
driver.get('some_url')
links = driver.find_elements_by_css_selector("a")
# responsecode = requests.get(links[1].get_attribute('href')).status_code
# print((links[1].get_attribute('href'))+" --- "+str(responsecode))
for i in range(1, len(links)):
    responsecode = requests.get(links[i].get_attribute('href')).status_code
    print((links[i].get_attribute('href'))+" --- "+str(responsecode))
    if(responsecode == 200):
        print("Valid Link")
    else: print("broken/invalid link")
driver.quit()
