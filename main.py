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
            identifyWords(driver,delay)
    except Exception as e:
        endCredits(driver)

def identifyWords(driver,delay):
    try:
        while True:
            word_div = driver.find_element(By.CLASS_NAME, 'word.active')
            letters = word_div.find_elements(By.TAG_NAME, 'letter')
            word = ''.join([letter.text for letter in letters])
            word += ' '
            ActionChains(driver).send_keys(word).perform()
            time.sleep(delay)
    except Exception as e:
        endCredits(driver)

def endCredits(driver):
    wpm=driver.find_element(By.CSS_SELECTOR, ".group.wpm").find_element(By.CLASS_NAME,"bottom").text
    acc=driver.find_element(By.CSS_SELECTOR, ".group.acc").find_element(By.CLASS_NAME,"bottom").text
    consistency = driver.find_element(By.CSS_SELECTOR, ".group.flat.consistency").find_element(By.CLASS_NAME, "bottom").text
    print("wpm: " + wpm)
    print("accuracy: " + acc)
    print("consistency: " + consistency)
    runAgain(driver)

def runAgain(driver):
    userChoice=input("do you wish to run again (y/n) : ")
    # time.sleep(30)
    if userChoice=='y':
        try:
            next_test_button = driver.find_element(By.ID, 'nextTestButton')
            next_test_button.click()
            time.sleep(1)
            identifyWords(driver,0.1)
        except Exception as e:
            print('Error clicking Next test button:', e)
    elif userChoice=='n':
        print("bye")
        try:
            driver.quit()  # Close the browser
        except Exception as e:
            pass  # Ignore any exceptions raised by driver.quit()
        quit()
    else:
        print("invalid input, please type it according to the format")
        runAgain()


url = 'https://monkeytype.com/'
get_word_from_web(url)
