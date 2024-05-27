from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_word_from_web(url):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    
    try:
        # Explicit wait for the element to be present
        word_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'word active'))
        )
        word = word_div.text
        print(word)
        
        input_field = driver.find_element(By.CLASS_NAME, '')  # Replace with actual class name or ID
        input_field.send_keys(word)

    except Exception as e:
        print('Failed to find the word active div:', e)
    finally:
        driver.quit()

url = 'https://monkeytype.com/'
get_word_from_web(url)
