from selenium.common import UnexpectedAlertPresentException, ElementClickInterceptedException
import RO.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By

class locators_doctors_diary:
    LOCATOR_DIARY_1 = (By.XPATH, '//span[contains(text(), "Рабочие места")]')
    LOCATOR_DIARY_2 = (By.XPATH, '//body[1]//div[5]//tr[1]//span[contains(text(), "Дневник")]')
    LOCATOR_REGISTER_1 = (By.XPATH, '//body[1]//table[5]//td[2]')
    LOCATOR_SEARCH_1 = (By.XPATH, '//div[@name="search_patient_form"]//table[@name="fullSearchRegimContainer"]//td[5]//input[@type="text"]')
    LOCATOR_SEARCH_2 = (By.XPATH, '//td[contains(text(),"Найти")]')
    LOCATOR_CHOICE_PATIENT = (By.XPATH, f'//body[1]//tr[1]//tr[1]//a[contains(text(), "{prm.name_patient}")]')
    LOCATOR_SERVICES = (By.XPATH, '//div[@name="makeReg"]//tr[@name="TR_SERVICES"]//input')
    LOCATOR_SERVICE = (By.XPATH, '//div[@name="ComboItemsList_SERVICES"]//tr[@se_code_attr="B01.047.001"]')
    LOCATOR_REGISTER_2 = (By.XPATH, '//td[3][contains(text(), "Записать")]')
    LOCATOR_CLOSE_1 = (By.XPATH, '//body[1]/div[8]//div[5]')
    LOCATOR_PROVIDE_SERVICE = (By.XPATH, '//a[contains(text(), "Оказать")]')
    LOCATOR_STATISTICAL_DESIGN = (By.XPATH, '//div[contains(text(), "Статистическое")]')
    LOCATOR_FULLSCREEN_WINDOW = (By.XPATH, '//tbody/tr[2]/td[2]//div[4]')
    LOCATOR_RESULT_APPEAL_1 = (By.XPATH, '//body[1]/div[7]//div[3]//tr[6]//img[1]')
    LOCATOR_RESULT_APPEAL_2 = (By.XPATH, '//span[contains(text(), "Случай незакончен")]')
    LOCATOR_RESULT_APPEAL_3 = (By.XPATH, '//body[1]/div[7]//tr[9]/td[4]//img[1]')
    LOCATOR_RESULT_APPEAL_4 = (By.XPATH, '//span[contains(text(), "304 - Лечение продолжено")]')
    LOCATOR_RESULT_APPEAL_5 = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_NUMBER_PP = (By.XPATH, '//body[1]/div[7]//tr[12]//table[2]//img[1]')
    LOCATOR_DIAGNOSIS = (By.XPATH, '// div[contains(text(), "Диагноз")]')
    LOCATOR_MKB = (By.XPATH, '//body[1]/div[7]//tr[2]//tr[2]//tr[2]//tr[3]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]//img[1]')
    LOCATOR_MKB_SEARCH_1 = (By.XPATH, '//body[1]/div[8]//tr[2]/td[1]//input[1]')
    LOCATOR_MKB_SEARCH_2 = (By.XPATH, '//td[contains(text(), "Поиск")]')
    LOCATOR_MKB_CHOICE = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_MKB_TYPE_1 = (By.XPATH, '//body[1]/div[7]//tr[2]//tr[2]//tr[2]//tr[3]//td[4]//img[1]')
    LOCATOR_MKB_TYPE_2 = (By.XPATH, '//body[1]/div[8]//span[contains(text(), "Заключительный")]')
    LOCATOR_SAVE_SERVICE = (By.XPATH, '//body[1]/div[7]//table[2]//td[2][contains(text(), "Сохранить")]')
    LOCATOR_PATIENT_RCM = (By.XPATH, f'//body[1]//a[contains(text(), "{prm.name_patient}")]')
    LOCATOR_CANCEL_SERVICE = (By.XPATH, '//td[contains(text(), "Отменить оказание")]')
    LOCATOR_DELETE_PATIENT = (By.XPATH, '//body[1]//div[23]//td[contains(text(), "Удалить направление")]')

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
        search_string_1 = self.find_element(locators_doctors_diary.LOCATOR_SEARCH_1) # поиск тестового пациента 1600046061
        search_string_1.send_keys(prm.patient) # ввод данных
        self.find_element(locators_doctors_diary.LOCATOR_SEARCH_2).click() # кнопка "Найти"
        self.find_element_pb() # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_CHOICE_PATIENT).click() # выбор тестового пациента 1600046061
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
        self.find_element_pb()  # прогрессбар
        time.sleep(3)  # ожидание
        self.find_element(locators_doctors_diary.LOCATOR_STATISTICAL_DESIGN).click() # выбор вкладки "Статический оформление обращения (посещения)"
        self.find_element(locators_doctors_diary.LOCATOR_FULLSCREEN_WINDOW).click() # открыть окно в полный экран
        self.find_element(locators_doctors_diary.LOCATOR_RESULT_APPEAL_1).click()  # выбор "Результат визита"
        self.find_element(locators_doctors_diary.LOCATOR_RESULT_APPEAL_2).click()  # выбор визита "Случай незакончен"
        self.find_element(locators_doctors_diary.LOCATOR_RESULT_APPEAL_3).click() # выбор "Результат обращения"
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_RESULT_APPEAL_4).click() # выбор обращения "304"
        self.find_element(locators_doctors_diary.LOCATOR_RESULT_APPEAL_5).click()  # кнопка "Ок"
        self.find_element(locators_doctors_diary.LOCATOR_NUMBER_PP).click() # номер п/п
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_DIAGNOSIS).click() # вкладка "Диагноз"
        self.find_element(locators_doctors_diary.LOCATOR_MKB).click() # окно заболеваний
        search_string_2 = self.find_element(locators_doctors_diary.LOCATOR_MKB_SEARCH_1) # поиск заболевания "J00.0"
        search_string_2.send_keys(prm.disease)  # ввод данных
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_MKB_SEARCH_2).click() # кнопка "Поиск"
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_MKB_CHOICE).click() # выбор заболевания "J00.0"
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_doctors_diary.LOCATOR_MKB_TYPE_1).click() # тип заболевания
        self.find_element(locators_doctors_diary.LOCATOR_MKB_TYPE_2).click() # выбрать заключительный
        self.find_element(locators_doctors_diary.LOCATOR_SAVE_SERVICE).click() # сохранение визита с характером заболевания "J00.0"
        self.driver.switch_to.alert.accept()  # принятие всплывающего окна
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