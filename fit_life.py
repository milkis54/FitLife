# Проект FitLife - MVP версия 1.0
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. Знакомство
print('Здравствуйте! Я Ваш помщник в приложение Fit Life.')
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
user_name = input('Как я могу к Вам обращаться?')
# TODO: Спроси возраст и сохрани в переменную user_age
user_ages = int(input('Сколько Вам лет?'))

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
user_weight = float(input('Какой Ваш вес?'))
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height
user_height = float(input('Какой Ваш рост?'))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
WATER_ML_KG = 30
WATER_L_KG = 1000
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_ml = user_weight * 30
water_l = water_ml / 1000

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например:"Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f'Отчет для пользователя: {user_name} ({user_ages} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l}')
print(f'Расчет окончен. До свидания, {user_name}!\n')
