from NSO import full_test_NSO
# from conftest import browser_SNILS, browser_NSO
import time, testit

class Test_NSO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    @testit.workItemIds(214541, 214542, 214543, 214544, 214545)
    @testit.displayName('НСО')
    @testit.title('Крит. модули')
    @testit.labels('AUTOTEST_SC')
    @testit.link('https://testit.bars.group//projects/214392/tests?isolatedSection=b2221a92-83be-4963-9397-a914fdcdae86')
    def test_NSO(self, browser_NSO):
        start = time.time()  # начало отсчета
        full_test_NSO.test_NSO_login(browser_NSO)
        full_test_NSO.test_NSO_doctors_diary(browser_NSO)
        full_test_NSO.test_NSO_schedule(browser_NSO)
        full_test_NSO.test_NSO_hospitalization(browser_NSO)
        full_test_NSO.test_NSO_search_patient(browser_NSO)
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        time_format = time.strftime("%H:%M:%S", time.gmtime(full_test))
        print('Затраченное время на тестирование: ', time_format)  # вывод полного времени тестирования

