import random

"""Параметы тестирования"""
region = 'Тверская область' #регион/отдельный клиент
login = 'BARS_TTEST' #логин
password = '123' #пароль
disease = 'J10.0' #диагноз при дневнике врача
patient = '23/000021' #тестовый пациент
doctor = 'Белялова Л.С.' #врачь
department = 'Поликлиника отд' #отделение
polyclinic = 'ТЕРАПЕВТ' #кабинет
g_disease = 'J10.0' #диагноз при госпитализации
name_patient = 'Тест Тестирование Патчей' #имя тестового пациента
schedule_patient = 'Тест Т.П.' #сокращенное имя тестового пациента
first_name = 'Патча' #имя создаваемого тестового пользователя
last_name = 'Тестирование' #фамилия создаваемого тестового пользователя
surname = 'Новаяверсия' #отчество создаваемого тестового пользователя
data = '01011999' #дата рождения тестового пользователя
post_snils = '//tr[10]/td[1]//input[1]' #поле ввода для СНИЛС
snils = '37273811090' #статичное значение СНИЛС
position = '1'
rand = random.randint(10000000, 99999999) #рандомное значение полиса
certificate = 'Временное свидетельство' #вид полиса
area = '1' #регион
home = '13' #номер квартиры
mvd = 'МВД' #кем выдан документ