# Сложение
addition = 'Сложение'
try:
    print('=' * len(addition), addition, '=' * len(addition), sep='\n')

    user_input_1 = float(input('Введите первое число: '))
    user_input_2 = float(input('Введите второе число: '))
    result = user_input_1 + user_input_2
    print(f'Результат сложения: {result}\n')
except ValueError:
    print('Введено не числовое значение\n')

# Вычитание
subtraction = 'Вычитание'
try:
    print('=' * len(subtraction), subtraction, '=' * len(subtraction), sep='\n')

    user_input_1 = float(input('Введите первое число: '))
    user_input_2 = float(input('Введите второе число: '))
    result = user_input_1 - user_input_2
    print(f'Результат вычитания: {result}\n')
except ValueError:
    print('Введено не числовое значение\n')

# Умножение
multiplication = 'Умножение'
try:
    print('=' * len(multiplication), multiplication, '=' * len(multiplication), sep='\n')

    user_input_1 = float(input('Введите первое число: '))
    user_input_2 = float(input('Введите второе число: '))
    result = user_input_1 * user_input_2
    print(f'Результат умножения: {result}\n')
except ValueError:
    print('Введено не числовое значение\n')

# Деление
division = 'Деление'
try:
    print('=' * len(division), division, '=' * len(division), sep='\n')

    user_input_1 = float(input('Введите первое число: '))
    user_input_2 = float(input('Введите второе число: '))
    result = user_input_1 / user_input_2
    print(f'Результат деления: {result}\n')
except ValueError:
    print('Введено не числовое значение\n')
except ZeroDivisionError:
    print('На ноль делить нельзя\n')
