import random

"""Параметы тестирования"""
region = 'Ростовской области' #регион/отдельный клиент
login = 'BARS_TTEST' #логин
password = '123' #пароль
disease = 'J10.0' #диагноз при дневнике врача
patient = '160000202' #тестовый пациент
doctor = 'Тестирование П.' #врачь
department = 'Поликлиника отд' #отделение
polyclinic = 'Тестирование_графиков' #кабинет
g_disease = 'Z00.0' #диагноз при госпитализации
name_patient = 'Тесттап Тап Тап' #имя тестового пациента
schedule_patient = 'Тесттап Т.Т.' #сокращенное имя тестового пациента
first_name = 'Патча' #имя создаваемого тестового пользователя
last_name = 'Тестирование' #фамилия создаваемого тестового пользователя
surname = 'Новаяверсия' #отчество создаваемого тестового пользователя
data = '01011999' #дата рождения тестового пользователя
post_snils = '//tr[10]/td[1]//input[1]' #поле ввода для СНИЛС
snils = '79166023523' #статичное значение СНИЛС
position = '1'
rand_1 = random.randint(10000000, 99999999) #рандомное значение полиса
rand_2 = random.randint(1000000000, 9999999999) #рандомное значение полиса
certificate = 'Временное свидетельство' #вид полиса
area = '1' #регион
home = '13' #номер квартиры
mvd = 'МВД' #кем выдан документ