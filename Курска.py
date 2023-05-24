from KURO import full_test_KURO
# from conftest import browser_SNILS, browser_KURO
import time

class Test_KURO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    def test_KURO(self, browser_KURO):
        start = time.time()  # начало отсчета
        full_test_KURO.test_KURO_login(browser_KURO)  # тест "Авторизации"
        full_test_KURO.test_KURO_doctors_diary(browser_KURO)  # тест "Дневник врача"
        full_test_KURO.test_KURO_schedule(browser_KURO)  # тест "Расписание"
        full_test_KURO.test_KURO_hospitalization(browser_KURO)  # тест "Госпитализация"
        full_test_KURO.test_KURO_search_patient(browser_KURO)  # тест "Поиск пациентов"
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        print('🏁 Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования
