from selenium.common import UnexpectedAlertPresentException, ElementClickInterceptedException
import TO.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By

class locators_doctors_diary:
    LOCATOR_READ_ALL = (By.XPATH, '//a[contains(text(), "Прочитать все")]')
    LOCATOR_DIARY_1 = (By.XPATH, '//span[contains(text(), "Рабочие места")]')
    LOCATOR_DIARY_2 = (By.XPATH, '//body[1]//div[5]//tr[1]//span[contains(text(), "Дневник")]')
    LOCATOR_REGISTER_1 = (By.XPATH, '//body[1]//table[5]//td[2]')
    LOCATOR_SEARCH_1 = (By.XPATH, '//div[@name="search_patient_form"]//table[@name="fullSearchRegimContainer"]//td[5]//input[@type="text"]')
    LOCATOR_SEARCH_2 = (By.XPATH, '//td[contains(text(),"Найти")]')
    LOCATOR_CHOICE_PATIENT = (By.XPATH, f'//body[1]//tr[1]//tr[1]//a[contains(text(), "{prm.name_patient}")]')
    LOCATOR_SERVICES = (By.XPATH, '//div[@name="makeReg"]//tr[@name="TR_SERVICES"]//input')
    LOCATOR_SERVICE = (By.XPATH, '//span[contains(text(), "B01.047.001 Прием (осмотр, консультация) врача-тер")]')
    LOCATOR_REGISTER_2 = (By.XPATH, '//td[3][contains(text(), "Записать")]')
    LOCATOR_CLOSE_1 = (By.XPATH, '//body[1]/div[8]//div[5]')
    LOCATOR_PROVIDE_SERVICE = (By.XPATH, '//a[contains(text(), "Оказать")]')
    LOCATOR_DIAGNOSIS = (By.XPATH, '//div[contains(text(), "Диагноз")]')
    LOCATOR_MKB_CHOICE = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_MKB_1 = (By.XPATH, '//tr[3]//tr[3]//tr[3]//tr[1]/td[3]//img[1]')
    LOCATOR_MKB_2 = (By.XPATH, '//div[8]//span[contains(text(), "Острое")]')
    LOCATOR_DEFAULT = (By.XPATH, '//div[contains(text(), "Объективный")]')
    LOCATOR_STATUS_1 = (By.XPATH, '//div[7]//div[3]//tr[5]//img[1]')
    LOCATOR_STATUS_2 = (By.XPATH, '// span[contains(text(), "Удовлетворительное")]')
    LOCATOR_SAVE_SERVICE = (By.XPATH, '//body[1]/div[7]//table[2]//td[2][contains(text(), "Сохранить")]')
    LOCATOR_PATIENT_RCM = (By.XPATH, f'//body[1]//a[contains(text(), "{prm.name_patient}")]')
    LOCATOR_CANCEL_SERVICE = (By.XPATH, '//td[contains(text(), "Отменить оказание")]')
    LOCATOR_DELETE_PATIENT = (By.XPATH, '//tr[22]/td[contains(text(), "Удалить направление")]')

class doctors_diary(BasePage):
    def diary(self):
        try:
            start_doctors_diary = time.time()
            try:
                self.find_element(locators_doctors_diary.LOCATOR_READ_ALL, time=5).click() # прочесть все системные сообщения
                self.find_element_pb(time=5)  # прогрессбар
            except Exception:
                pass
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
                print('⚠️ Формирования окна - Дневник врача: ', round(full_diary, 2), 'сек', '(> 10 с)')
            try:
                self.find_element(locators_doctors_diary.LOCATOR_REGISTER_1).click() #кнопка "Запись"
            except ElementClickInterceptedException:
                self.find_element(locators_doctors_diary.LOCATOR_REGISTER_1).click()  # кнопка "Запись"
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            time.sleep(5) # ожидание
            search_string_1 = self.find_element(locators_doctors_diary.LOCATOR_SEARCH_1) # поиск тестового пациента 11/003414
            search_string_1.send_keys(prm.patient) # ввод данных
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
            ###########след.этап########################################################################################
            self.find_element(locators_doctors_diary.LOCATOR_PROVIDE_SERVICE).click() # оказать услугу
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            time.sleep(2)  # ожидание
            self.find_element(locators_doctors_diary.LOCATOR_DIAGNOSIS).click() # выбор вкладки "Диагноз"
            self.find_element(locators_doctors_diary.LOCATOR_MKB_1).click()
            self.find_element(locators_doctors_diary.LOCATOR_MKB_2).click()
            self.find_element(locators_doctors_diary.LOCATOR_MKB_CHOICE).click() # кнопка ОК
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_doctors_diary.LOCATOR_DEFAULT).click()
            self.find_element(locators_doctors_diary.LOCATOR_STATUS_1).click()
            self.find_element(locators_doctors_diary.LOCATOR_STATUS_2).click()
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_doctors_diary.LOCATOR_SAVE_SERVICE).click() # сохранение визита с характером заболевания "Z00.0"
            self.find_element_pb()  # прогрессбар
            print('✅ Услуга оказана') # вывод
            ###########след.этап########################################################################################
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
            end_doctors_diary = time.time()
            full_doctors_diary = end_doctors_diary - start_doctors_diary
            print('   🔼 Модуль - "Дневник врача", выполнен за: ', round(full_doctors_diary, 2), 'с')
        except Exception as error:
            self.get_screenshots('Results/Results_sc/Дневник.png')
            print('❗️ Ошибка:', error)
            self.driver.quit()