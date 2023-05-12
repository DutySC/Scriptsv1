import PK.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By

class login_locators:
    LOCATOR_USER = (By.XPATH, '//tr[1]/td[3]//input[1]')
    LOCATOR_PASWD = (By.XPATH, '//tr[2]//input[1]')
    LOCATOR_ENTER = (By.XPATH, '//div[contains(text(), "Войти")]')
    LOCATOR_LPU_1 = (By.XPATH, '//div[@class="cmbb-button"]')
    LOCATOR_LPU_2 = (By.XPATH, '//tr[4][@cmptype="ComboItem"]')
    LOCATOR_LC_1 = (By.XPATH, '//div[@name="CABLAB"]/div[@class="cmbb-button"]')
    LOCATOR_LC_2 = (By.XPATH, '//div[@cmptype="Form"]/div[@cmptype="ComboBoxDL"]/table/tbody/tr[2]/td/div[@class="item_block"]')
    LOCATOR_ENTERLPU = (By.XPATH, '//tr[3]/td[1]/div[1]/div[1]')

class login(BasePage):
    def auth(self):
        user = self.find_element(login_locators.LOCATOR_USER) # логин
        user.send_keys(prm.login) # ввод логина
        paswd = self.find_element(login_locators.LOCATOR_PASWD) # пароль
        paswd.send_keys(prm.password) # ввод пароля
        self.find_element(login_locators.LOCATOR_ENTER).click() # кнопка "Войти"
        start_auth_1 = time.time() # начало отсчета
        self.find_element_pb()  # прогрессбар
        end_auth_1 = time.time() # конец отсчета
        full_auth_1 = end_auth_1 - start_auth_1 # полное время авторизации
        if full_auth_1 <= 2: # условие
            print('\n✅ Авторизация: ', round(full_auth_1, 2), 'с')
        else:
            print('\n⚠️️ Авторизация: ', round(full_auth_1, 2), 'с', '(норма - менее 2 с)')
        time.sleep(1) # ожидание
        self.find_element(login_locators.LOCATOR_LPU_1).click() # открыть вкладку ЛПУ
        self.find_element(login_locators.LOCATOR_LPU_2).click() # выбор ЛПУ
        self.find_element_pb()  # прогрессбар
        self.find_element(login_locators.LOCATOR_ENTERLPU).click() # продолжить
        start_auth_2 = time.time() # начало отсчета
        self.find_element_pb()  # прогрессбар
        end_auth_2 = time.time() # начало отсчета
        full_auth_2 = end_auth_2 - start_auth_2 # полное время выбора ЛПУ
        if full_auth_2 <= 5: # условие
            print('✅ Выбор ЛПУ: ', round(full_auth_2, 2), 'с')
        else:
            print('⚠️️ Выбор ЛПУ: ', round(full_auth_2, 2), 'с', '(норма - менее 5 с)')
        full_auth = full_auth_1 + full_auth_2 # полное время модуля авторизации
        print(' ▶️ Модуль - "Авторизация", выполнен за: ', round(full_auth, 2), 'с') # вывод полного времени модуля авторизации
