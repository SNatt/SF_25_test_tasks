import pytest
import time

from settings import email, password
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('/web_drivers/chromedriver.exe')

    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


@pytest.fixture()
def my_pets_page():

    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys(email)

    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys(password)

    # Нажимаем кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Переходим на страницу "Мои питомцы"
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()
    time.sleep(10)

