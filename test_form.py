import pytest
import allure
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():


    options = Options()
    options.add_argument("--headless")  # run without UI
    options.add_argument("--no-sandbox")  # required in many CI environments
    options.add_argument("--disable-dev-shm-usage")  # overcome limited /dev/shm size on Linux

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
@allure.feature("Авторизация")
@allure.title("Успешный вход: корректные логин и пароль")
@allure.description("Тест проверяет, что пользователь может успешно войти в защищённую зону с валидными учётными данными")
def test_successful_login(driver):
    with allure.step("Открыть страницу входа"):
        driver.get("https://the-internet.herokuapp.com/login")
    with allure.step("Ввести логин и пароль"):
        username_input = driver.find_element(By.ID, "username")
        username_input.clear()
        username_input.send_keys("tomsmith")

        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys("SuperSecretPassword!")

    with allure.step("Нажать кнопку входа и дождаться сообщения об успехе"):
        wait = WebDriverWait(driver, 15)
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.ID, "flash-messages"),
            "You logged into a secure area!"
        ))
    assert 'You logged into a secure area!' in driver.page_source
@allure.feature("Авторизация")
@allure.title("Неуспешный вход: некорректный пароль")
@allure.description("Тест проверяет, что при неверном пароле система показывает сообщение об ошибке")
def test_unsuccessful_login(driver):
    with allure.step("Открыть страницу входа"):
        driver.get("https://the-internet.herokuapp.com/login")
    with allure.step("Ввести логин и неверныйпароль"):
        username_input = driver.find_element(By.ID, "username")
        username_input.clear()
        username_input.send_keys("tomsmith")

        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys("WrongPassword!")
    with allure.step("Нажать кнопку входа и дождаться сообщения об ошибке"):
        wait = WebDriverWait(driver, 15)
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.ID, "flash-messages"),
            "Your password is invalid!"
        ))
    assert 'Your password is invalid!' in driver.page_source



