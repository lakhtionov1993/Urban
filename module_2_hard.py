def get_password(number):
    password = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            elif number % (i + j) == 0:
                password += str(i) + str(j)
    return password
number = int(input('Введите число(от 3 до 20): '))
result = get_password(number)
print('Пароль:', result)


