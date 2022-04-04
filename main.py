from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service("A:\Webservices ML\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("https://python.org")
price = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul').text
# print(type(price))
price = price.split('\n')
# print(type(price))
event_dict = dict()
i = 0
print(len(price))
event_dict['date'] = [price[i] for i in range(len(price)) if i % 2 == 0]
event_dict['name'] = [price[i] for i in range(len(price)) if i % 2 != 0]
print(event_dict)
driver.quit()
driver.find_element(By.NAME, 'btnK').click



