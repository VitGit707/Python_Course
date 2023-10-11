"""
a = 5
b = 5.89
c = 'hello'

print(a,' - ', b,' - ', c)
print(f"{a} - {b} - {c}")
print("{} - {} - {}".format(a,b,c))
"""
# Ввод данных:
# 1-ый вариант ввода данных:
# print('Введите первое число: ')
# a = input()
# print(a)

# 2-ой вариант ввода данных:
# print('Введите первое число: ')
# a = input()
# b = input('Введите второе число: ')

# print('Введите первое число: ')
# a = input()
# b = input('Введите второе число: ')

# print(a, ' + ', b, ' = ', a + b)

# Приведение типов:  Чтобы получить сумму чисел, а не сложение 2-ух
# строк нужно применить Применение типов

# c = 5.89
# print(c)
# n = int(c)
# print(n)

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# Когда невозможно приведение данных (В терминале будет ошибка при
# расчетах):
# Например: v = int (v)
#        ^^^^^^^
# ValueError: invalid literal for int() with base 10: 'fkjghdfk'
# v = 'fkjghdfk'
# v = int (v)

# Вариант кода, который складывает числа:
# print('Введите первое число: ')
# a = int(input())
# b = int(input('Введите второе число: '))
# print(a, ' + ', b, ' = ', a + b)

# Округление чисел:

# a = 5.554894
# b = 6.564987
# print(round(a*b, 3)) # В первом аргументе мы указываем число котор хотим 
#                      # округлить, и во втором аргументе число, 
#                      # сколько знаков после запятой мы хотим округлить

# Сокращеные операции присваивания:
# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# Логические операции в Python
# Примеры логич операций:

# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a ='qwe'
# b ='qwe'
# print (a == b)
# a = 1 < 3 < 5 < 10
# print (a)

# Управляющие конструкции IF ELSE

# Пример:
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина!')
# elif username == 'Ильнар':
#    print('Ильнар - топ)')
# else:
#    print('Привет, ', username)

# Управляющие конструкции IF ELSE
# Пример:
# n = 423
# summa = 423
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(summa)

# Пример:
a = 'qwerty'
print(a[2])
# пройдемся по всей строке qwerty с помощью цила for
for i in a:
    print(i)