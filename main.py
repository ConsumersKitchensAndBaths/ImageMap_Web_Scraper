# import requests
# from cgitb import text
# import pyodbc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
import time

IMPLICIT_WAIT_TIME = 30
SLEEP_TIMER = 5

def launchBrowser():
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("start-maximized")
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--disable-dev-shm-usage")
  driver = webdriver.Chrome(options=chrome_options)
  driver.get('https://amazing-brahmagupta.67-225-141-216.plesk.page/wp-admin/plugins.php?page=image-map-pro- wordpress')
  return driver


# RESTLET_URL = ''
# response = requests.get(RESTLET_URL)
driver = launchBrowser()
time.sleep(SLEEP_TIMER) 
driver.implicitly_wait(IMPLICIT_WAIT_TIME)
driver.find_element(by=By.ID, value="user_login").send_keys("domains@consumersmail.com")
driver.find_element(by=By.ID, value="user_pass").send_keys("CSRruUgt&CQmc&PSABf1p9s1")
submit_button = driver.find_element(by=By.ID, value="wp-submit").send_keys(Keys.ENTER)

# WebDriverWait(driver, timeout=10).until(document_initialised)
driver.implicitly_wait(IMPLICIT_WAIT_TIME)
time.sleep(SLEEP_TIMER) 
if len(driver.find_elements(by=By.ID, value="wcp-tour-simple-button-skip")) > 0:
  driver.find_element(by=By.ID, value="wcp-tour-simple-button-skip").click()
time.sleep(SLEEP_TIMER) 
driver.implicitly_wait(IMPLICIT_WAIT_TIME)
buttons = driver.find_elements(by=By.CLASS_NAME, value="wcp-editor-main-button-text")
driver.implicitly_wait(IMPLICIT_WAIT_TIME)
buttons[8].click()
time.sleep(SLEEP_TIMER) 
driver.implicitly_wait(IMPLICIT_WAIT_TIME)
time.sleep(SLEEP_TIMER)
driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div[3]/div/div/div[2]/textarea").send_keys("abc") # Paste JSON
driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div[4]/div[2]").click()
# time.sleep(SLEEP_TIMER)
# for txt in textareas:
#     print('1')
#     txt.send_keys("abc")
        
    
