from selenium.common import UnexpectedAlertPresentException, ElementClickInterceptedException
import KURO.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By

class locators_doctors_diary:
    LOCATOR_DIARY_1 = (By.XPATH, '//span[contains(text(), "Рабочие места")]')
    LOCATOR_DIARY_2 = (By.XPATH, '//body[1]//tr[1]//span[1][contains(text(), "Дневник")]')
    LOCATOR_REGISTER_1 = (By.XPATH, '//body[1]//table[5]//td[2]')
    LOCATOR_SEARCH_1 = (By.XPATH, '//div[@name="search_patient_form"]//table[@name="fullSearchRegimContainer"]//td[5]//input[@type="text"]')
    LOCATOR_SEARCH_2 = (By.XPATH, '//td[contains(text(),"Найти")]')
    LOCATOR_CHOICE_PATIENT = (By.XPATH, f'//body[1]//tr[1]//tr[1]//a[contains(text(), "{prm.name_patient_1}")]')
    LOCATOR_SERVICES = (By.XPATH, '//div[@name="makeReg"]//tr[@name="TR_SERVICES"]//input')
    LOCATOR_SERVICE = (By.XPATH, '//div[@name="ComboItemsList_SERVICES"]//tr[@se_code_attr="B01.047.001"]')
    LOCATOR_REGISTER_2 = (By.XPATH, '//td[3][contains(text(), "Записать")]')
    LOCATOR_CLOSE_1 = (By.XPATH, '//body[1]/div[8]//div[5]')
    LOCATOR_PROVIDE_SERVICE = (By.XPATH, '//a[contains(text(), "Оказать")]')
    LOCATOR_NEW_CREATE = (By.XPATH, '//div[contains(text(), "Создать новый")]')
    LOCATOR_BASIC_1 = (By.XPATH, '//body[1]/div[7]//tr[2]//div[1]//tr[2]/td[2]//img[1]')
    LOCATOR_BASIC_1_2_3 = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_BASIC_2_1 = (By.XPATH, '//body[1]//td[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]//tr[4]/td[1]//img[1]')
    LOCATOR_BASIC_2_2 = (By.XPATH, '//span[contains(text(), "Без перемен")]')
    LOCATOR_BASIC_3_1 = (By.XPATH, '//body[1]/div[7]//tr[2]/td/div[1]//tr[4]/td[2]//img[1]')
    LOCATOR_BASIC_3_2 = (By.XPATH, '//span[contains(text(), "Направлен на обследования")]')
    LOCATOR_DIAGNOSIS = (By.XPATH, '//div[contains(text(), "Диагноз")]')

    LOCATOR_MKB = (By.XPATH, '//body[1]/div[7]//tr[3]//tr[3]//tr[3]//tr[1]/td[1]//img[1]')
    LOCATOR_MKB_SEARCH_1 = (By.XPATH, '//body[1]/div[8]//tr[2]/td[1]//input[1]')
    LOCATOR_MKB_SEARCH_2 = (By.XPATH, '//td[contains(text(), "Поиск")]')
    LOCATOR_MKB_CHOICE = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_MKB_DISEASE_1 = (By.XPATH, '//body[1]/div[7]//div[8]/table[1]/tbody/tr[3]//tr[3]//td[4]//img[1]')
    LOCATOR_MKB_DISEASE_2 = (By.XPATH, '//body[1]/div[8]//span[2][contains(text(), "Острое")]')
    LOCATOR_SAVE_SERVICE = (By.XPATH, '//body[1]/div[7]//table[2]//td[2][contains(text(), "Сохранить")]')
    LOCATOR_PATIENT_RCM = (By.XPATH, f'//body[1]//a[contains(text(), "{prm.name_patient_1}")]')
    LOCATOR_CANCEL_SERVICE = (By.XPATH, '//td[contains(text(), "Отменить оказание")]')
    LOCATOR_MARKER = (By.XPATH, '//body[1]//div[3]/div[1]//tr[1]/td[5]')
    LOCATOR_DELETE_PATIENT = (By.XPATH, '//body[1]/div[2]/div[15]/div[10]/table[1]/tbody[1]/tr[23]/td[2][contains(text(), "Удалить направление")]')

class doctors_diary(BasePage):
    def diary(self):
        self.find_element(locators_doctors_diary.LOCATOR_DIARY_1).click() # вкладка "Рабочие места"
        self.find_element(locators_doctors_diary.LOCATOR_DIARY_2).click() # вкладка "Дневник врача"
        start_diary = time.time() # начало отчета времени формирования окна
        self.find_element_pb() # прогрессбар
        self.find_element_pb()  # прогрессбар
        # time.sleep(3)  # ожидание
        end_diary = time.time() # конец отчета времени формирования окна
        full_diary = end_diary - start_diary # суммарное время формирования окна "Дневник врача"
        if full_diary <= 10: # условие
            print('✅ Формирования окна - Дневник врача: ', round(full_diary, 2), 'сек')
        else:
            print('⚠️️ Формирования окна - Дневник врача: ', round(full_diary, 2), 'сек')
        try:
            self.find_element(locators_doctors_diary.LOCATOR_REGISTER_1).click() #кнопка "Запись"
        except ElementClickInterceptedException:
            self.find_element(locators_doctors_diary.LOCATOR_REGISTER_1).click()  # кнопка "Запись"
        self.find_element_pb()  # прогрессбар
        self.find_element_pb()  # прогрессбар
        # time.sleep(3) # ожидание
        search_string_1 = self.find_element(locators_doctors_diary.LOCATOR_SEARCH_1) # поиск тестового пациента 11/003414
        search_string_1.send_keys(prm.patient_1) # ввод данных
        self.find_element(locators_doctors_diary.LOCATOR_SEARCH_2).click() # кнопка "Найти"
        self.find_element_pb() # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_CHOICE_PATIENT).click() # выбор тестового пациента 11/003414
        self.find_element_pb() # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_SERVICES).click() # выпадающее окно услуг
        self.find_element(locators_doctors_diary.LOCATOR_SERVICE).click() # выбор услуги
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_REGISTER_2).click() #кнопка "Записать"
        self.find_element_pb()  # прогрессбар
        self.find_element_pb() # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_CLOSE_1).click() # закрыть окно
        self.find_element_pb()  # прогрессбар
        print('✅ Пациент записан на услугу') # вывод

    def diary_provide_service(self):
        self.find_element(locators_doctors_diary.LOCATOR_PROVIDE_SERVICE).click() # оказать услугу
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_NEW_CREATE).click() # создать новый случай заболевания
        self.find_element_pb()  # прогрессбар
        self.find_element_pb()  # прогрессбар
        self.find_element_pb()  # прогрессбар
        # time.sleep(5)  # ожидание
        self.find_element(locators_doctors_diary.LOCATOR_BASIC_1).click() # указать цель посещения - по заболеванию
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_BASIC_1_2_3).click()  # кнопка "Ок"
        self.find_element(locators_doctors_diary.LOCATOR_BASIC_2_1).click()  # указать исход обращения
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_BASIC_2_2).click()  # без перемен
        self.find_element(locators_doctors_diary.LOCATOR_BASIC_1_2_3).click()  # кнопка "Ок"
        self.find_element(locators_doctors_diary.LOCATOR_BASIC_3_1).click()  # результат обращения
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_BASIC_3_2).click()  # напрвлен на обследования
        self.find_element(locators_doctors_diary.LOCATOR_BASIC_1_2_3).click()  # кнопка "Ок"
        self.find_element(locators_doctors_diary.LOCATOR_DIAGNOSIS).click() # выбор вкладки "Диагноз"
        self.find_element(locators_doctors_diary.LOCATOR_MKB).click() # окно заболеваний
        self.find_element_pb()  # прогрессбар
        search_string_2 = self.find_element(locators_doctors_diary.LOCATOR_MKB_SEARCH_1) # поиск заболевания "J10.0"
        search_string_2.send_keys(prm.disease)  # ввод данных
        self.find_element(locators_doctors_diary.LOCATOR_MKB_SEARCH_2).click() # кнопка "Поиск"
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_MKB_CHOICE).click() # выбор заболевания "J10.0"
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_MKB_DISEASE_1).click() # характер заболевания
        self.find_element(locators_doctors_diary.LOCATOR_MKB_DISEASE_2).click() # острое
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_SAVE_SERVICE).click() # сохранение визита с характером заболевания "Z00.0"
        self.find_element_pb()  # прогрессбар
        print('✅ Услуга оказана') # вывод

    def diary_delite(self):
        self.actionchains(locators_doctors_diary.LOCATOR_PATIENT_RCM).perform() # ПКМ по имени тестового пациента
        self.find_clickable_elements(locators_doctors_diary.LOCATOR_CANCEL_SERVICE).click() # отмена оказания услуги
        self.find_element_pb()  # прогрессбар
        print('✅ Услуга отменена') # вывод
        self.find_clickable_elements(locators_doctors_diary.LOCATOR_MARKER).click()  # клик по пустому слоту
        self.actionchains(locators_doctors_diary.LOCATOR_PATIENT_RCM).perform() # ПКМ по имени тестового пациента
        self.find_clickable_elements(locators_doctors_diary.LOCATOR_DELETE_PATIENT).click() # удаление тестовго пациента
        self.driver.switch_to.alert.accept() # принятие всплывающего окна
        self.find_element_pb()  # прогрессбар
        print('✅ Запись удалена') # вывод
        time.sleep(3) # ожидание


