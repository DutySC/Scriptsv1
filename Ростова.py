from RO import full_test_RO
# from conftest import browser_SNILS, browser_RO
import time, testit

class Test_RO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    @testit.workItemIds(214615, 214616, 214617, 214618, 214619)
    @testit.displayName('Ростовская область')
    @testit.title('Крит. модули')
    @testit.labels('AUTOTEST_SC')
    @testit.link('https://testit.bars.group//projects/214392/tests?isolatedSection=ce794613-67d8-4087-bfc7-786165c54492')
    def test_RO(self, browser_RO):
        start = time.time()  # начало отсчета
        full_test_RO.test_RO_login(browser_RO)  # тест модуля авторизации
        full_test_RO.test_RO_doctors_diary(browser_RO) # тест модуля "Дневник врача"
        full_test_RO.test_RO_schedule(browser_RO) # тест модуля "Расписание"
        full_test_RO.test_RO_hospitalization(browser_RO) # тест модуля "Госпитализация"
        full_test_RO.test_RO_search_patient(browser_RO) # тест модуля "Поиск пациентов"
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        time_format = time.strftime("%H:%M:%S", time.gmtime(full_test))
        print('🏁 Затраченное время на тестирование: ', time_format)  # вывод полного времени тестирования


