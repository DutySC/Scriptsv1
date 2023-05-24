from PK import full_test_PK
# from conftest import browser_SNILS, browser_PK
import time

class Test_PK:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    def test_PK(self, browser_PK):
        start = time.time()  # начало отсчета
        full_test_PK.test_PK_login(browser_PK)  # тест модуля авторизации
        full_test_PK.test_PK_doctors_diary(browser_PK) # тест модуля "Дневник врача"
        full_test_PK.test_PK_schedule(browser_PK) # тест модуля "Расписание"
        full_test_PK.test_PK_hospitalization(browser_PK) # тест модуля "Госпитализация"
        full_test_PK.test_PK_search_patient(browser_PK)  # тест модуля "Поиск пациентов"
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        print('🏁 Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования

