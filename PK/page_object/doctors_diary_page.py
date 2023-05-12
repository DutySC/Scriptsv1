from selenium.common import UnexpectedAlertPresentException, ElementClickInterceptedException
import PK.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By

class locators_doctors_diary:
    LOCATOR_DIARY_1 = (By.XPATH, '//span[contains(text(), "Рабочие места")]')
    LOCATOR_DIARY_2 = (By.XPATH, '//span[contains(text(), "Дневник")]')
    LOCATOR_REGISTER_1 = (By.XPATH, '//body[1]//table[5]//td[2]')
    LOCATOR_SEARCH_1 = (By.XPATH, '//div[@name="search_patient_form"]//table[@name="fullSearchRegimContainer"]//td[5]//input[@type="text"]')
    LOCATOR_SEARCH_2 = (By.XPATH, '//td[contains(text(),"Найти")]')
    LOCATOR_CHOICE_PATIENT = (By.XPATH, f'//tr[1]//tr[1]//a[contains(text(), "{prm.name_patient}")]')
    LOCATOR_SERVICES = (By.XPATH, '//div[@name="makeReg"]//tr[@name="TR_SERVICES"]//input')
    LOCATOR_SERVICE = (By.XPATH, '//div[@name="ComboItemsList_SERVICES"]//tr[@se_code_attr="B01.047.001"]')
    LOCATOR_REGISTER_2 = (By.XPATH, '//td[3][contains(text(), "Записать")]')
    LOCATOR_CLOSE_1 = (By.XPATH, '//body[1]/div[8]//div[5]')
    LOCATOR_PROVIDE_SERVICE = (By.XPATH, '//a[contains(text(), "Оказать")]')
    LOCATOR_NEW_CREATE = (By.XPATH, '//div[contains(text(), "Создать новый")]')
    LOCATOR_OBJECTIVE_STATUS = (By.XPATH, '//div[contains(text(), "Объективный")]')
    LOCATOR_PATIENT_CONDITION = (By.XPATH, '//body[1]/div[7]//div[2]//div[2]//tr[3]//img[1]')
    LOCATOR_PATIENT_CONDITION_CHOICE = (By.XPATH, '//body[1]/div[8]//tr[2]//span[contains(text(), "Удовлетворительное")]')
    LOCATOR_DIAGNOSIS = (By.XPATH, '//div[contains(text(), "Диагноз")]')
    LOCATOR_MKB = (By.XPATH, '//body[1]//tr[3]//tr[3]//tr[3]//tr[1]/td[1]//img[1]')
    LOCATOR_MKB_SEARCH_1 = (By.XPATH, '//body[1]/div[8]//tr[2]/td[1]//input[1]')
    LOCATOR_MKB_SEARCH_2 = (By.XPATH, '//td[contains(text(), "Поиск")]')
    LOCATOR_MKB_CHOICE = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_BASIC_DATA = (By.XPATH, '//div[contains(text(),"Основные")]')
    LOCATOR_RESULT_OF_TREATMENT = (By.XPATH, '//body[1]/div[7]//tr[6]/td[1]/table[1]//img[1]')
    LOCATOR_RESULT_OF_TREATMENT_CHOICE = (By.XPATH, '//span[contains(text(), "304 - Лечение продолжено")]')
    LOCATOR_DISEASE_OUTCOME = (By.XPATH, '//body[1]/div[7]//tr[9]/td[1]/table[1]//img[1]')
    LOCATOR_DISEASE_OUTCOME_CHOICE = (By.XPATH, '//span[contains(text(), "308 - Лечение продолжено")]')
    LOCATOR_VISIT_PURPOSE = (By.XPATH, '//body[1]/div[7]//tr[6]/td[2]/table[1]//img[1]')
    LOCATOR_VISIT_PURPOSE_CHOICE = (By.XPATH, '//span[contains(text(), "1.0 - 1.0 - Посещение по заболеванию")]')
    LOCATOR_PLACE_OF_RECEPTION = (By.XPATH, '//body[1]/div[7]//tr[9]/td[3]/table[1]//img[1]')
    LOCATOR_PLACE_OF_RECEPTION_CHOICE= (By.XPATH, '//span[contains(text(), "АПУ")]')
    LOCATOR_SAVE_SERVICE = (By.XPATH, '//body[1]//table[2]//td[contains(text(), "Сохранить")]')
    LOCATOR_SAVE_SERVICE_NEXT = (By.XPATH, '//div[contains(text(), "Продолжить")]')
    LOCATOR_OPEN_WINDOW_SAVE_SERVICE_1 = (By.XPATH, '//body[1]/div[8]//tr[7]//img[1]')
    LOCATOR_OPEN_WINDOW_SAVE_SERVICE_2 = (By.XPATH, '//td[contains(text(), "ОК")]')
    LOCATOR_OPEN_WINDOW_SAVE_SERVICE_3 = (By.XPATH, '//body[1]/div[8]//div/table[2]//td[contains(text(), "Сохранить")]')
    LOCATOR_PATIENT_RCM = (By.XPATH, f'//body//a[contains(text(), "{prm.name_patient}")]')
    LOCATOR_CANCEL_SERVICE = (By.XPATH, '//td[contains(text(), "Отменить оказание")]')
    LOCATOR_DELETE_PATIENT = (By.XPATH, '//body[1]//div[12]//td[2][contains(text(), "Удалить направление")]')

class doctors_diary(BasePage):
    def diary(self):
        self.find_element(locators_doctors_diary.LOCATOR_DIARY_1).click() # вкладка "Рабочие места"
        self.find_element(locators_doctors_diary.LOCATOR_DIARY_2).click() # вкладка "Дневник врача"
        start_diary = time.time() # начало отчета времени формирования окна
        self.find_element_pb() # прогрессбар
        self.find_element_pb()  # прогрессбар
        time.sleep(3)  # ожидание
        end_diary = time.time() # конец отчета времени формирования окна
        full_diary = end_diary - start_diary # суммарное время формирования окна "Дневник врача"
        if full_diary <= 10: # условие
            print('✅ Формирования окна - Дневник врача: ', round(full_diary, 2), 'сек')
        else:
            print('⚠️️ Формирования окна - Дневник врача: ', round(full_diary, 2), 'сек', '(норма - менее 10 с)')
        try:
            self.find_element(locators_doctors_diary.LOCATOR_REGISTER_1).click() #кнопка "Запись"
        except ElementClickInterceptedException:
            self.find_element(locators_doctors_diary.LOCATOR_REGISTER_1).click()  # кнопка "Запись"
        self.find_element_pb()  # прогрессбар
        self.find_element_pb()  # прогрессбар
        time.sleep(3) # ожидание
        search_string_1 = self.find_element(locators_doctors_diary.LOCATOR_SEARCH_1) # поиск тестового пациента К002489
        search_string_1.send_keys(prm.patient) # ввод данных
        self.find_element(locators_doctors_diary.LOCATOR_SEARCH_2).click() # кнопка "Найти"
        self.find_element_pb() # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_CHOICE_PATIENT).click() # выбор тестового пациента К002489
        self.find_element_pb() # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_SERVICES).click() # выпадающее окно услуг
        self.find_element(locators_doctors_diary.LOCATOR_SERVICE).click() # выбор услуги
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_REGISTER_2).click() #кнопка "Записать"
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
        time.sleep(5)  # ожидание
        self.find_element(locators_doctors_diary.LOCATOR_OBJECTIVE_STATUS).click() # вкладка "Объективный статус"
        self.find_element(locators_doctors_diary.LOCATOR_PATIENT_CONDITION).click() # выбор степени состояния пациента
        self.find_element(locators_doctors_diary.LOCATOR_PATIENT_CONDITION_CHOICE).click()  # степень состояния пациента
        self.find_element(locators_doctors_diary.LOCATOR_DIAGNOSIS).click() # выбор вкладки "Диагноз"
        self.find_element(locators_doctors_diary.LOCATOR_MKB).click() # окно заболеваний
        search_string_2 = self.find_element(locators_doctors_diary.LOCATOR_MKB_SEARCH_1) # поиск заболевания "K00.0"
        search_string_2.send_keys(prm.disease)  # ввод данных
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_MKB_SEARCH_2).click() # кнопка "Поиск"
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_MKB_CHOICE).click() # выбор заболевания "K00.0"
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_BASIC_DATA).click() # выбор вкладки "Основные данные"
        self.find_element(locators_doctors_diary.LOCATOR_RESULT_OF_TREATMENT).click() # результат обращения
        self.find_element(locators_doctors_diary.LOCATOR_RESULT_OF_TREATMENT_CHOICE).click() # выбор обращения
        self.find_element(locators_doctors_diary.LOCATOR_DISEASE_OUTCOME).click()  # исход заболевания
        self.find_element(locators_doctors_diary.LOCATOR_DISEASE_OUTCOME_CHOICE).click() # выбор заболевания
        self.find_element(locators_doctors_diary.LOCATOR_VISIT_PURPOSE).click()  # цель посещения
        self.find_element(locators_doctors_diary.LOCATOR_VISIT_PURPOSE_CHOICE).click() # выбор посещения
        self.find_element(locators_doctors_diary.LOCATOR_PLACE_OF_RECEPTION).click()  # место оказания приема
        self.find_element(locators_doctors_diary.LOCATOR_PLACE_OF_RECEPTION_CHOICE).click() # выбор приема
        self.find_element(locators_doctors_diary.LOCATOR_SAVE_SERVICE).click() # сохранение приема
        try:
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_doctors_diary.LOCATOR_SAVE_SERVICE_NEXT).click() # сохранение визита с характером заболевания "K00.0"
        except UnexpectedAlertPresentException:
            self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_doctors_diary.LOCATOR_OPEN_WINDOW_SAVE_SERVICE_1).click() # план ДН
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_doctors_diary.LOCATOR_OPEN_WINDOW_SAVE_SERVICE_2).click() # план ДН
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_doctors_diary.LOCATOR_OPEN_WINDOW_SAVE_SERVICE_3).click() # кнопка "Сохранить"
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_doctors_diary.LOCATOR_SAVE_SERVICE_NEXT).click()  # сохранение визита с характером заболевания "K00.0"
        self.find_element_pb()  # прогрессбар
        print('✅ Услуга оказана') # вывод

    def diary_delite(self):
        self.actionchains(locators_doctors_diary.LOCATOR_PATIENT_RCM).perform() # ПКМ по имени тестового пациента
        self.find_clickable_elements(locators_doctors_diary.LOCATOR_CANCEL_SERVICE).click() # отмена оказания услуги
        self.find_element_pb()  # прогрессбар
        print('✅ Услуга отменена') # вывод
        self.actionchains(locators_doctors_diary.LOCATOR_PATIENT_RCM).perform() # ПКМ по имени тестового пациента
        self.find_clickable_elements(locators_doctors_diary.LOCATOR_DELETE_PATIENT).click() # удаление тестовго пациента
        self.driver.switch_to.alert.accept() # принятие всплывающего окна
        self.find_element_pb()  # прогрессбар
        print('✅ Запись удалена') # вывод
        time.sleep(3) # ожидание


