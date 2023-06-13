from selenium.common import ElementClickInterceptedException
import RO.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By

class locators_hospitalization:
    LOCATOR_HOSPITALIZATION_1 = (By.XPATH, '//span[contains(text(), "Регистратура")]')
    LOCATOR_HOSPITALIZATION_2 = (By.XPATH, '//span[contains(text(),"Приемный покой")]')
    LOCATOR_HOSPITALIZATION_3 = (By.XPATH, '//span[contains(text(),"Журнал госпитализации")]')
    LOCATOR_PATIENT_REG_CONTAINER = (By.XPATH, '//tbody/tr[6]/td[1]/div[1]/div[3]/div[1]')
    LOCATOR_WINDOW_RCM_1 = (By.XPATH, '//body[1]/div[1]/div[1]//div[1]/div[1]//td[5]')
    LOCATOR_WINDOW_RCM_2 = (By.XPATH, '//td[contains(text(), "Добавить")]')
    LOCATOR_SEARCH_PATIENT_1 = (By.XPATH, '//body[1]/div[7]//div[1]/div[1]/table[1]/tbody[1]/tr[1]//td[2]/img[1]')
    LOCATOR_SEARCH_PATIENT_2 = (By.XPATH, '//body[1]/div[8]//td[5]//input[1]')
    LOCATOR_SEARCH_PATIENT_3 = (By.XPATH, '//td[contains(text(), "Найти")]')
    LOCATOR_SEARCH_PATIENT_4 = (By.XPATH, f'//body[1]/div[8]//tr[1]//tr[1]//a[contains(text(), "{prm.name_patient}")]')
    LOCATOR_JORNAL_1 = (By.XPATH, '//body[1]/div[7]//div[1]/div[1]/table[1]//tr[2]//img[1]')
    LOCATOR_JORNAL_2 = (By.XPATH, '//body[1]/div[8]//span[contains(text(), "Журнал госпитализации")]')
    LOCATOR_HOSPITALIZATION_DEPARTMENT_1 = (By.XPATH, '//body[1]/div[7]//fieldset[1]//tbody[2]/tr[1]/td/table[1]//img[1]')
    LOCATOR_HOSPITALIZATION_DEPARTMENT_2 = (By.XPATH, '//span[contains(text(), "Гинекологическое отделение")]')
    LOCATOR_PALLET_1 = (By.XPATH, '//body[1]/div[7]//tbody[2]/tr[2]//img[1]')
    LOCATOR_PALLET_2 = (By.XPATH, '//span[contains(text(), "Кардиохирургические")]')
    LOCATOR_DIAGNOSIS_1 = (By.XPATH, '//body[1]/div[7]//fieldset[1]//tbody[3]/tr[1]//img[1]')
    LOCATOR_DIAGNOSIS_2 = (By.XPATH, '//body[1]/div[8]//tr[2]/td[1]//input[1]')
    LOCATOR_DIAGNOSIS_3 = (By.XPATH, '//body[1]/div[8]//div[1]/div[1]/div[1]/div[1]/div[1]//td[3]//td[2]')
    LOCATOR_DIAGNOSIS_4 = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_DATA_1 = (By.XPATH, '//tbody/tr[6]/td[2]/div/div/div[1]')
    LOCATOR_DATA_2 = (By.XPATH, '//div[contains(text(), "Сегодня")]')
    LOCATOR_CREATE_DIRECTION = (By.XPATH, '//body[1]/div[7]//td[contains(text(), "ОК")]')
    LOCATOR_CHOOSE_PATIENT_PCM = (By.XPATH, f'//tbody//a[contains(text(), "{prm.name_patient}")]')
    LOCATOR_HOSPITALIZATION_PATIENT_1 = (By.XPATH, '//body[1]//tr[14]/td[contains(text(), "Госпитализировать")]')
    LOCATOR_HOSPITALIZATION_PATIENT_2 = (By.XPATH, '//td[contains(text(), "Далее")]')
    LOCATOR_HOSPITALIZATION_PATIENT_3 = (By.XPATH, '//body[1]/div[7]//td[contains(text(), "ОК")]')
    LOCATOR_CANCEL_HOSPITALIZATION = (By.XPATH, '//td[contains(text(), "Отменить госпитализацию")]')
    LOCATOR_DELETE_HOSPITALIZATION = (By.XPATH, '//td[contains(text(), "Удалить")]')


class hospitalization(BasePage):
    def register_patient(self):
        global end_patient_hospitalization, start_patient_hospitalization
        try:
            start_patient_hospitalization = time.time()
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_1).click() # вкладка "Регистратура"
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_2).click() # вкладка "Приемный покой"
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_3).click() # вкладка "Журнал госпитализации"
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_PATIENT_REG_CONTAINER) # полная прогрузка элементов страницы
            time.sleep(3)  # ожидание
            self.actionchains(locators_hospitalization.LOCATOR_WINDOW_RCM_1).perform() # ПКМ по области окна
            self.find_element(locators_hospitalization.LOCATOR_WINDOW_RCM_2).click() # добавить пациента для создания направления
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            time.sleep(2)
            self.find_element(locators_hospitalization.LOCATOR_SEARCH_PATIENT_1).click() # открытие окна для выбора пациента
            self.find_element_pb()  # прогрессбар
            search_string_1 = self.find_element(locators_hospitalization.LOCATOR_SEARCH_PATIENT_2)  # окно ввода
            search_string_1.send_keys(prm.patient) # указать карту пользователя
            self.find_element(locators_hospitalization.LOCATOR_SEARCH_PATIENT_3).click()  # кнопка "Найти"
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_SEARCH_PATIENT_4).click()  # выбор пользователя "Тест Патч Пятнадцать"
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_JORNAL_1).click() # открытие выпадающего таблицы
            self.find_element(locators_hospitalization.LOCATOR_JORNAL_2).click() # выбор журнала
            self.find_element_pb(time=80)  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_DEPARTMENT_1).click() # выбор отделения
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_DEPARTMENT_2).click() # отделение "Гинекологическое отделение"
            self.find_element(locators_hospitalization.LOCATOR_PALLET_1).click()  # выбор койки
            self.find_element(locators_hospitalization.LOCATOR_PALLET_2).click()  # койка "Кардиохирургические"
            self.find_element(locators_hospitalization.LOCATOR_DIAGNOSIS_1).click() # окно выбора диагноза
            self.find_element_pb()  # прогрессбар
            search_string_2 = self.find_element(locators_hospitalization.LOCATOR_DIAGNOSIS_2) # поиск диагноза Z00.0
            search_string_2.send_keys(prm.g_disease) # ввод диагноза Z00.0
            self.find_element(locators_hospitalization.LOCATOR_DIAGNOSIS_3).click() # кнопка "Поиск"
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_DIAGNOSIS_4).click() # кнопка "ОК"
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_DATA_1).click() # выбор даты
            self.find_element(locators_hospitalization.LOCATOR_DATA_2).click() # сегодняшняя дата
            self.find_element(locators_hospitalization.LOCATOR_CREATE_DIRECTION).click() # кнопка "ОК"
            self.find_element_pb()  # прогрессбар
            print('✅ Пациент записан на госпитализацию') # вывод
            ###########след.этап########################################################################################
            self.actionchains(locators_hospitalization.LOCATOR_CHOOSE_PATIENT_PCM).perform() # ПКМ по имени пациента
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_PATIENT_1).click() # госпитализация пациента
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_PATIENT_2).click() # кнопка "Далее"
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_PATIENT_3).click() # кнопка "ОК"
            self.find_element_pb()  # прогрессбар
            print('✅ Пациент госпитализирован') # вывод
            ###########след.этап########################################################################################
            try:
                self.actionchains(locators_hospitalization.LOCATOR_CHOOSE_PATIENT_PCM).perform() # ПКМ по имени пациента
                self.find_element(locators_hospitalization.LOCATOR_CANCEL_HOSPITALIZATION).click() # отмена госпитализации пациента
                self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            except ElementClickInterceptedException:
                self.actionchains(locators_hospitalization.LOCATOR_WINDOW_RCM_1).click() # ЛКМ по области окна
                self.actionchains(locators_hospitalization.LOCATOR_CHOOSE_PATIENT_PCM).perform()  # ПКМ по имени пациента
                self.find_element(locators_hospitalization.LOCATOR_CANCEL_HOSPITALIZATION).click()  # отмена госпитализации пациента
                self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            self.find_element_pb()  # прогрессбар
            print('✅ Госпитализация отменена') # вывод
            ###########след.этап########################################################################################
            self.actionchains(locators_hospitalization.LOCATOR_CHOOSE_PATIENT_PCM).perform() # ПКМ по имени пациента
            self.find_element(locators_hospitalization.LOCATOR_DELETE_HOSPITALIZATION).click() # удаление записи на госпитализацию
            self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            self.find_element_pb()  # прогрессбар
            print('✅ Запись на госпитализацию удалена') # вывод
            end_patient_hospitalization = time.time()
            full_patient_hospitalization = end_patient_hospitalization - start_patient_hospitalization
            print('   🔼 Модуль - "Госпитализация", выполнен за: ', round(full_patient_hospitalization, 2), 'с')
        except Exception as error:
            full_patient_hospitalization = end_patient_hospitalization - start_patient_hospitalization
            print('   ❌ Модуль - "Госпитализация", завершен за: ', round(full_patient_hospitalization, 2), 'с')
            self.get_screenshots('Results/Results_sc/Госпитализация.png')
            print('❗️ Ошибка:', error)
            self.driver.quit()