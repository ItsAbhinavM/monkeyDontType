from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

def get_word_from_web(url, delay=0.1):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # install chromium
    driver.get(url)
    # driver.find_element(By.CSS_SELECTOR,'active acceptAll').click() # sfocus on the page ; the unwanted bug_4ao5eF8B
    
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
        wpm=driver.find_element(By.CSS_SELECTOR, ".group.wpm").find_element(By.CLASS_NAME,"bottom").text
        acc=driver.find_element(By.CSS_SELECTOR, ".group.acc").find_element(By.CLASS_NAME,"bottom").text
        consistency = driver.find_element(By.CSS_SELECTOR, ".group.flat.consistency").find_element(By.CLASS_NAME, "bottom").text
        print("wpm: " + wpm)
        print("accuracy: " + acc)
        print("consistency: " + consistency)
        driver.quit()

url = 'https://monkeytype.com/'
browser= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
try:
    accept_cookie_btn = browser.find_element(By.CSS_SELECTOR, ".button.active.acceptAll")
    accept_cookie_btn.click()
except Exception as e:
    print("exception occured in finding the cookie button : ",e)
    pass
get_word_from_web(url)
