# Проект FitLife - MVP версия 1.0
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

WATER_PER_KG = 30
WATER_ML_L_KG = 1000
# 1. Знакомство
print('Здравствуйте! Я Ваш помщник в приложение Fit Life.')
# Было выполнено с помощью ИИ
user_name = ('Как я могу к Вам обращаться?')

while True:
    user_name = input('Как я могу к Вам обращаться?')
    if user_name.strip():
        break
    else:
        print('Введите, пожалуйста, свое имя.')


user_ages = int(input('Сколько Вам лет?'))


# 2. Сбор данных

user_weight = float(input('Какой Ваш вес?'))

user_height = float(input('Какой Ваш рост?'))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)

bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл

water_ml = user_weight * 30
water_l = water_ml / 1000

# 4. Вывод красивого результата

print(f'Отчет для пользователя: {user_name} ({user_ages})\n')
print(f'Твой Индекс Массы Тела: {bmi}\n')
if bmi <= 16:
    print('Выраженный дефицит массы тела')
elif 16 <= bmi <= 18.5:
    print('Недостаточная масса тела')
elif 18.5 <= bmi <= 25:
    print('Норма')
elif 25 <= bmi <= 30:
    print('Избыточная масса тела (предожирение)')
elif 30 <= bmi <= 35:
    print('Ожирение 1 степени')
elif 35 <= bmi <= 40:
    print('Ожирение 2 степени')
elif 40 <= bmi:
    print('Ожирение 3 степени')
print(f'Рекомендуемая норма воды: {water_l}\n')
print("Расчет окончен. Будьте здоровы!\n")
