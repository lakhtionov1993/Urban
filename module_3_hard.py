
def calculate_structure_sum(data_structure):
    n = 0
    if isinstance(data_structure, dict): #словари
        for key, value in data_structure.items():
            n += calculate_structure_sum(key)
            n += calculate_structure_sum(value)
    elif isinstance(data_structure, (list, tuple, set)): #списки, кортежи, множетсва
        for i in data_structure:
            n += calculate_structure_sum(i)
    elif isinstance(data_structure, (int, float)): #целые числа, числа с плавающей точкой
        n += data_structure
    elif isinstance(data_structure, str): #строки
        n += len(data_structure)
    return n


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)

