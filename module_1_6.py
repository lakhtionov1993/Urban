#Работа со словарями(версия 1):
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict:', my_dict)
print('Existing value:' , my_dict.get('Masha'))
print('Not existing value:' , my_dict.get('Vitalii'))
my_dict["Artem"] = 1915
my_dict["Kamila"] = 1981
print('Deleted value: ' , my_dict.pop('Egor'))
print('Modified dictionary: ', my_dict, '''

''')
#Работа с множествами:
print("Работа с множествам: ")
my_set = [1, 1,  'Яблоко', 42.314]
my_set=set(my_set)
print("Set: " , my_set)
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.discard(1)
print("Modified set: " , my_set, '''

''')
#Работа со словарями(версия 2):
print("Работа со словарями(версия 2): ")
my_dict = {"Виталий" : 1993 , "Надежда" : 1993 , "Василиса" : 2019 }
print(my_dict,)
print("Введите имя, чтобы узнать год рождения :")
Name=input()
print(my_dict.get(Name, "Человека с таким именем нет в списке!"))
print("Добавление в список двух людей: Ольга и Алексей!")
my_dict["Ольга"] = 1974
my_dict["Алексей"] = 1971
print(my_dict)
print("Введите имя человека, которого хотите удалить из списка:")
Name=input()
a = my_dict.pop(Name, "Человека с таким именем нет в списке!")
print(a)
print('''Окончательный список : 
''',  my_dict)
