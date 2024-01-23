from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle

import time


options = webdriver.ChromeOptions()






def test_selenium():
    driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\selenium_pytest\chromedriver.exe',options)
    try:
        driver.get('https://mail.ru/')

        enter_btn = driver.find_element(By.XPATH,'//*[@id="mailbox"]/div[1]/button').click()
        user_name = driver.find_element(By.NAME,'username').send_keys('test_qa_python')
        enter_btn_log_in = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div[2]/div/div/form/div[2]/div[2]/div[3]/div/div/div[1]/div/button/span').click()
        time.sleep(10)





    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
