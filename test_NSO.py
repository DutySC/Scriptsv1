from NSO.page_object.login_page import login
from NSO.page_object.doctors_diary_page import doctors_diary
# from NSO.page_object.schedule_page import schedule
# from NSO.page_object.hospitalization_page import hospitalization
# from NSO.page_object.search_patient_page import search_patient
from conftest import browser_SNILS, browser_PK
import time

class Test_NSO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    def test_NSO_full(self, browser_NSO):
        start = time.time()  # начало отсчета
        start_page = login(browser_NSO)  # тест модуля авторизации
        start_page.auth()
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        print(' ▶️ Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования

    """Тест по модулям"""
    def test_PK_login(self, browser_NSO):
        start_page = login(browser_NSO)  # тест модуля авторизации
        start_page.auth()
        print('STAGE_1: COMPLETE')

    def test_PK_doctors_diary(self, browser_NSO):
        self.test_PK_login(browser_NSO) # тест авторизации
        doctors_diary_test = doctors_diary(browser_NSO)
        doctors_diary_test.diary()
        doctors_diary_test.diary_provide_service()
        doctors_diary_test.diary_delite()
        print('STAGE_2: COMPLETE')

    # def test_PK_schedule(self, browser_NSO):
    #     self.test_PK_login(browser_NSO) # тест авторизации
    #     patient_schedule_test = schedule(browser_NSO)
    #     patient_schedule_test.patient_schedule()
    #     patient_schedule_test.patient_schedule_delete()
    #     print('STAGE_3: COMPLETE')

    # def test_PK_hospitalization(self, browser_NSO):
    #     self.test_PK_login(browser_NSO) # тест авторизации
    #     patient_hospitalization_test = hospitalization(browser_NSO)
    #     patient_hospitalization_test.register_patient()
    #     patient_hospitalization_test.patient_hospitalization()
    #     patient_hospitalization_test.patient_cancel_hospitalization()
    #     patient_hospitalization_test.patient_delete_hospitalization()
    #     print('STAGE_4: COMPLETE')

    # def test_PK_search_patient(self, browser_NSO):
    #     self.test_PK_login(browser_NSO) # тест авторизации
    #     search_patient_test = search_patient(browser_NSO)
    #     search_patient_test.create_patient()
    #     search_patient_test.delete_patient()
    #     print('STAGE_5: COMPLETE')

