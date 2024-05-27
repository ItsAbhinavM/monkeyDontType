from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_word_from_web(url):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    
    try:
        word_div = driver.find_element(By.CLASS_NAME, 'word.active')
        word=word_div.text
        # input_field=driver.find_element(By)
        # word_div.send_keys(word)
        print(word)

    except Exception as e:
        print('Failed to find the word-active div:', e)
    # finally:
    #     driver.quit()

url = 'https://monkeytype.com/'
get_word_from_web(url)