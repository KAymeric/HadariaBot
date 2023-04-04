from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

from data import Data

def coroutine(browser):
    data = Data()

    input = browser.find_element('name','username')
    input.send_keys(data.pseudo)

    time.sleep(1)
    browser.find_element(By.XPATH,'//form/button').click()
    time.sleep(1)
    browser.find_element(By.CLASS_NAME,'website-14').click()
    
    time.sleep(4)
    all_win_handles = browser.window_handles
    browser.switch_to.window(all_win_handles[1])
    time.sleep(1)
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME,'fc-consent-root')))
    browser.find_element(By.CLASS_NAME,'fc-primary-button').click()
    
    time.sleep(1)
    browser.find_element(By.CLASS_NAME,'btn-secondary').click()

    input = browser.find_element('name','email')
    input.send_keys(data.email)
    input = browser.find_element('name','passe')
    input.send_keys(data.password)    
