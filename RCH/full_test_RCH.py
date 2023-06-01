import testit
from RCH.page_object.login_page import login
from RCH.page_object.doctors_diary_page import doctors_diary
from RCH.page_object.schedule_page import schedule
from RCH.page_object.hospitalization_page import hospitalization
from RCH.page_object.search_patient_page import search_patient
# import time


@testit.step('Модуль: Авторизация', 'Проверка авторизации на продуктивном стенде')
def test_RCH_login(browser_RCH):
    start_page = login(browser_RCH)
    start_page.auth()


@testit.step('Модуль: Дневник врача', 'Запись пациента, оказание услуги и ее отмена')
def test_RCH_doctors_diary(browser_RCH):
    # test_RCH_login(browser_RCH)  # тест авторизации
    doctors_diary_test = doctors_diary(browser_RCH)
    doctors_diary_test.diary()


@testit.step('Модуль: Расписание', 'Проверка записи пациента к врачу')
def test_RCH_schedule(browser_RCH):
    # test_RCH_login(browser_RCH)  # тест авторизации
    patient_schedule_test = schedule(browser_RCH)
    patient_schedule_test.patient_schedule()


@testit.step('Модуль: Госпитализация', 'Госпитализация пользователя')
def test_RCH_hospitalization(browser_RCH):
    # test_RCH_login(browser_RCH)  # тест авторизации
    patient_hospitalization_test = hospitalization(browser_RCH)
    patient_hospitalization_test.register_patient()


@testit.step('Модуль: Поиск пациента', 'Создание и удаление тестового пациента')
def test_RCH_search_patient(browser_RCH):
    # test_RCH_login(browser_RCH)  # тест авторизации
    search_patient_test = search_patient(browser_RCH)
    search_patient_test.create_patient()

# def test_RCH_full(self, browser_RCH):
#     start = time.time()  # начало отсчета
#     start_page = login(browser_RCH)  # тест модуля авторизации
#     start_page.auth()
#     start_doctors_diary = time.time()
#     doctors_diary_test = doctors_diary(browser_RCH)  # тест модуля "Дневник врача"
#     doctors_diary_test.diary()
#     doctors_diary_test.diary_provide_service()
#     doctors_diary_test.diary_delite()
#     end_doctors_diary = time.time()
#     full_doctors_diary = end_doctors_diary - start_doctors_diary
#     print(' ▶️ Модуль - "Дневник врача", выполнен за: ', round(full_doctors_diary, 2),
#           'с')  # вывод полного времени тестирования
#     start_patient_schedule = time.time()
#     patient_schedule_test = schedule(browser_RCH)  # тест модуля "Расписание"
#     patient_schedule_test.patient_schedule()
#     patient_schedule_test.patient_schedule_delete()
#     end_patient_schedule = time.time()
#     full_patient_schedule = end_patient_schedule - start_patient_schedule
#     print(' ▶️ Модуль - "Расписание", выполнен за: ', round(full_patient_schedule, 2),
#           'с')  # вывод полного времени тестирования
#     start_patient_hospitalization = time.time()
#     patient_hospitalization_test = hospitalization(browser_RCH)  # тест модуля "Госпитализация"
#     patient_hospitalization_test.register_patient()
#     patient_hospitalization_test.patient_hospitalization()
#     patient_hospitalization_test.patient_cancel_hospitalization()
#     patient_hospitalization_test.patient_delete_hospitalization()
#     end_patient_hospitalization = time.time()
#     full_patient_hospitalization = end_patient_hospitalization - start_patient_hospitalization
#     print(' ▶️ Модуль - "Госпитализация", выполнен за: ', round(full_patient_hospitalization, 2),
#           'с')  # вывод полного времени тестирования
#     start_search_patient = time.time()
#     search_patient_test = search_patient(browser_RCH)  # тест модуля "Поиск пациента"
#     search_patient_test.create_patient()
#     search_patient_test.delete_patient()
#     end_search_patient = time.time()
#     full_search_patient = end_search_patient - start_search_patient
#     print(' ▶️ Модуль - "Поиск пациентов", выполнен за: ', round(full_search_patient, 2),
#           'с')  # вывод полного времени тестирования
#     end = time.time()  # конец отсчета
#     full_test = end - start  # полное время авторизации
#     print(' ▶️ Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования