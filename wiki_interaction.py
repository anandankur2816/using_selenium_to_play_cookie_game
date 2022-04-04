from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service("A:\Webservices ML\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)
# # driver.minimize_window()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# interaction_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
# print(interaction_count)

# Interacting with website and filling form
driver.get("http://secure-retreat-92358.herokuapp.com/")
driver.find_element(By.NAME, 'fName').send_keys('admin')
driver.find_element(By.NAME, 'lName').send_keys('singh')
driver.find_element(By.NAME, 'email').send_keys('alpha@alpha.com')
driver.find_element(By.XPATH, '/html/body/form/button').send_keys(Keys.ENTER)

