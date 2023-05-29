from SO import full_test_SO
# from conftest import browser_SNILS, browser_SO
import time, testit

class Test_SO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    @testit.workItemIds(214655, 214656, 214657, 214658, 214659)
    @testit.displayName('Сахалинская область')
    @testit.title('Крит. модули')
    @testit.labels('AUTOTEST_SC')
    @testit.link('https://testit.bars.group//projects/214392/tests?isolatedSection=bacab8c9-c864-411a-a2fe-1ec3a7cf3bec')
    def test_SO(self, browser_SO):
        start = time.time()  # начало отсчета
        full_test_SO.test_SO_login(browser_SO)  # тест модуля авторизации
        full_test_SO.test_SO_doctors_diary(browser_SO) # тест модуля "Дневник врача"
        full_test_SO.test_SO_schedule(browser_SO) # тест модуля "Расписание"
        full_test_SO.test_SO_hospitalization(browser_SO) # тест модуля "Госпитализация"
        full_test_SO.test_SO_search_patient(browser_SO)  # тест модуля "Поиск пациентов"
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        time_format = time.strftime("%H:%M:%S", time.gmtime(full_test))
        print('🏁 Затраченное время на тестирование: ', time_format)  # вывод полного времени тестирования

