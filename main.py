# Сложение
addition = 'Сложение'
try:
    print('=' * len(addition))
    print(addition)
    print('=' * len(addition))

    user_input_1 = float(input('Введите первое число: '))
    user_input_2 = float(input('Введите второе число: '))
    result = user_input_1 + user_input_2
    print(f'Результат сложения: {result}\n')
except ValueError:
    print('Введено не числовое значение\n')

# Вычитание
subtraction = 'Вычитание'
try:
    print('=' * len(subtraction))
    print(subtraction)
    print('=' * len(subtraction))

    user_input_1 = float(input('Введите первое число: '))
    user_input_2 = float(input('Введите второе число: '))
    result = user_input_1 - user_input_2
    print(f'Результат вычитания: {result}\n')
except ValueError:
    print('Введено не числовое значение\n')

# Умножение
multiplication = 'Умножение'
try:
    print('=' * len(multiplication))
    print(multiplication)
    print('=' * len(multiplication))

    user_input_1 = float(input('Введите первое число: '))
    user_input_2 = float(input('Введите второе число: '))
    result = user_input_1 * user_input_2
    print(f'Результат умножения: {result}\n')
except ValueError:
    print('Введено не числовое значение\n')

# Деление
division = 'Деление'
try:
    print('=' * len(division))
    print(division)
    print('=' * len(division))

    user_input_1 = float(input('Введите первое число: '))
    user_input_2 = float(input('Введите второе число: '))
    result = user_input_1 / user_input_2
    print(f'Результат деления: {result}\n')
except ValueError:
    print('Введено не числовое значение\n')
except ZeroDivisionError:
    print('На ноль делить нельзя\n')
