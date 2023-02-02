import pytest
from selenium.webdriver.common.by import By


def test_show_all_my_pets(my_pets_page):
    '''Проверяем, что на странице "Мои питомцы" отображаются все питомцы'''

    # Получаем количество питомцев указанных в статистике
    stat = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    quantity_stat = stat[0].text.split('\n')
    quantity_stat = quantity_stat[1].split(' ')
    quantity_stat = int(quantity_stat[1])

    # Получаем количество карточек питомцев
    my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    quantity_of_pets = len(my_pets)

    # Проверяем, что количество питомцев в статистике равно количеству карточек
    assert quantity_stat == quantity_of_pets, 'Данные статистики не совпадают с количеством карточек'

