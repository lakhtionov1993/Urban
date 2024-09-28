grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
i = 0
new_grades = []
while i < len(grades):
    if grades[i] == len(grades):
        break
    new_grades.append(sum(grades[i])/len(grades[i]))
    i += 1
students_grades = {}
for n in range(0, len(grades)):
    students_grades[students[n]] = new_grades[n]
print(students_grades)
#Дополнительная функция
Name = input()
print(students_grades.get(Name, "No data available!"))