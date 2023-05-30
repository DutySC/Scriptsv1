from KO import full_test_KO
# from conftest import browser_SNILS, browser_KO
import time, testit

class Test_KO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    @testit.workItemIds(214630, 214631, 214632, 214633, 214634)
    @testit.displayName('Калининградская область')
    @testit.title('Крит. модули')
    @testit.labels('AUTOTEST_SC')
    @testit.link('https://testit.bars.group//projects/214392/tests?isolatedSection=4be2f6e0-2be2-4830-9b31-b0eaffbc7b83')
    def test_KO(self, browser_KO):
        start = time.time()  # начало отсчета
        full_test_KO.test_KO_login(browser_KO)
        # full_test_KO.test_KO_doctors_diary(browser_KO)
        # full_test_KO.test_KO_schedule(browser_KO)
        # full_test_KO.test_KO_hospitalization(browser_KO)
        # full_test_KO.test_KO_search_patient(browser_KO)
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        time_format = time.strftime("%H:%M:%S", time.gmtime(full_test))
        print('Затраченное время на тестирование: ', time_format)  # вывод полного времени тестирования

