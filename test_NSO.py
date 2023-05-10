from NSO.page_object.login_page import login
from NSO.page_object.doctors_diary_page import doctors_diary
from NSO.page_object.schedule_page import schedule
from NSO.page_object.hospitalization_page import hospitalization
from NSO.page_object.search_patient_page import search_patient
from conftest import browser_SNILS, browser_PK
import time

class Test_NSO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    def test_NSO_full(self, browser_NSO):
        start = time.time()  # начало отсчета
        start_page = login(browser_NSO)  # тест модуля авторизации
        start_page.auth()
        start_doctors_diary = time.time()
        doctors_diary_test = doctors_diary(browser_NSO) # тест модуля "Дневник врача"
        doctors_diary_test.diary()
        doctors_diary_test.diary_provide_service()
        doctors_diary_test.diary_delite()
        end_doctors_diary = time.time()
        full_doctors_diary = end_doctors_diary - start_doctors_diary
        print(' ▶️ Модуль - "Дневник врача", выполнен за: ', round(full_doctors_diary, 2), 'с')  # вывод полного времени тестирования
        start_patient_schedule = time.time()
        patient_schedule_test = schedule(browser_NSO) # тест модуля "Расписание"
        patient_schedule_test.patient_schedule()
        patient_schedule_test.patient_schedule_delete()
        end_patient_schedule = time.time()
        full_patient_schedule = end_patient_schedule - start_patient_schedule
        print(' ▶️ Модуль - "Расписание", выполнен за: ', round(full_patient_schedule, 2), 'с')  # вывод полного времени тестирования
        start_patient_hospitalization = time.time()
        patient_hospitalization_test = hospitalization(browser_NSO) # тест модуля "Госпитализации"
        patient_hospitalization_test.register_patient()
        patient_hospitalization_test.patient_hospitalization()
        patient_hospitalization_test.patient_cancel_hospitalization()
        patient_hospitalization_test.patient_delete_hospitalization()
        end_patient_hospitalization = time.time()
        full_patient_hospitalization = end_patient_hospitalization - start_patient_hospitalization
        print(' ▶️ Модуль - "Госпитализация", выполнен за: ', round(full_patient_hospitalization, 2), 'с')  # вывод полного времени тестирования
        start_search_patient = time.time()
        search_patient_test = search_patient(browser_NSO) # тест модуля "Поиск пациентов"
        search_patient_test.create_patient()
        search_patient_test.delete_patient()
        end_search_patient = time.time()
        full_search_patient = end_search_patient - start_search_patient
        print(' ▶️ Модуль - "Поиск пациентов", выполнен за: ', round(full_search_patient, 2), 'с')  # вывод полного времени тестирования
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        print(' ▶️ Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования

    """Тест по модулям"""
    def test_NSO(self, browser_NSO):
        self.test_NSO_login(browser_NSO)  # тест "Авторизации"
        self.test_NSO_doctors_diary(browser_NSO) # тест "Дневник врача"
        self.test_NSO_schedule(browser_NSO) # тест "Расписание"
        self.test_NSO_hospitalization(browser_NSO) # тест "Госпитализация"
        self.test_NSO_search_patient(browser_NSO) # тест "Поиск пациентов"

    def test_NSO_login(self, browser_NSO):
        start_page = login(browser_NSO)  # тест модуля авторизации
        start_page.auth()
        print('STAGE_1: COMPLETE')

    def test_NSO_doctors_diary(self, browser_NSO):
        self.test_NSO_login(browser_NSO) # тест авторизации
        doctors_diary_test = doctors_diary(browser_NSO)
        doctors_diary_test.diary()
        doctors_diary_test.diary_provide_service()
        doctors_diary_test.diary_delite()
        print('STAGE_2: COMPLETE')

    def test_NSO_schedule(self, browser_NSO):
        self.test_NSO_login(browser_NSO) # тест авторизации
        patient_schedule_test = schedule(browser_NSO)
        patient_schedule_test.patient_schedule()
        patient_schedule_test.patient_schedule_delete()
        print('STAGE_3: COMPLETE')

    def test_NSO_hospitalization(self, browser_NSO):
        self.test_NSO_login(browser_NSO) # тест авторизации
        patient_hospitalization_test = hospitalization(browser_NSO)
        patient_hospitalization_test.register_patient()
        patient_hospitalization_test.patient_hospitalization()
        patient_hospitalization_test.patient_cancel_hospitalization()
        patient_hospitalization_test.patient_delete_hospitalization()
        print('STAGE_4: COMPLETE')

    def test_NSO_search_patient(self, browser_NSO):
        self.test_NSO_login(browser_NSO) # тест авторизации
        search_patient_test = search_patient(browser_NSO)
        search_patient_test.create_patient()
        search_patient_test.delete_patient()
        print('STAGE_5: COMPLETE')

