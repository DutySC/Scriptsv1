import PK.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By
# from conftest import browser_SNILS

class search_patient_locators:
    LOCATOR_SEARCH_PATIENT_1 = (By.XPATH, '//span[contains(text(), "Регистратура")]')
    LOCATOR_SEARCH_PATIENT_2 = (By.XPATH, '//tbody/tr[7]/td[2]/a[1]/span[1]')
    LOCATOR_NEW_PATIENT = (By.XPATH, '//td[contains(text(), "Новый пациент")]')
    LOCATOR_LAST_NAME = (By.XPATH, '//body[1]//div[7]/div[1]/div[1]/table[1]//tr[4]/td[1]//input[1]')
    LOCATOR_FIRST_NAME = (By.XPATH, '//body[1]//div[7]/div[1]/div[1]/table[1]//tr[4]/td[2]//input[1]')
    LOCATOR_SURNAME = (By.XPATH, '//body[1]//div[7]/div[1]/div[1]/table[1]//tr[4]/td[3]//input[1]')
    LOCATOR_BIRTHDAY = (By.XPATH, '//tbody/tr[6]/td[1]/span[1]/div[1]/div[1]/input[1]')
    LOCATOR_CARD_NUMBER = (By.XPATH, '//body[1]/div[7]//tr[8]/td[1]/table[1]//img[1]')
    LOCATOR_SNILS = (By.XPATH, '//body[1]/div[7]//tr[10]/td[1]//input[1]')
    LOCATOR_ENTER_POLIS = (By.XPATH, '//body[1]/div[7]//td[1]/div[1]//div[1]/div[2]//td[2]//input[1]')
    LOCATOR_INSURANCE_COMPANY = (By.XPATH, '//body[1]/div[7]//tr[2]/td[1]//td[1]/div[1]//tr[4]//img[1]')
    LOCATOR_OBLASTI = (By.XPATH, '//body[1]/div[8]//div[1]/div[1]/div[1]/div[1]/div[1]//img[1]')
    LOCATOR_OBLAST = (By.XPATH, '//body[1]/div[9]//span[contains(text(), "Все")]')
    LOCATOR_OBLAST_OK = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_TYPE_OF_POLIS = (By.XPATH, '//body[1]/div[7]//div[1]/div[1]/div[1]//div[1]//div[1]/div[2]//tr[2]//img[1]')
    LOCATOR_CHOOSE_POLIS = (By.XPATH, '//span[contains(text(), "Временное свидетельство")]')
    LOCATOR_DATA_1 = (By.XPATH, '//body[1]/div[7]//div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]//tr[4]//div/div/div[1]')
    LOCATOR_DATA_2 = (By.XPATH, '//div[contains(text(), "Сегодня")]')
    LOCATOR_TAB_STATUS = (By.XPATH, '//div[contains(text(), "Соц.")]')
    LOCATOR_STATUS_OPEN = (By.XPATH, '//body[1]/div[7]//td[1]/div[1]//div[3]/div[2]//img[1]')
    LOCATOR_STATUS_OK = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_TAB_DOCUMENTS = (By.XPATH, '//div[contains(text(),"Документы")]')
    LOCATOR_TYPE_OF_DOCUMENTS = (By.XPATH, '//body[1]/div[7]//td[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]//tr[2]//img[1]')
    LOCATOR_CHOOSE_DOCUMENT = (By.XPATH, '//span[contains(text(), "Вид на жительство")]')
    LOCATOR_DATA_3 = (By.XPATH, '//body[1]/div[7]//td[1]/div[2]//tr[4]//div/div/div[1]')
    LOCATOR_DATA_4 = (By.XPATH, '//div[contains(text(), "Сегодня")]')
    LOCATOR_WHO_GAVE = (By.XPATH, '//body[1]/div[7]//td[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]//textarea[1]')
    LOCATOR_TAB_AREAS = (By.XPATH, '//body[1]/div[7]//td[1]/div[2]/table[1]/tbody[1]/tr[1]//div[2]/div[2]')
    LOCATOR_AREA = (By.XPATH, '//body[1]/div[7]//tbody[1]/tr[2]//tr[2]/td[1]//td[1]/div[1]//tr[2]//img[1]')
    LOCATOR_AREA_OK = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_ENTER_AREA = (By.XPATH, '//body[1]/div[7]//tr[2]/td[1]/div[2]//td/div[1]//tr[3]//img[1]')
    LOCATOR_CHOOSE_ANYCHINSKIY = (By.XPATH, '//a[contains(text(), "Анучинский")]')
    LOCATOR_CHOOSE_ABRICOSOVOE = (By.XPATH, '//a[contains(text(), "Абрикосовое")]')
    LOCATOR_HOME = (By.XPATH, '//body[1]/div[7]//tbody[1]//tbody[1]//tbody[1]/tr[2]//tr[2]/td[1]/div[1]//tr[4]/td[2]//input[1]')
    LOCATOR_OK = (By.XPATH, '//td[contains(text(), "ОК")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_1 = (By.XPATH, '//span[contains(text(), "Словари")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_2 = (By.XPATH, '//span[contains(text(), "Контрагенты")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_3 = (By.XPATH, '//span[contains(text(), "Карты пациентов")]')
    LOCATOR_PATIENT_FILTER_1 = (By.XPATH, '//div[4]/div[1]//span[1]//span[1]')
    LOCATOR_PATIENT_FILTER_2 = (By.XPATH, '//div[3]/div[1]//td[4]//input[1]')
    LOCATOR_PATIENT_FILTER_SEARCH_1 = (By.XPATH, '//td[2]/div[1]//span[contains(text(), "Найти")]')
    LOCATOR_LAST_NAME_NEWVERSION = (By.XPATH, '//span[contains(text(), "Новаяверсия")]')
    LOCATOR_DELETE_USER_1 = (By.XPATH, '//body[1]/div[2]/div[2]/div[4]/table[1]/tbody[1]/tr[5]/td[2]')
    LOCATOR_DICTIONARY_INDIVIDUAL_1 = (By.XPATH, '//span[contains(text(), "Словари")]')
    LOCATOR_DICTIONARY_INDIVIDUAL_2 = (By.XPATH, '//span[contains(text(), "Контрагенты")]')
    LOCATOR_DICTIONARY_INDIVIDUAL_3 = (By.XPATH, '//div[2]//tr[1]//span[contains(text(), "Контрагенты")]')
    LOCATOR_PATIENT_FILTER_3 = (By.XPATH, '//div[2]//span[contains(text(), "Показать фильтр")]')
    LOCATOR_PATIENT_FILTER_4 = (By.XPATH, '//td[6]//input[1]')
    LOCATOR_PATIENT_FILTER_SEARCH_2 = (By.XPATH, '//div[1]/div[1]/div[2]//span[contains(text(), "Найти")]')
    LOCATOR_DELETE_USER_2 = (By.XPATH, '//div[2]/div[2]//td[contains(text(), "Удалить")]')

class search_patient(BasePage):
    def create_patient(self):
        try:
            start_search_patient = time.time()
            self.find_element(search_patient_locators.LOCATOR_SEARCH_PATIENT_1).click()  # вкладка "Регистратура"
            self.find_element(search_patient_locators.LOCATOR_SEARCH_PATIENT_2).click()  # вкладка "Поиск пациентов"
            self.find_element_pb()  # прогрессбар
            time.sleep(3)  # ожидание
            self.find_element(search_patient_locators.LOCATOR_NEW_PATIENT).click()  # создание нового пациента
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            time.sleep(5) # ожидание
            search_string_1 = self.find_element(search_patient_locators.LOCATOR_LAST_NAME)  # ввод фамилии
            search_string_1.send_keys(prm.last_name)  # указывается фамилия
            search_string_2 = self.find_element(search_patient_locators.LOCATOR_FIRST_NAME)  # ввод имени
            search_string_2.send_keys(prm.first_name)  # указывается имя
            search_string_3 = self.find_element(search_patient_locators.LOCATOR_SURNAME)  # ввод отчетсва
            search_string_3.send_keys(prm.surname)  # указывается отчетсво
            self.find_element(search_patient_locators.LOCATOR_BIRTHDAY).click() # дата рождения
            search_string_4 = self.find_element(search_patient_locators.LOCATOR_BIRTHDAY)  # дата рождения
            search_string_4.send_keys(prm.data) # указывается дата рождения
            self.find_element(search_patient_locators.LOCATOR_CARD_NUMBER).click()  # кнопка для выдачи номера карты
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_SNILS).click()  # ввод СНИЛС
            search_string_5 = self.find_element(search_patient_locators.LOCATOR_SNILS)  # ввод СНИЛС
            search_string_5.send_keys(prm.snils) # указывается СНИЛС
            search_string_6 = self.find_element(search_patient_locators.LOCATOR_ENTER_POLIS)  # ввод номера полиса
            search_string_6.send_keys(prm.rand)  # указывается номер полиса
            self.find_element(search_patient_locators.LOCATOR_INSURANCE_COMPANY).click()  # окно для указания страховой компании
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            time.sleep(2)  # ожидание
            self.find_element(search_patient_locators.LOCATOR_OBLASTI).click()  # выкидное окно для указания областей
            self.find_element(search_patient_locators.LOCATOR_OBLAST).click()  # выбор всех областей
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_OBLAST_OK).click()  # кнопка "Ок"
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_TYPE_OF_POLIS).click()  # выбор вида полиса
            self.find_element(search_patient_locators.LOCATOR_TYPE_OF_POLIS).click()  # выбор вида полиса
            self.find_element(search_patient_locators.LOCATOR_CHOOSE_POLIS).click()  # указать временное свидетельство
            self.find_element(search_patient_locators.LOCATOR_DATA_1).click()  # дата выдачи
            self.find_element(search_patient_locators.LOCATOR_DATA_2).click()  # указать дату выдачи
            self.find_element(search_patient_locators.LOCATOR_TAB_STATUS).click() # вкладка Соц. статус
            self.find_element(search_patient_locators.LOCATOR_STATUS_OPEN).click() # окно выбора соц. статуса
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_STATUS_OK).click()  # подтверждения соц. статуса
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_TAB_DOCUMENTS).click()  # вкладка Документы/Адреса
            self.find_element(search_patient_locators.LOCATOR_TAB_DOCUMENTS).click()  # вкладка Документы/Адреса
            self.find_element(search_patient_locators.LOCATOR_TYPE_OF_DOCUMENTS).click()  # тип документа
            self.find_element(search_patient_locators.LOCATOR_CHOOSE_DOCUMENT).click()  # указать тип документа "Вид на жительство"
            self.find_element(search_patient_locators.LOCATOR_DATA_3).click()  # дата выдачи
            self.find_element(search_patient_locators.LOCATOR_DATA_4).click()  # указать дату выдачи
            search_string_7 = self.find_element(search_patient_locators.LOCATOR_WHO_GAVE)  # кем выдан
            search_string_7.send_keys(prm.mvd) # указать кем выдан - "МВД"
            self.find_element(search_patient_locators.LOCATOR_TAB_AREAS).click()  # подвкладка "Адреса"
            self.find_element(search_patient_locators.LOCATOR_AREA).click()  # ввод района
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_AREA_OK).click()  # кнопка "Ок"
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_ENTER_AREA).click()  # ввод адреса
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_CHOOSE_ANYCHINSKIY).click()  # выбрать Анучинский
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_CHOOSE_ABRICOSOVOE).click()  # выбрать Абрикосовое
            self.find_element_pb()  # прогрессбар
            search_string_8 = self.find_element(search_patient_locators.LOCATOR_HOME)  # выбрать дом
            search_string_8.send_keys(prm.home) # указать номер дома
            self.find_element(search_patient_locators.LOCATOR_OK).click()  # кнопка "ОК"
            self.find_element_pb()  # прогрессбар
            print('✅ Тестовый пациент - создан') # вывод
            ###########след.этап########################################################################################
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_1).click() # вкладка "Словари"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_2).click() # вкладка "Контрагенты"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_3).click() # вкладка "Карты пациентов"
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_PATIENT_FILTER_1).click()  # включить поиск по фильтрам
            search_string_9 = self.find_element(search_patient_locators.LOCATOR_PATIENT_FILTER_2)   # поиск по отчеству
            search_string_9.send_keys(prm.surname)   # ввод отчества пациента
            self.find_element(search_patient_locators.LOCATOR_PATIENT_FILTER_SEARCH_1).click()  # кнопка "Найти"
            self.actionchains(search_patient_locators.LOCATOR_LAST_NAME_NEWVERSION).perform()  # ПКМ по имени созданного пациента
            self.find_element(search_patient_locators.LOCATOR_DELETE_USER_1).click() # кнопка "Удалить"
            self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_1).click() # вкладка "Словари"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_2).click() # вкладка "Контрагенты"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_3).click() # вкладка "Контрагенты"
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_PATIENT_FILTER_3).click()  # включить поиск по фильтрам
            search_string_10 = self.find_element(search_patient_locators.LOCATOR_PATIENT_FILTER_4)   # поиск по отчеству
            search_string_10.send_keys(prm.surname)   # ввод отчества пациента
            self.find_element(search_patient_locators.LOCATOR_PATIENT_FILTER_SEARCH_2).click()  # кнопка "Найти"
            self.actionchains(search_patient_locators.LOCATOR_LAST_NAME_NEWVERSION).perform()  # ПКМ по имени созданного пациента
            self.find_element(search_patient_locators.LOCATOR_DELETE_USER_2).click() # кнопка "Удалить"
            self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            self.find_element_pb()  # прогрессбар
            print('✅ Тестовый пациент - удален') # вывод
            end_search_patient = time.time()
            full_search_patient = end_search_patient - start_search_patient
            print('   🔼 Модуль - "Поиск пациентов", выполнен за: ', round(full_search_patient, 2), 'с')
        except Exception as error:
            self.get_screenshots('Results/Results_sc/Поиск.png')
            print('❗️ Ошибка:', error)
            self.driver.quit()