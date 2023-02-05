import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_1_show_all_my_pets(my_pets_page):
    '''Проверяем, что на странице "Мои питомцы" отображаются все питомцы'''

    # Получаем количество питомцев указанных в статистике
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
    stat = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    quantity_stat = stat[0].text.split('\n')
    quantity_stat = quantity_stat[1].split(' ')
    quantity_stat = int(quantity_stat[1])

    # Получаем количество карточек питомцев
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
    my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    quantity_of_pets = len(my_pets)

    # Проверяем, что количество питомцев в статистике равно количеству карточек
    assert quantity_stat == quantity_of_pets, 'Данные статистики не совпадают с количеством карточек'

def test_2_pets_have_photo(my_pets_page):
    '''Проверяем, что на странице "Мои питомцы", хотя бы у половины питомцев есть фото'''

    # Получаем количество питомцев из данных статистики
    element = WebDriverWait(pytest.driver, 10).until\
            (EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
    stat = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    quantity_stat = stat[0].text.split('\n')
    quantity_stat = quantity_stat[1].split(' ')
    quantity_stat = int(quantity_stat[1])

    # Сохраняем в переменную элементы с атрибутом img
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    # Находим половину от количества питомцев
    half = quantity_stat // 2

    # Находим количество питомцев с фото
    quantity_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            quantity_photos += 1

    # Проверяем, что количество питомцев с фото больше или равно половине количества питомцев
    assert quantity_photos >= half, 'Количество питомцев с фото меньше половины количества питомцев'

def test_3_all_pets_have_name_age_breed(my_pets_page):
    '''проверяем, что на странице "Мои питомцы", у всех питомцеы есть имя, возраст и порода'''

    element = WebDriverWait(pytest.driver, 10).until\
        (EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
    # Сохраняем в переменную данные о питомцах
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Проверяем начилие всех необходимых атрибутов в данных
    for i in range(len(pet_data)):
        ex_pet_data = pet_data[i].text.replace('\n', '').replace('*', '')
        final_pet_data = ex_pet_data.split(' ')
        res = len(final_pet_data)
        assert res == 3, 'не у всех питомцев есть имя, возраст или порода'

def test_4_pets_have_different_name(my_pets_page):
    '''Поверяем, что на странице "Мои питомцы", у всех питомцев разные имена'''

    element = WebDriverWait(pytest.driver, 10).until\
            (EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    # Сохраняем в переменную элементы с данными о питомцах
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Процедура выборки имён из данных
    pets_name = []
    for i in range(len(pet_data)):
        ex_pet_data = pet_data[i].text.replace('\n', '').replace('×', '')
        final_pet_data = ex_pet_data.split(' ')
        pets_name.append(final_pet_data[0])

    # Процедура поиска одинаковых имён
    # Если счётчик r равен 0, то одинаковых имён нет
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    assert r == 0, 'В списке представлены питомцы имеющие одинаковые имена'

def test_5_all_pets_are_different(my_pets_page):
    '''Поверяем что на странице "Мои питомцы" нет повторяющихся питомцев'''

    element = WebDriverWait(pytest.driver, 10).until\
            (EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    # Сохраняем в переменную данные о питомцах
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Преобразуем данные в удобный для обработки вид
    list_data = []
    for i in range(len(pet_data)):
        ex_pet_data = pet_data[i].text.replace('\n', '').replace('×', '')
        final_pet_data = ex_pet_data.split(' ')
        list_data.append(final_pet_data)

    # Полученные данные преобразуем в склееную строку
    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '

    # Получаем список
    list_line = line.split(' ')

    # Преобразуем список в множество
    set_list_line = set(list_line)

    # Находим количество элементов списка и множества
    a = len(list_line)
    b = len(set_list_line)

    # Из количества элементов списка вычитаем количество элементов множества
    res = a - b

    # Если количество элементов == 0 значит карточки с одинаковыми данными отсутствуют
    assert res == 0, 'В списке содержатся повторяющиеся питомцы'