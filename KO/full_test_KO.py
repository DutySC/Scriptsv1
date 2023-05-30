import testit
from KO.page_object.login_page import login
from KO.page_object.doctors_diary_page import doctors_diary
from KO.page_object.schedule_page import schedule
from KO.page_object.hospitalization_page import hospitalization
from KO.page_object.search_patient_page import search_patient
# import time


@testit.step('Модуль: Авторизация', 'Проверка авторизации на продуктивном стенде')
def test_KO_login(browser_KO):
    start_page = login(browser_KO)
    start_page.auth()


@testit.step('Модуль: Дневник врача', 'Запись пациента, оказание услуги и ее отмена')
def test_KO_doctors_diary(browser_KO):
    # test_KO_login(browser_KO)  # тест авторизации
    doctors_diary_test = doctors_diary(browser_KO)
    doctors_diary_test.diary()


@testit.step('Модуль: Расписание', 'Проверка записи пациента к врачу')
def test_KO_schedule(browser_KO):
    # test_KO_login(browser_KO)  # тест авторизации
    patient_schedule_test = schedule(browser_KO)
    patient_schedule_test.patient_schedule()


@testit.step('Модуль: Госпитализация', 'Госпитализация пользователя')
def test_KO_hospitalization(browser_KO):
    # test_KO_login(browser_KO)  # тест авторизации
    patient_hospitalization_test = hospitalization(browser_KO)
    patient_hospitalization_test.register_patient()


@testit.step('Модуль: Поиск пациента', 'Создание и удаление тестового пациента')
def test_KO_search_patient(browser_KO):
    # test_KO_login(browser_KO)  # тест авторизации
    search_patient_test = search_patient(browser_KO)
    search_patient_test.create_patient()

# def test_KO_full(self, browser_KO):
#     start = time.time()  # начало отсчета
#     start_page = login(browser_KO)  # тест модуля авторизации
#     start_page.auth()
#     start_doctors_diary = time.time()
#     doctors_diary_test = doctors_diary(browser_KO)  # тест модуля "Дневник врача"
#     doctors_diary_test.diary()
#     doctors_diary_test.diary_provide_service()
#     doctors_diary_test.diary_delite()
#     end_doctors_diary = time.time()
#     full_doctors_diary = end_doctors_diary - start_doctors_diary
#     print(' ▶️ Модуль - "Дневник врача", выполнен за: ', round(full_doctors_diary, 2),
#           'с')  # вывод полного времени тестирования
#     start_patient_schedule = time.time()
#     patient_schedule_test = schedule(browser_KO)  # тест модуля "Расписание"
#     patient_schedule_test.patient_schedule()
#     patient_schedule_test.patient_schedule_delete()
#     end_patient_schedule = time.time()
#     full_patient_schedule = end_patient_schedule - start_patient_schedule
#     print(' ▶️ Модуль - "Расписание", выполнен за: ', round(full_patient_schedule, 2),
#           'с')  # вывод полного времени тестирования
#     start_patient_hospitalization = time.time()
#     patient_hospitalization_test = hospitalization(browser_KO)  # тест модуля "Госпитализация"
#     patient_hospitalization_test.register_patient()
#     patient_hospitalization_test.patient_hospitalization()
#     patient_hospitalization_test.patient_cancel_hospitalization()
#     patient_hospitalization_test.patient_delete_hospitalization()
#     end_patient_hospitalization = time.time()
#     full_patient_hospitalization = end_patient_hospitalization - start_patient_hospitalization
#     print(' ▶️ Модуль - "Госпитализация", выполнен за: ', round(full_patient_hospitalization, 2),
#           'с')  # вывод полного времени тестирования
#     start_search_patient = time.time()
#     search_patient_test = search_patient(browser_KO)  # тест модуля "Поиск пациента"
#     search_patient_test.create_patient()
#     search_patient_test.delete_patient()
#     end_search_patient = time.time()
#     full_search_patient = end_search_patient - start_search_patient
#     print(' ▶️ Модуль - "Поиск пациентов", выполнен за: ', round(full_search_patient, 2),
#           'с')  # вывод полного времени тестирования
#     end = time.time()  # конец отсчета
#     full_test = end - start  # полное время авторизации
#     print(' ▶️ Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования