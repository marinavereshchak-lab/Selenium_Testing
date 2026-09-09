import pytest

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():

# Selenium Manager will auto-download the appropriate driver
    options = Options()
    options.add_argument("--headless")  # run without UI
    options.add_argument("--no-sandbox")  # required in many CI environments
    options.add_argument("--disable-dev-shm-usage")  # overcome limited /dev/shm size on Linux

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_successful_login(driver):
# 2. Открываем страницу с формой:
    driver.get("https://the-internet.herokuapp.com/login")
# 3. Заполняем текстовое поле:
    username_input = driver.find_element(By.ID, "username")
    username_input.clear()
    username_input.send_keys("tomsmith")
# 4. Заполняем поле пароля:
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys("SuperSecretPassword!")
# 15. Отправляем форму:


    wait = WebDriverWait(driver, 15)
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()
    wait.until(EC.text_to_be_present_in_element(
        (By.ID, "flash-messages"),
        "You logged into a secure area!"
    ))
    assert 'You logged into a secure area!' in driver.page_source

def test_unsuccessful_login(driver):
    # 2. Открываем страницу с формой:
    driver.get("https://the-internet.herokuapp.com/login")
    # 3. Заполняем текстовое поле:
    username_input = driver.find_element(By.ID, "username")
    username_input.clear()
    username_input.send_keys("tomsmith")
    # 4. Заполняем поле пароля:
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys("WrongPassword!")
    # 15. Отправляем форму:
    wait = WebDriverWait(driver, 15)
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()
    wait.until(EC.text_to_be_present_in_element(
        (By.ID, "flash-messages"),
        "Your password is invalid!"
    ))
    assert 'Your password is invalid!' in driver.page_source



