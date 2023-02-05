import pytest

from settings import email, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
    pytest.driver.find_element(By.ID, 'email').send_keys(email)

    # Вводим пароль
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'pass')))
    pytest.driver.find_element(By.ID, 'pass').send_keys(password)

    # Нажимаем кнопку входа в аккаунт
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Переходим на страницу "Мои питомцы"
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()