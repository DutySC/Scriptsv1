from KURO import full_test_KURO
# from conftest import browser_SNILS, browser_KURO
import time, testit

class Test_KURO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    @testit.workItemIds(214620, 214621, 214622, 214623, 214624)
    @testit.displayName('Курская область')
    @testit.title('Крит. модули')
    @testit.labels('AUTOTEST_SC')
    @testit.link('https://testit.bars.group//projects/214392/tests?isolatedSection=209dbcc0-ff8d-4f70-a294-d204c5b97dfb')
    def test_KURO(self, browser_KURO):
        start = time.time()  # начало отсчета
        full_test_KURO.test_KURO_login(browser_KURO)  # тест "Авторизации"
        full_test_KURO.test_KURO_doctors_diary(browser_KURO)  # тест "Дневник врача"
        full_test_KURO.test_KURO_schedule(browser_KURO)  # тест "Расписание"
        full_test_KURO.test_KURO_hospitalization(browser_KURO)  # тест "Госпитализация"
        full_test_KURO.test_KURO_search_patient(browser_KURO)  # тест "Поиск пациентов"
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        time_format = time.strftime("%H:%M:%S", time.gmtime(full_test))
        print('🏁 Затраченное время на тестирование: ', time_format)  # вывод полного времени тестирования
