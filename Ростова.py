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
        full_test_RO.test_RO_login(browser_RO)  # тест модуля авторизации
        full_test_RO.test_RO_doctors_diary(browser_RO) # тест модуля "Дневник врача"
        full_test_RO.test_RO_schedule(browser_RO) # тест модуля "Расписание"
        full_test_RO.test_RO_hospitalization(browser_RO) # тест модуля "Госпитализация"
        full_test_RO.test_RO_search_patient(browser_RO) # тест модуля "Поиск пациентов"
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        print('🏁 Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования


