immutable_var = 1, 2, 'a', 'b'
print("immutable_var:" , immutable_var)
try:
    immutable_var[0] = 34
    print(immutable_var)
except:
    print('данный вид кортежа не поддерживает обращение к элементам')
finally:
    mutable_list = [1, 2, 'a', 'b']
    mutable_list.append('Modified') #добавление эелемента кортежа
    print("mutable_list :" , mutable_list)
    mutable_list[1] = 'Привет' #изменение элемента [n] кортежа на вводимое значение
    print("mutable_list_new" , mutable_list)
