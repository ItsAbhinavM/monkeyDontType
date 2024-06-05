from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

def get_word_from_web(url, delay=0.1):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    
    try:
        while True:
            word_div = driver.find_element(By.CLASS_NAME, 'word.active')
            letters = word_div.find_elements(By.TAG_NAME, 'letter')
            word = ''.join([letter.text for letter in letters])
            word += ' '
            ActionChains(driver).send_keys(word).perform()
            time.sleep(delay)
    except Exception as e:
        print('Error:', e)
    finally:
        driver.quit()

url = 'https://monkeytype.com/'
get_word_from_web(url)
