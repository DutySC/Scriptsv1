from HK import full_test_HK
# from conftest import browser_SNILS, browser_HK
import time, testit

class Test_HK:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    @testit.workItemIds(214680, 214681, 214682, 214683, 214684)
    @testit.displayName('Хабаровский край')
    @testit.title('Крит. модули')
    @testit.labels('AUTOTEST_SC')
    @testit.link('https://testit.bars.group//projects/214392/tests?isolatedSection=20dfb6cd-0e70-4bc6-8a1f-e03c54578c09')
    def test_HK(self, browser_HK):
        start = time.time()  # начало отсчета
        full_test_HK.test_HK_login(browser_HK)
        full_test_HK.test_HK_doctors_diary(browser_HK)
        full_test_HK.test_HK_schedule(browser_HK)
        full_test_HK.test_HK_hospitalization(browser_HK)
        full_test_HK.test_HK_search_patient(browser_HK)
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        time_format = time.strftime("%H:%M:%S", time.gmtime(full_test))
        print('🏁 Затраченное время на тестирование: ', time_format)  # вывод полного времени тестирования

