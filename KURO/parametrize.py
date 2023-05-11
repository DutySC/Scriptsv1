import random

"""Параметы тестирования"""
region = 'Новосибирской области' #регион/отдельный клиент
login = 'BARS_TTEST' #логин
password = '123' #пароль
disease = 'Z00.0' #диагноз при дневнике врача
patient_1 = '11/003414' #тестовый пациент "Дневник врача"
patient_2 = '11/003437' #тестовый пациент "Расписание", "Госпитализация", "Поиск пациентов"
doctor = '' #врачь
department = '' #отделение
polyclinic = 'Аптека' #кабинет
g_disease = 'Z00.0' #диагноз при госпитализации
name_patient_1 = 'Тест Андрей Андрей' #имя тестового пациента
name_patient_2 = 'Тест Алевтина Алексеевна' #имя тестового пациента
patient = 'Тест А.А.' #сокращенное имя тестового пациента
first_name = 'Патча' #имя создаваемого тестового пользователя
last_name = 'Тестирование' #фамилия создаваемого тестового пользователя
surname = 'Новаяверсия' #отчество создаваемого тестового пользователя
data = '01011999' #дата рождения тестового пользователя
post_snils = '//tr[10]/td[1]//input[1]' #поле ввода для СНИЛС
snils = '44900573380' #статичное значение СНИЛС
position = '1'
rand = random.randint(10000000, 99999999) #рандомное значение полиса
certificate = 'Временное свидетельство' #вид полиса
area = '1' #регион
home = '13' #номер квартиры
mvd = 'МВД' #кем выдан документ