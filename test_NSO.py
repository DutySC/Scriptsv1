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
        full_test_NSO.test_NSO_login(browser_NSO)
        full_test_NSO.test_NSO_doctors_diary(browser_NSO)
        full_test_NSO.test_NSO_schedule(browser_NSO)
        full_test_NSO.test_NSO_hospitalization(browser_NSO)
        full_test_NSO.test_NSO_search_patient(browser_NSO)
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        print('🏁 Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования