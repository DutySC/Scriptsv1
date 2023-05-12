import NSO.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By

class locators_schedule:
    LOCATOR_SCHEDULE_1 = (By.XPATH, '//span[contains(text(), "Регистратура")]')
    LOCATOR_SCHEDULE_2 = (By.XPATH, '//tbody/tr[2]/td[2]/a[1]/span[1][contains(text(), "Расписание стандартное")]')
    LOCATOR_REG_CONTAINER = (By.XPATH, '//div[@id = "RegContainer"]')
    LOCATOR_FILTER = (By.XPATH, '//tbody/tr[3]//div[2]/div[3]')
    LOCATOR_FILTER_CABINET = (By.XPATH, '//body[1]//tbody[1]/tr[3]//tr[3]/td[1]//input[1]')
    LOCATOR_SEARCH_1 = (By.XPATH, '//body[1]//tr[3]//td[contains(text(), "Найти")]')
    LOCATOR_CHOOSE_SCHEDULE = (By.XPATH, '//tbody//a[1][contains(text(), "Прием (осмотр, консультация)")]')
    LOCATOR_NEXT_PAGE = (By.XPATH, '//body[1]/div[7]//table[2]//img[1]')
    LOCATOR_WRITE_TO_DOCTOR = (By.XPATH, '//tbody//a[contains(text(), "08:00")]')
    LOCATOR_CARD_NUMBER = (By.XPATH, '//body[1]//div[9]//td[5]//input[1]')
    LOCATOR_SEARCH_2 = (By.XPATH, '//body[1]/div[8]//td[3]//td[contains(text(), "Найти")]')
    LOCATOR_PATIENT_ON_WRITE = (By.XPATH, f'//body[1]//tr[1]//tr[1]//a[contains(text(), "{prm.name_patient_2}")]')
    LOCATOR_WRITE = (By.XPATH, '//body[1]/div[8]//table[2]//td[contains(text(), "Записать")]')
    LOCATOR_ESC_1 = (By.XPATH, '//body[1]/div[9]//div[5]')
    LOCATOR_PATIENT = (By.XPATH, f'//a[contains(text(), "{prm.patient}")]')
    LOCATOR_DELETE_WRITE = (By.XPATH, '//span[contains(text(), "Удалить")]')
    LOCATOR_ESC_2 = (By.XPATH, '//tbody/tr[2]/td[2]//div[5]')

class schedule(BasePage):
    def patient_schedule(self):
        self.find_element(locators_schedule.LOCATOR_SCHEDULE_1).click() # вкладка "Регистратура"
        self.find_element(locators_schedule.LOCATOR_SCHEDULE_2).click() # вкладка "Расписание"
        start_open_schedule = time.time() # отчет времени
        self.find_element_pb() # прогрессбар
        self.find_element_pb() # прогрессбар
        self.find_element(locators_schedule.LOCATOR_REG_CONTAINER) # полная прогрузка элементов страницы
        end_open_schedule = time.time() # отчет времени
        full_time_schedule = end_open_schedule - start_open_schedule # затраченное время
        if full_time_schedule <= 15: # условие
            print('✅ Формирование окна - Расписание: ', round(full_time_schedule, 2), 'с') # вывод затраченного времени
        else:
            print('⚠️️ Формирование окна - Расписание: ', round(full_time_schedule, 2), 'с', '(норма - менее 15 с)') # вывод затраченного времени
        self.find_element(locators_schedule.LOCATOR_FILTER).click() # шторка вниз
        search_string_2 = self.find_element(locators_schedule.LOCATOR_FILTER_CABINET) # ввод кабинета
        search_string_2.send_keys(prm.polyclinic) # указать кабинет
        self.find_element(locators_schedule.LOCATOR_SEARCH_1).click() # кнопка "Найти"
        self.find_element_pb() # прогрессбар
        self.find_element(locators_schedule.LOCATOR_CHOOSE_SCHEDULE).click() # выбор врача для тестирования "Прием (осмотр, консультация) врача-терапевта первичный"
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_schedule.LOCATOR_NEXT_PAGE).click() # выбор следующей недели
        self.find_element_pb() # прогрессбар
        self.find_element(locators_schedule.LOCATOR_WRITE_TO_DOCTOR).click() # запись на назнаначенную дату
        self.find_element_pb() # прогрессбар
        self.find_element_pb() # прогрессбар
        search_string_4 = self.find_element(locators_schedule.LOCATOR_CARD_NUMBER) # ввод значения поля "Номер карты"
        search_string_4.send_keys(prm.patient_2) # вввод 11/003437
        time.sleep(3)  # ожидание
        self.find_element(locators_schedule.LOCATOR_SEARCH_2).click() # кнопка "Найти"
        self.find_element_pb() # прогрессбар
        self.find_element(locators_schedule.LOCATOR_PATIENT_ON_WRITE).click() # выбор пациента
        self.find_element_pb() # прогрессбар
        self.find_element(locators_schedule.LOCATOR_WRITE).click() # запись к врачу
        self.find_element_pb() # прогрессбар
        self.find_element(locators_schedule.LOCATOR_ESC_1).click() # закрыть окно
        self.find_element_pb()  # прогрессбар
        print('✅ Пациент записан к врачу') # вывод

    def patient_schedule_delete(self):
        time.sleep(2)  # ожидание
        self.find_element(locators_schedule.LOCATOR_CHOOSE_SCHEDULE).click()  # выбор врача для тестирования "Прием (осмотр, консультация) врача-терапевта первичный"
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_schedule.LOCATOR_NEXT_PAGE).click()  # выбор следующей недели
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_schedule.LOCATOR_PATIENT).click()
        self.find_element(locators_schedule.LOCATOR_DELETE_WRITE).click()
        self.driver.switch_to.alert.accept()  # принятие всплывающего окна
        self.find_element_pb()  # прогрессбар
        self.find_element(locators_schedule.LOCATOR_ESC_2).click() # закрыть окно
        self.find_element_pb()  # прогрессбар
        print('✅ Запись удалена') # вывод