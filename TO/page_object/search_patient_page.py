import TO.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
# from conftest import browser_SNILS

class search_patient_locators:
    LOCATOR_SEARCH_PATIENT_1 = (By.XPATH, '//span[contains(text(), "Регистратура")]')
    LOCATOR_SEARCH_PATIENT_2 = (By.XPATH, '//tbody/tr[13]/td[2]/a[1]/span[1]')
    LOCATOR_NEW_PATIENT = (By.XPATH, '//td[contains(text(), "Новый пациент")]')
    LOCATOR_FULL_WINDOW = (By.XPATH, '//tbody/tr[2]/td[2]//div[4]')
    LOCATOR_LAST_NAME = (By.XPATH, '//div[7]/div[1]/div[1]/table[1]//tr[4]/td[1]//input[1]')
    LOCATOR_FIRST_NAME = (By.XPATH, '//div[7]/div[1]/div[1]/table[1]//tr[4]/td[2]//input[1]')
    LOCATOR_SURNAME = (By.XPATH, '//div[7]/div[1]/div[1]/table[1]//tr[4]/td[3]//input[1]')
    LOCATOR_BIRTHDAY = (By.XPATH, '//tr[6]/td[1]/span[1]//input[1]')
    LOCATOR_CARD_NUMBER = (By.XPATH, '//div[7]//tr[8]/td[1]//img[1]')
    LOCATOR_SNILS = (By.XPATH, '//div[7]//tr[10]/td[1]//input[1]')
    LOCATOR_ENTER_POLIS = (By.XPATH, '//body[1]/div[7]//td[1]/div[1]//div[1]/div[2]//td[2]//input[1]')
    LOCATOR_INSURANCE_COMPANY = (By.XPATH, '//body[1]/div[7]//tr[2]/td[1]//td[1]/div[1]//tr[4]//img[1]')
    LOCATOR_OBLAST_OK = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_TYPE_OF_POLIS = (By.XPATH, '//body[1]/div[7]//div[1]/div[1]//div[1]//td[1]/div[1]/div[2]//tr[2]//img[1]')
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
    LOCATOR_TAB_AREAS = (By.XPATH, '//div[2]/table[1]//div[contains(text(), "Адреса")]')
    LOCATOR_AREA = (By.XPATH, '//body[1]/div[7]//tbody[1]/tr[2]//tr[2]/td[1]//td[1]/div[1]//tr[2]//img[1]')
    LOCATOR_AREA_ZABAYKALSKY = (By.XPATH, '//span[contains(text(), "Республика Коми")]')
    LOCATOR_AREA_OK = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_ENTER_AREA_1 = (By.XPATH, '//body[1]/div[7]//tr[2]/td[1]/div[2]//td/div[1]//tr[3]//img[1]')
    LOCATOR_ENTER_AREA_2 = (By.XPATH, '//a[contains(text(), "Авиатор")]')
    LOCATOR_HOME = (By.XPATH, '//body[1]/div[7]//tbody[1]//tbody[1]//tbody[1]/tr[2]//tr[2]/td[1]/div[1]//tr[4]/td[2]//input[1]')
    LOCATOR_OK = (By.XPATH, '//div[1]/div/div/div[2]//td[contains(text(), "ОК")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_1 = (By.XPATH, '//span[contains(text(), "Еще")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_2 = (By.XPATH, '//span[contains(text(), "Словари")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_3 = (By.XPATH, '//span[contains(text(), "Контрагенты")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_4 = (By.XPATH, '//span[contains(text(), "Карты пациентов")]')
    LOCATOR_FILTER_1 = (By.XPATH, '//tbody//td[2]/div[1]//span[contains(text(), "Показать фильтр")]')
    LOCATOR_FILTER_2 = (By.XPATH, '//div[3]/div[1]//td[3]//input[1]')
    LOCATOR_FILTER_3 = (By.XPATH, '//div[3]/div[1]//td[4]//input[1]')
    LOCATOR_FILTER_4 = (By.XPATH, '//div[3]/div[1]//td[5]//input[1]')
    LOCATOR_FILTER_5 = (By.XPATH, '//td[2]/div[1]//span[contains(text(), "Найти")]')
    LOCATOR_LAST_NAME_NEWVERSION_1 = (By.XPATH, '//span[contains(text(), "Новаяверсия")]')
    LOCATOR_DELETE_USER_1 = (By.XPATH, '//body[1]/div[2]/div[2]/div[4]/table[1]/tbody[1]/tr[7]/td[2]')
    LOCATOR_DICTIONARY_INDIVIDUAL_1 = (By.XPATH, '//span[contains(text(), "Еще")]')
    LOCATOR_DICTIONARY_INDIVIDUAL_2 = (By.XPATH, '//span[contains(text(), "Словари")]')
    LOCATOR_DICTIONARY_INDIVIDUAL_3 = (By.XPATH, '//span[contains(text(), "Контрагенты")]')
    LOCATOR_DICTIONARY_INDIVIDUAL_4 = (By.XPATH, '//span[contains(text(), "Контрагенты физ. лица")]')
    LOCATOR_FILTER_CATALOGS_2 = (By.XPATH, '//body[1]//div[3]/div[1]//td[2]//input[1]')
    LOCATOR_FILTER_CATALOGS_3 = (By.XPATH, '//body[1]//div[3]/div[1]//td[3]//input[1]')
    LOCATOR_FILTER_CATALOGS_4 = (By.XPATH, '//body[1]//div[3]/div[1]//td[4]//input[1]')
    LOCATOR_CATALOGS_1 = (By.XPATH, '//div[@id="TreeArea_CATALOGS_DEFAULT"]')
    LOCATOR_CATALOGS_2 = (By.XPATH, '//td[contains(text(), "Список")]')
    LOCATOR_LAST_NAME_NEWVERSION_2 = (By.XPATH, '//tbody/tr[1]/td[4]/span[contains(text(), "Новаяверсия")]')
    LOCATOR_DELETE_USER_2 = (By.XPATH, '//body[1]/div[2]/div[2]//td[2][contains(text(), "Удалить")]')

class search_patient(BasePage):
    def create_patient(self):
        global end_search_patient, start_search_patient
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
            self.find_element(search_patient_locators.LOCATOR_FULL_WINDOW).click()
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
            search_string_5.send_keys(prm.snils) # указывается статичный СНИЛС
            # search_string_5.send_keys(browser_SNILS())  # указывается динамический СНИЛС
            search_string_6 = self.find_element(search_patient_locators.LOCATOR_ENTER_POLIS)  # ввод номера полиса
            search_string_6.send_keys(prm.rand)  # указывается номер полиса
            self.find_element(search_patient_locators.LOCATOR_INSURANCE_COMPANY).click()  # окно для указания страховой компании
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            time.sleep(2)  # ожидание
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
            self.find_element(search_patient_locators.LOCATOR_AREA_ZABAYKALSKY).click() #
            self.find_element(search_patient_locators.LOCATOR_AREA_OK).click()  # кнопка "Ок"
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_ENTER_AREA_1).click()  # ввод адреса
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_ENTER_AREA_2).click() # ввод адреса
            self.find_element_pb()  # прогрессбар
            search_string_8 = self.find_element(search_patient_locators.LOCATOR_HOME)  # выбрать дом
            search_string_8.send_keys(prm.home) # указать номер дома
            self.find_element(search_patient_locators.LOCATOR_OK).click()  # кнопка "ОК"
            self.find_element_pb()  # прогрессбар
            print('✅ Тестовый пациент - создан') # вывод
            ###########след.этап########################################################################################
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_1).click() # вкладка "Еще"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_2).click() # вкладка "Словари"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_3).click() # вкладка "Контрагенты"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_4).click() # вкладка "Карты пациентов"
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_FILTER_1).click()
            search_string_9 = self.find_element(search_patient_locators.LOCATOR_FILTER_2)
            search_string_9.send_keys(prm.last_name)
            search_string_10 = self.find_element(search_patient_locators.LOCATOR_FILTER_3)
            search_string_10.send_keys(prm.first_name)
            search_string_11 = self.find_element(search_patient_locators.LOCATOR_FILTER_4)
            search_string_11.send_keys(prm.surname)
            self.find_element(search_patient_locators.LOCATOR_FILTER_5).click()
            self.find_element_pb()  # прогрессбар
            self.actionchains(search_patient_locators.LOCATOR_LAST_NAME_NEWVERSION_1).perform()  # ПКМ по имени созданного пациента
            self.find_element(search_patient_locators.LOCATOR_DELETE_USER_1).click() # кнопка "Удалить"
            self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_1).click()  # вкладка "Еще"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_2).click() # вкладка "Словари"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_3).click() # вкладка "Контрагенты"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_4).click() # вкладка "Контрагенты"
            try:
                self.find_element_pb(time=60)  # прогрессбар
                self.find_element_pb(time=60)  # прогрессбар
            except TimeoutException:
                time.sleep(50)
            search_string_9 = self.find_element(search_patient_locators.LOCATOR_FILTER_CATALOGS_2) # фамилия
            search_string_9.send_keys(prm.last_name) # написать фамилию
            search_string_10 = self.find_element(search_patient_locators.LOCATOR_FILTER_CATALOGS_3) # имя
            search_string_10.send_keys(prm.first_name) # написать имя
            search_string_11 = self.find_element(search_patient_locators.LOCATOR_FILTER_CATALOGS_4) # отчество
            search_string_11.send_keys(prm.surname) # написать отчество
            self.actionchains(search_patient_locators.LOCATOR_CATALOGS_1).perform()  # ПКМ по каталогу
            self.find_element(search_patient_locators.LOCATOR_CATALOGS_2).click()  # поиск по списку
            try:
                self.find_element_pb()  # прогрессбар
            except TimeoutException:
                time.sleep(10)
            self.actionchains(search_patient_locators.LOCATOR_LAST_NAME_NEWVERSION_2).perform() # ПКМ по имени созданного пациента
            self.find_element(search_patient_locators.LOCATOR_DELETE_USER_2).click() # кнопка "Удалить"
            self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            self.find_element_pb()  # прогрессбар
            print('✅ Тестовый пациент - удален')  # вывод
            end_search_patient = time.time()
            full_search_patient = end_search_patient - start_search_patient
            print('   🔼 Модуль - "Поиск пациентов", выполнен за: ', round(full_search_patient, 2), 'с')
        except Exception as error:
            full_search_patient = end_search_patient - start_search_patient
            print('   ❌ Модуль - "Поиск пациентов", завершен за: ', round(full_search_patient, 2), 'с')
            self.get_screenshots('Results/Results_sc/Поиск.png')
            print('❗️ Ошибка:', error)
            self.driver.quit()
