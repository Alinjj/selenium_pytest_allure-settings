import allure_commons
import pytest
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions()


class tests(object):
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=r'/\chromedriver.exe')

    def teardown(self):
        self.driver.quit()

    # @allure.feature('Open pages')
    # @allure.story('Открыть страницу вк')
    # @allure.severity('blocker')
    # def test_selenium(self):
    #     self.driver.get('https://vk.com/')
    #     try:
    #         self.driver.get('https://vk.com/')
    #         with allure.MASTER_HELPER.step('Скриншот'):
    #             allure.MASTER_HELPER.attach(self.driver.get_screenshot_as_png(), name='screen',attachment_type=AttachmentType.PNG)
    #         email_input = self.driver.find_element(By.ID,'index_email')
    #         email_input.clear()
    #         email_input.send_keys('1')
    #
    #         password_input = self.driver.find_element(By.ID,'index_pass')
    #         password_input.clear()
    #         password_input.send_keys('ds')
    #
    #        # login_btn = driver.find_element(By.ID,'index_login_button').click()
    #         password_input.send_keys(Keys.ENTER)
    #
    #
    #     except Exception as ex:
    #         print(ex)
    #     finally:
    #         self.driver.close()
    #         self.driver.quit()


# @pytest.mark.xfail
@allure.feature('Open pages')
@allure.story('Открыть VK')
@allure.severity(allure.severity_level.CRITICAL)
def test_selenium():
    driver = webdriver.Chrome(executable_path=r'/\chromedriver.exe')
    driver.get('')
    with allure.step('Скриншот'):
        allure.attach(driver.get_screenshot_as_png(), name='screen', attachment_type=AttachmentType.PNG)
    with allure.step('Заполняет поле email'):
        email_input = driver.find_element(By.ID, 'index_email')
        email_input.clear()
        email_input.send_keys('1')
        email_input.send_keys(Keys.ENTER)
    # login_btn = driver.find_element(By.ID,'index_login_button').click()

    driver.close()
    driver.quit()


# @pytest.mark.xfail
# @allure.feature('Open pages')
# @allure.story('Открыть VK')
# @allure.severity(allure.severity_level.CRITICAL)
# def test_selenium():
#     driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\selenium_pytest_allure\chromedriver.exe')
#
#     try:
#         driver.get('https://vk.com/')
#         with allure.MASTER_HELPER.step('Скриншот'):
#             allure.MASTER_HELPER.attach(driver.get_screenshot_as_png(), name='screen',
#                                         attachment_type=AttachmentType.PNG)
#         email_input = driver.find_element(By.ID, 'index_email')
#         email_input.clear()
#         email_input.send_keys('1')
#
#         password_input = driver.find_element(By.ID, 'index_pass')
#         password_input.clear()
#         password_input.send_keys('ds')
#
#         # login_btn = driver.find_element(By.ID,'index_login_button').click()
#         password_input.send_keys(Keys.ENTER)
#         assert driver.current_url != 'https://vk.com/'
#
#
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
