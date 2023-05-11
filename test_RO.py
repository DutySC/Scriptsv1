from RO.page_object.login_page import login
from RO.page_object.doctors_diary_page import doctors_diary
from RO.page_object.schedule_page import schedule
from RO.page_object.hospitalization_page import hospitalization
# from RO.page_object.search_patient_page import search_patient
# from conftest import browser_SNILS, browser_RO
import time

class Test_RO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    def test_RO_full(self, browser_RO):
        start = time.time()  # начало отсчета
        start_page = login(browser_RO) # тест модуля авторизации
        start_page.auth()
        start_doctors_diary = time.time()
        doctors_diary_test = doctors_diary(browser_RO) # тест модуля "Дневник врача"
        doctors_diary_test.diary()
        doctors_diary_test.diary_provide_service()
        doctors_diary_test.diary_delite()
        end_doctors_diary = time.time()
        full_doctors_diary = end_doctors_diary - start_doctors_diary
        print(' ▶️ Модуль - "Дневник врача", выполнен за: ', round(full_doctors_diary, 2), 'с') # вывод полного времени тестирования
        start_patient_schedule = time.time()
        patient_schedule_test = schedule(browser_RO) # тест модуля "Расписание"
        patient_schedule_test.patient_schedule()
        patient_schedule_test.patient_schedule_delete()
        end_patient_schedule = time.time()
        full_patient_schedule = end_patient_schedule - start_patient_schedule
        print(' ▶️ Модуль - "Расписание", выполнен за: ', round(full_patient_schedule, 2), 'с') # вывод полного времени тестирования
        start_patient_hospitalization = time.time()
        patient_hospitalization_test = hospitalization(browser_RO) # тест модуля "Госпитализация"
        patient_hospitalization_test.register_patient()
        patient_hospitalization_test.patient_hospitalization()
        patient_hospitalization_test.patient_cancel_hospitalization()
        patient_hospitalization_test.patient_delete_hospitalization()
        end_patient_hospitalization = time.time()
        full_patient_hospitalization = end_patient_hospitalization - start_patient_hospitalization
        print(' ▶️ Модуль - "Госпитализация", выполнен за: ', round(full_patient_hospitalization, 2), 'с') # вывод полного времени тестирования
        start_search_patient = time.time()
        search_patient_test = search_patient(browser_RO) # тест модуля "Поиск пациента"
        search_patient_test.create_patient()
        search_patient_test.delete_patient()
        end_search_patient = time.time()
        full_search_patient = end_search_patient - start_search_patient
        print(' ▶️ Модуль - "Поиск пациентов", выполнен за: ', round(full_search_patient, 2), 'с') # вывод полного времени тестирования
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        print(' ▶️ Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования

    """Тест по модулям"""
    def test_RO(self, browser_RO):
        self.test_RO_login(browser_RO)  # тест модуля авторизации
        self.test_RO_doctors_diary(browser_RO) # тест модуля "Дневник врача"
        self.test_RO_schedule(browser_RO) # тест модуля "Расписание"
        self.test_RO_hospitalization(browser_RO) # тест модуля "Госпитализация"
        self.test_RO_search_patient(browser_RO) # тест модуля "Поиск пациентов"

    def test_RO_login(self, browser_RO):
        start_page = login(browser_RO)
        start_page.auth()
        print('STAGE_1: COMPLETE')

    def test_RO_doctors_diary(self, browser_RO):
        self.test_RO_login(browser_RO) # тест авторизации
        doctors_diary_test = doctors_diary(browser_RO)
        doctors_diary_test.diary()
        doctors_diary_test.diary_provide_service()
        doctors_diary_test.diary_delite()
        print('STAGE_2: COMPLETE')

    def test_RO_schedule(self, browser_RO):
        self.test_RO_login(browser_RO) # тест авторизации
        patient_schedule_test = schedule(browser_RO)
        patient_schedule_test.patient_schedule()
        patient_schedule_test.patient_schedule_delete()
        print('STAGE_3: COMPLETE')

    def test_RO_hospitalization(self, browser_RO):
        self.test_RO_login(browser_RO) # тест авторизации
        patient_hospitalization_test = hospitalization(browser_RO)
        patient_hospitalization_test.register_patient()
        patient_hospitalization_test.patient_hospitalization()
        patient_hospitalization_test.patient_cancel_hospitalization()
        patient_hospitalization_test.patient_delete_hospitalization()
        print('STAGE_4: COMPLETE')
    #
    # def test_RO_search_patient(self, browser_RO):
    #     self.test_RO_login(browser_RO)  # тест авторизации
    #     search_patient_test = search_patient(browser_RO)
    #     search_patient_test.create_patient()
    #     search_patient_test.delete_patient()
    #     print('STAGE_5: COMPLETE')
