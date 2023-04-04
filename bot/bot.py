from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from data import Data
from process import coroutine

data = Data()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
browser  = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

browser.get(data.url)
coroutine(browser)