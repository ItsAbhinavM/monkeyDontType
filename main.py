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
        try:
            while True:
                identifyWords(driver,delay)
        except Exception as e:
            endCredits(driver)
    except KeyboardInterrupt:
        print("keyboard interpution detected")
        quit()

def identifyWords(driver,delay):
    try:
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
    except KeyboardInterrupt:
        print("keyboard interpution detected")
        quit()

def endCredits(driver):
    wpm=driver.find_element(By.CSS_SELECTOR, ".group.wpm").find_element(By.CLASS_NAME,"bottom").text
    acc=driver.find_element(By.CSS_SELECTOR, ".group.acc").find_element(By.CLASS_NAME,"bottom").text
    consistency = driver.find_element(By.CSS_SELECTOR, ".group.flat.consistency").find_element(By.CLASS_NAME, "bottom").text
    if len(wpm)==0:
        runAgain(driver)
    else:
        print("wpm: " + wpm)
        print("accuracy: " + acc)
        print("consistency: " + consistency)
        runAgain(driver)

def runAgain(driver):
    userChoice=input("do you wish to run again (y/n) : ")
    if userChoice=='y':
        try:
            next_test_button = driver.find_element(By.ID, 'nextTestButton')
            next_test_button.click()
            time.sleep(1)
            identifyWords(driver,0.1)
        except Exception:
            print('Error clicking Next test button:')
    elif userChoice=='n':
        print("bye")
        try:
            driver.quit() 
        except Exception as e:
            pass 
        quit()
    else:
        print("invalid input, please type it according to the format")
        runAgain()

banner=f"""
███╗   ███╗ ██████╗ ███╗   ██╗██╗  ██╗███████╗██╗   ██╗██████╗  ██████╗ ███╗   ██╗████████╗████████╗██╗   ██╗██████╗ ███████╗
████╗ ████║██╔═══██╗████╗  ██║██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝╚══██╔══╝╚██╗ ██╔╝██╔══██╗██╔════╝
██╔████╔██║██║   ██║██╔██╗ ██║█████╔╝ █████╗   ╚████╔╝ ██║  ██║██║   ██║██╔██╗ ██║   ██║      ██║    ╚████╔╝ ██████╔╝█████╗  
██║╚██╔╝██║██║   ██║██║╚██╗██║██╔═██╗ ██╔══╝    ╚██╔╝  ██║  ██║██║   ██║██║╚██╗██║   ██║      ██║     ╚██╔╝  ██╔═══╝ ██╔══╝  
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██╗███████╗   ██║   ██████╔╝╚██████╔╝██║ ╚████║   ██║      ██║      ██║   ██║     ███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝      ╚═╝      ╚═╝   ╚═╝     ╚══════╝
                                                                                                                             """
print(banner)
print("This version does not support automated cookie detection, kindly click on the accept cookie button for better experience")
url = 'https://monkeytype.com/'
get_word_from_web(url)
