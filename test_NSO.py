from NSO.page_object.login_page import login
from NSO.page_object.doctors_diary_page import doctors_diary
from NSO.page_object.schedule_page import schedule
from NSO.page_object.hospitalization_page import hospitalization
from NSO.page_object.search_patient_page import search_patient
from conftest import browser_SNILS, browser_PK
import time

class Test_NSO:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    def test_NSO_full(self, browser_NSO):


    """Тест по модулям"""
    def test_PK_login(self, browser_NSO):

    def test_PK_doctors_diary(self, browser_NSO):

    def test_PK_schedule(self, browser_NSO):

    def test_PK_hospitalization(self, browser_NSO):

    def test_PK_search_patient(self, browser_NSO):
