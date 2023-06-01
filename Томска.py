from TO import full_test_TO
# from conftest import browser_SNILS, browser_TO
import time, testit

class Test_TO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    @testit.workItemIds(214675, 214676, 214677, 214678, 214679)
    @testit.displayName('Томская область')
    @testit.title('Крит. модули')
    @testit.labels('AUTOTEST_SC')
    @testit.link('https://testit.bars.group//projects/214392/tests?isolatedSection=2947198b-979c-48f5-8074-f619af4f8ee5')
    def test_TO(self, browser_TO):
        start = time.time()  # начало отсчета
        full_test_TO.test_TO_login(browser_TO)  # тест модуля авторизации
        # full_test_TO.test_TO_doctors_diary(browser_TO) # тест модуля "Дневник врача"
        full_test_TO.test_TO_schedule(browser_TO) # тест модуля "Расписание"
        # full_test_TO.test_TO_hospitalization(browser_TO) # тест модуля "Госпитализация"
        # full_test_TO.test_TO_search_patient(browser_TO)  # тест модуля "Поиск пациентов"
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        time_format = time.strftime("%H:%M:%S", time.gmtime(full_test))
        print('🏁 Затраченное время на тестирование: ', time_format)  # вывод полного времени тестирования

