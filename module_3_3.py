def print_params(a = 1, b = 'строка', c = True):
    if a == b == c == None:
        print('Вызов функции без аргументов')
    elif a == b == None:
        print(c)
    elif b == c == None:
        print(a)
    elif a == c == None:
        print(b)
    elif a == None:
        print(b, c)
    elif b == None:
        print(a, c)
    elif c == None:
        print(a, b)
    else:
        print(a, b, c)


print('1. Функция с параметром по умолчанию:')
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print()
print('1.1. Вызов функций с разным количеством аргументов:')
print_params(a = None ,b = None , c = None)
print_params(b = None , c = None)
print_params(a = None , c = None)
print_params(a = None , b = None)
print_params(a = None)
print_params(b = None)
print_params(c = None)



print('''
''')
print('2. Распаковка параметров:')
values_list = ['Виталий', 31, False]
values_dict = {'a': 'Лахтионов', 'b': 1993, 'c': True}
print_params(*values_list)
print_params(**values_dict)


print('''
''')
print('3. Распаковка + отдельные параметры:')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

