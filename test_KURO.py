from KURO.page_object.login_page import login
from KURO.page_object.doctors_diary_page import doctors_diary
from KURO.page_object.schedule_page import schedule
# from KURO.page_object.hospitalization_page import hospitalization
# from KURO.page_object.search_patient_page import search_patient
# from conftest import browser_SNILS, browser_KURO
import time

class Test_KURO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    # def test_KURO_full(self, browser_KURO):
    #     start = time.time()  # начало отсчета
    #     start_page = login(browser_KURO)  # тест модуля авторизации
    #     start_page.auth()
    #     start_doctors_diary = time.time()
    #     doctors_diary_test = doctors_diary(browser_KURO)  # тест модуля "Дневник врача"
    #     doctors_diary_test.diary()
    #     doctors_diary_test.diary_provide_service()
    #     doctors_diary_test.diary_delite()
    #     end_doctors_diary = time.time()
    #     full_doctors_diary = end_doctors_diary - start_doctors_diary
    #     print(' ▶️ Модуль - "Дневник врача", выполнен за: ', round(full_doctors_diary, 2), 'с')  # вывод полного времени тестирования
    #     start_patient_schedule = time.time()
    #     patient_schedule_test = schedule(browser_KURO)  # тест модуля "Расписание"
    #     patient_schedule_test.patient_schedule()
    #     patient_schedule_test.patient_schedule_delete()
    #     end_patient_schedule = time.time()
    #     full_patient_schedule = end_patient_schedule - start_patient_schedule
    #     print(' ▶️ Модуль - "Расписание", выполнен за: ', round(full_patient_schedule, 2), 'с')  # вывод полного времени тестирования
    #     start_patient_hospitalization = time.time()
    #     patient_hospitalization_test = hospitalization(browser_KURO)  # тест модуля "Госпитализации"
    #     patient_hospitalization_test.register_patient()
    #     patient_hospitalization_test.patient_hospitalization()
    #     patient_hospitalization_test.patient_cancel_hospitalization()
    #     patient_hospitalization_test.patient_delete_hospitalization()
    #     end_patient_hospitalization = time.time()
    #     full_patient_hospitalization = end_patient_hospitalization - start_patient_hospitalization
    #     print(' ▶️ Модуль - "Госпитализация", выполнен за: ', round(full_patient_hospitalization, 2), 'с')  # вывод полного времени тестирования
    #     start_search_patient = time.time()
    #     search_patient_test = search_patient(browser_KURO)  # тест модуля "Поиск пациентов"
    #     search_patient_test.create_patient()
    #     search_patient_test.delete_patient()
    #     end_search_patient = time.time()
    #     full_search_patient = end_search_patient - start_search_patient
    #     print(' ▶️ Модуль - "Поиск пациентов", выполнен за: ', round(full_search_patient, 2), 'с')  # вывод полного времени тестирования
    #     end = time.time()  # конец отсчета
    #     full_test = end - start  # полное время авторизации
    #     print(' ▶️ Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования

    """Тест по модулям"""

    def test_KURO(self, browser_KURO):
        self.test_KURO_login(browser_KURO)  # тест "Авторизации"
        self.test_KURO_doctors_diary(browser_KURO)  # тест "Дневник врача"
        self.test_KURO_schedule(browser_KURO)  # тест "Расписание"
        self.test_KURO_hospitalization(browser_KURO)  # тест "Госпитализация"
        self.test_KURO_search_patient(browser_KURO)  # тест "Поиск пациентов"

    def test_KURO_login(self, browser_KURO):
        start_page = login(browser_KURO)  # тест модуля авторизации
        start_page.auth()
        print('STAGE_1: COMPLETE')

    def test_KURO_doctors_diary(self, browser_KURO):
        self.test_KURO_login(browser_KURO)  # тест авторизации
        doctors_diary_test = doctors_diary(browser_KURO)
        doctors_diary_test.diary()
        doctors_diary_test.diary_provide_service()
        doctors_diary_test.diary_delite()
        print('STAGE_2: COMPLETE')

    def test_KURO_schedule(self, browser_KURO):
        self.test_KURO_login(browser_KURO)  # тест авторизации
        patient_schedule_test = schedule(browser_KURO)
        patient_schedule_test.patient_schedule()
        patient_schedule_test.patient_schedule_delete()
        print('STAGE_3: COMPLETE')

    def test_KURO_hospitalization(self, browser_KURO):
        self.test_KURO_login(browser_KURO)  # тест авторизации
        patient_hospitalization_test = hospitalization(browser_KURO)
        patient_hospitalization_test.register_patient()
        patient_hospitalization_test.patient_hospitalization()
        patient_hospitalization_test.patient_cancel_hospitalization()
        patient_hospitalization_test.patient_delete_hospitalization()
        print('STAGE_4: COMPLETE')

    def test_KURO_search_patient(self, browser_KURO):
        self.test_KURO_login(browser_KURO)  # тест авторизации
        search_patient_test = search_patient(browser_KURO)
        search_patient_test.create_patient()
        search_patient_test.delete_patient()
        print('STAGE_5: COMPLETE')