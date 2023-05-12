from NSO import full_test_NSO
# from conftest import browser_SNILS, browser_NSO
import time

class Test_NSO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    def test_NSO(self, browser_NSO):
        start = time.time()  # начало отсчета
        try:
            full_test_NSO.test_NSO_login(browser_NSO)
            # self.test_NSO_login(browser_NSO)  # тест "Авторизации"
        except Exception as error_1:
            print('Ошибка:', error_1)
        try:
            start_doctors_diary = time.time()
            full_test_NSO.test_NSO_doctors_diary(browser_NSO)
            # self.test_NSO_doctors_diary(browser_NSO) # тест "Дневник врача"
            end_doctors_diary = time.time()
            full_doctors_diary = end_doctors_diary - start_doctors_diary
            print(' ▶️ Модуль - "Дневник врача", выполнен за: ', round(full_doctors_diary, 2), 'с')  # вывод полного времени тестирования
        except Exception as error_2:
            print('Ошибка:', error_2)
        try:
            start_patient_schedule = time.time()
            full_test_NSO.test_NSO_schedule(browser_NSO)
            # self.test_NSO_schedule(browser_NSO) # тест "Расписание"
            end_patient_schedule = time.time()
            full_patient_schedule = end_patient_schedule - start_patient_schedule
            print(' ▶️ Модуль - "Расписание", выполнен за: ', round(full_patient_schedule, 2), 'с')  # вывод полного времени тестирования
        except Exception as error_3:
            print('Ошибка:', error_3)
        try:
            start_patient_hospitalization =time.time()
            full_test_NSO.test_NSO_hospitalization(browser_NSO)
            # self.test_NSO_hospitalization(browser_NSO) # тест "Госпитализация"
            end_patient_hospitalization = time.time()
            full_patient_hospitalization = end_patient_hospitalization - start_patient_hospitalization
            print(' ▶️ Модуль - "Госпитализация", выполнен за: ', round(full_patient_hospitalization, 2), 'с')  # вывод полного времени тестирования
        except Exception as error_4:
            print('Ошибка:', error_4)
        try:
            start_search_patient = time.time()
            full_test_NSO.test_NSO_search_patient(browser_NSO)
            # self.test_NSO_search_patient(browser_NSO) # тест "Поиск пациентов"
            end_search_patient = time.time()
            full_search_patient = end_search_patient - start_search_patient
            print(' ▶️ Модуль - "Поиск пациентов", выполнен за: ', round(full_search_patient, 2), 'с')  # вывод полного времени тестирования
        except Exception as error_5:
            print('Ошибка:', error_5)
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        print(' ▶️ Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования
