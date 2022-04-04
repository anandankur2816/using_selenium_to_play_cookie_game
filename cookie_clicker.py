import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
timeout = time.time() + 60*4
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service("A:\Webservices ML\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get ids of elements in table
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]
# print(item_ids)
curr_time = time.time()
current_id = 0

while time.time() < timeout:
    driver.find_element(By.ID, "cookie").click()
    if time.time() > curr_time + 5:
        driver.find_element(By.ID, item_ids[current_id]).click()
        time.sleep(1)
        # print(driver.find_element_by_xpath('//*[@id="buyCursor"]/div'))
        count_id = f'//*[@id="{item_ids[current_id]}"]/div'
        # print(count_id)
        try:
            if driver.find_element_by_xpath(count_id).text =='1':
                current_id += 1
        except selenium.common.exceptions.NoSuchElementException:
            pass
        curr_time = time.time()
    # print(cookie_count)

# Print cookie count per second
print(driver.find_element_by_id("cps").text)
print("Done")