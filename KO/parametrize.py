import random

"""Параметы тестирования"""
region = 'Калининградская область' #регион/отдельный клиент
login = 'BARS_TTEST' #логин
password = '123' #пароль
disease = 'J10.0' #диагноз при дневнике врача
patient = '6145988' #тестовый пациент
doctor = 'Врач О.Г.' #врачь
department = 'Поликлиника отд' #отделение
polyclinic = 'Основной график' #кабинет
g_disease = 'Z00.0' #диагноз при госпитализации
name_patient = 'Тестовый Тестовый Тест' #имя тестового пациента
schedule_patient = 'Тестовый Т.Т.' #сокращенное имя тестового пациента
first_name = 'Патча' #имя создаваемого тестового пользователя
last_name = 'Тестирование' #фамилия создаваемого тестового пользователя
surname = 'Новаяверсия' #отчество создаваемого тестового пользователя
data = '01011999' #дата рождения тестового пользователя
post_snils = '//tr[10]/td[1]//input[1]' #поле ввода для СНИЛС
snils = '69870470261' #статичное значение СНИЛС
position = '1'
rand = random.randint(10000000, 99999999) #рандомное значение полиса
certificate = 'Временное свидетельство' #вид полиса
area = '1' #регион
home = '13' #номер квартиры
mvd = 'МВД' #кем выдан документ
place = 'test'