from TVERO import full_test_TVERO
# from conftest import browser_SNILS, browser_TVERO
import time, testit

class Test_TVERO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    @testit.workItemIds(214696, 214697, 214698, 214699, 214700)
    @testit.displayName('Тверская область')
    @testit.title('Крит. модули')
    @testit.labels('AUTOTEST_SC')
    @testit.link('https://testit.bars.group//projects/214392/tests?iTVEROlatedSection=0ba1b753-1a2c-4e65-b372-4c973fabb967')
    def test_TVERO(self, browser_TVERO):
        start = time.time()  # начало отсчета
        full_test_TVERO.test_TVERO_login(browser_TVERO)  # тест модуля авторизации
        # full_test_TVERO.test_TVERO_doctors_diary(browser_TVERO) # тест модуля "Дневник врача"
        full_test_TVERO.test_TVERO_schedule(browser_TVERO) # тест модуля "Расписание"
        # full_test_TVERO.test_TVERO_hospitalization(browser_TVERO) # тест модуля "Госпитализация"
        # full_test_TVERO.test_TVERO_search_patient(browser_TVERO)  # тест модуля "Поиск пациентов"
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        time_format = time.strftime("%H:%M:%S", time.gmtime(full_test))
        print('🏁 Затраченное время на тестирование: ', time_format)  # вывод полного времени тестирования

