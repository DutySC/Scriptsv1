from RO import full_test_RO
# from conftest import browser_SNILS, browser_RO
import time

class Test_RO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    def test_RO(self, browser_RO):
        start = time.time()  # начало отсчета
        try:
            full_test_RO.test_RO_login(browser_RO)  # тест модуля авторизации
        except Exception as error_1:
            print('Ошибка:', error_1)
        try:
            start_doctors_diary = time.time()
            full_test_RO.test_RO_doctors_diary(browser_RO) # тест модуля "Дневник врача"
            end_doctors_diary = time.time()
            full_doctors_diary = end_doctors_diary - start_doctors_diary
            print(' ▶️ Модуль - "Дневник врача", выполнен за: ', round(full_doctors_diary, 2), 'с')  # вывод полного времени тестирования
        except Exception as error_2:
            print('Ошибка:', error_2)
        try:
            start_patient_schedule = time.time()
            full_test_RO.test_RO_schedule(browser_RO) # тест модуля "Расписание"
            end_patient_schedule = time.time()
            full_patient_schedule = end_patient_schedule - start_patient_schedule
            print(' ▶️ Модуль - "Расписание", выполнен за: ', round(full_patient_schedule, 2), 'с')  # вывод полного времени тестирования
        except Exception as error_3:
            print('Ошибка:', error_3)
        try:
            start_patient_hospitalization = time.time()
            full_test_RO.test_RO_hospitalization(browser_RO) # тест модуля "Госпитализация"
            end_patient_hospitalization = time.time()
            full_patient_hospitalization = end_patient_hospitalization - start_patient_hospitalization
            print(' ▶️ Модуль - "Госпитализация", выполнен за: ', round(full_patient_hospitalization, 2), 'с')  # вывод полного времени тестирования
        except Exception as error_4:
            print('Ошибка:', error_4)
        try:
            start_search_patient = time.time()
            full_test_RO.test_RO_search_patient(browser_RO) # тест модуля "Поиск пациентов"
            end_search_patient = time.time()
            full_search_patient = end_search_patient - start_search_patient
            print(' ▶️ Модуль - "Поиск пациентов", выполнен за: ', round(full_search_patient, 2), 'с')  # вывод полного времени тестирования
        except Exception as error_5:
            print('Ошибка:', error_5)
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        print(' ▶️ Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования


