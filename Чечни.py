from RCH import full_test_RCH
# from conftest import browser_SNILS, browser_RCH
import time, testit

class Test_RCH:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    @testit.workItemIds(214686, 214687, 214688, 214689, 214690)
    @testit.displayName('Республика Чечня')
    @testit.title('Крит. модули')
    @testit.labels('AUTOTEST_SC')
    @testit.link('https://testit.bars.group//projects/214392/tests?isolatedSection=42adb35d-8166-44a7-ac36-d8f5e13eccc2')
    def test_RCH(self, browser_RCH):
        start = time.time()  # начало отсчета
        full_test_RCH.test_RCH_login(browser_RCH)  # тест модуля авторизации
        # full_test_RCH.test_RCH_doctors_diary(browser_RCH) # тест модуля "Дневник врача"
        # full_test_RCH.test_RCH_schedule(browser_RCH) # тест модуля "Расписание"
        # full_test_RCH.test_RCH_hospitalization(browser_RCH) # тест модуля "Госпитализация"
        full_test_RCH.test_RCH_search_patient(browser_RCH)  # тест модуля "Поиск пациентов"
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        time_format = time.strftime("%H:%M:%S", time.gmtime(full_test))
        print('🏁 Затраченное время на тестирование: ', time_format)  # вывод полного времени тестирования

