from RSO import full_test_RSO
# from conftest import browser_SNILS, browser_RSO
import time, testit

class Test_RSO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    @testit.workItemIds(214640, 214641, 214642, 214643, 214644)
    @testit.displayName('РСО-Алания')
    @testit.title('Крит. модули')
    @testit.labels('AUTOTEST_SC')
    @testit.link('https://testit.bars.group//projects/214392/tests?isolatedSection=f400646c-712b-4d0e-96e0-d418e5d16d5f')
    def test_RSO(self, browser_RSO):
        start = time.time()  # начало отсчета
        full_test_RSO.test_RSO_login(browser_RSO)  # тест "Авторизации"
        # full_test_RSO.test_RSO_doctors_diary(browser_RSO)  # тест "Дневник врача"
        # full_test_RSO.test_RSO_schedule(browser_RSO)  # тест "Расписание"
        # full_test_RSO.test_RSO_hospitalization(browser_RSO)  # тест "Госпитализация"
        # full_test_RSO.test_RSO_search_patient(browser_RSO)  # тест "Поиск пациентов"
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        time_format = time.strftime("%H:%M:%S", time.gmtime(full_test))
        print('🏁 Затраченное время на тестирование: ', time_format)  # вывод полного времени тестирования
