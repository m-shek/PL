# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
students_distinct = []

for student in students:
    name = student['first_name']

    if students_distinct.count(name) == 0:
        print(f"Людей с именем {name} в классе: {students.count(student)}")
        students_distinct.append(name)

print(f"Уникальные имена: {students_distinct}")
print("------------------")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

name_for_count = ''
count = 0
for student in students:
    if count == 0:
        count = students.count(student)
        name_for_count = student['first_name']
    elif count < students.count(student):
        count = students.count(student)
        name_for_count = student['first_name']
print(f"Самое частое имя среди учеников {name_for_count}, количество {count}")
print("------------------")

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
statistic = []
for class_num in school:
    school_class = class_num['students']
    count_men = 0
    count_women = 0
    for student in school_class:
        student_name = student['first_name']
        for gender in is_male:
            if student_name == gender:
                if is_male.get(gender):
                    count_men += 1
                elif not is_male.get(gender):
                    count_women += 1
    statistic.append({"class": class_num['class'], "count_men": count_men, "count_women": count_women})

for gender_count in statistic:
    print(f"Класс {gender_count['class']} Мальчиков {gender_count['count_men']} , Девочек {gender_count['count_women']}")
print("------------------")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
statistic = []
for class_num in school:
    school_class = class_num['students']
    count_men = 0
    count_women = 0
    for student in school_class:
        student_name = student['first_name']
        for gender in is_male:
            if student_name == gender:
                if is_male.get(gender):
                    count_men += 1
                elif not is_male.get(gender):
                    count_women += 1
    statistic.append({"class": class_num['class'], "count_men": count_men, "count_women": count_women})

gender_men = 0
gender_women = 0
for gender_count in statistic:
    if gender_count['count_men'] >= gender_men:
        gender_men = gender_count['count_men']
        class_more_men = gender_count['class']
    if gender_count['count_women'] >= gender_women:
        gender_women = gender_count['count_women']
        class_more_women = gender_count['class']
print(f'Девочек больше в  классе  {class_more_women} , кол-во {gender_women}')
print(f'Мальчиков больше в  классе  {class_more_men} , кол-во {gender_men}')
print("------------------")