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
    
    while True:
        try :
            input = browser.find_element(By.CLASS_NAME,'form-control-lg')
            input.send_keys(data.pseudo)
        except:
            pass
        
        try:
            browser.execute_script("window.scrollTo(0, 400)")
            time.sleep(4)
            browser.find_element(By.XPATH,'//*[@id="login-form"]/button').click()
        except:
            pass

        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'site_button_1')))
        time.sleep(2)
        browser.find_element(By.ID,'site_button_1').click()
        
        time.sleep(15)
        all_win_handles = browser.window_handles
        browser.switch_to.window(all_win_handles[1])
        time.sleep(1)

        if data.isConnected:
            input = browser.find_element(By.ID,'pseudo')
            input.send_keys(data.pseudo)
            browser.find_element(By.ID,'btnvote').click()
            time.sleep(5)

            browser.close()
            all_win_handles = browser.window_handles
            browser.switch_to.window(all_win_handles[0])
            time.sleep(5)
            browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div[3]/div/div/div/div/div/a').click()
            

            time.sleep(5430)

        else :
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME,'fc-consent-root')))
            browser.find_element(By.CLASS_NAME,'fc-primary-button').click()
            
            time.sleep(1)
            browser.find_element(By.CLASS_NAME,'btn-secondary').click()

            input = browser.find_element('name','email')
            input.send_keys(data.email)
            input = browser.find_element('name','passe')
            input.send_keys(data.password)

            thisUrl = browser.current_url
            while browser.current_url == thisUrl:
                pass

            data.isConnected = True
            browser.close()
            all_win_handles = browser.window_handles
            browser.switch_to.window(all_win_handles[0])

            time.sleep(1)
