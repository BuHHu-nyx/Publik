import random
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}

for student in students:
    students_marks[student] = {}

    for class_ in classes:
        marks = [random.randint(2,5) for i in range(3)]
        students_marks[student][class_] = marks

for student in students:
    print(f'''{student}
    {students_marks[student]}''')
print('''
Список команд:
1. Редактировать оценки ученика по предмету
2. Вывести средний балл 
3. Вывести оценки
4. Редактировать список учеников
5. Редактировать список предметов 
6. Выход из программы
''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('''
        Список команд:
        1. Добавить оценку ученика по предмету
        2. Удалить оценку ученика по предмету
        3. Редактировать оценку ученика по предмету
        4. Выйти в основное меню
        ''')
        while True:
            command1 = int(input('Введите команду: '))
            if command1 == 1:
                print('1. Добавить оценку ученика по предмету')
                student = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    mark = int(input('Введите оценку: '))
                    students_marks[student][class_].append(mark)
                    print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                    print(f'У {student} по предмету {class_} следующие оценки {students_marks[student][class_]}')
                else:
                    print('ОШИБКА: неверное имя ученика или название предмета')
            elif command1 == 2:
                print('2. Удалить оценку ученика по предмету')
                student = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    print(f'У {student} по предмету {class_} следующие оценки {students_marks[student][class_]}')
                    print()
                    mark = int(input('Введите оценку, которую нужно удалить: '))
                    if mark in students_marks[student][class_]:
                        students_marks[student][class_].remove(mark)
                        print(f'Для {student} по предмету {class_} удалена оценка {mark}')
                        print(f'У {student} по предмету {class_} следующие оценки {students_marks[student][class_]}')
                    else:
                        print('ОШИБКА: Такой оценки нет у ученика')
                else:
                    print('ОШИБКА: неверное имя ученика или название предмета')
            elif command1 == 3:
                print('3. Редактировать оценку ученика по предмету')
                student = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    print(f'У {student} по предмету {class_} следующие оценки {students_marks[student][class_]}')
                    print()
                    mark = int(input('Введите оценку, которую нужно редактировать: '))
                    index = students_marks[student][class_].index (mark)
                    mark1 = int(input('Введите новую оценку: '))
                    students_marks[student][class_][index] = mark1
                    print(f'Для {student} по предмету {class_} изменена оценка {mark} на {mark1}')
                    print(f'У {student} по предмету {class_} следующие оценки {students_marks[student][class_]}')
                else:
                    print('ОШИБКА: неверное имя ученика или название предмета')
            elif command1 == 4:
                print('4. Выход в основное меню')
                break

    elif command == 2:
        print('''
        Список команд:
         1. Вывести средний балл по всем предметам по каждому ученику
         2. Вывести средний балл по всем предметам по определеннрму ученику
         3. Выйти в основное меню
                ''')
        while True:
            command2 = int(input('Введите команду: '))
            if command2 == 1:
                print('1. Вывести средний балл по всем предметам по каждому ученику')
                for student in students:
                    print(student)
                    for class_ in classes:
                        marks_sum = sum(students_marks[student][class_])
                        marks_count = len(students_marks[student][class_])
                        if marks_count == 0:
                            print(f'{class_} нет оценок')
                        else:
                            print(f'{class_} - {marks_sum // marks_count}')
                    print()
            elif command2 == 2:
                print('2. Вывести средний балл по всем предметам по ученику')
                student = input('Введите имя ученика: ')
                if student in students_marks.keys():
                    for class_ in classes:
                        marks_sum = sum(students_marks[student][class_])
                        marks_count = len(students_marks[student][class_])
                        if marks_count == 0:
                            print(f'{class_} нет оценок')
                        else:
                            print(f'{class_} - {marks_sum // marks_count}')
                    print()
            elif command2 == 3:
                print('3. Выход в основное меню')
                break

    elif command == 3:
        print('''
        Список команд:
         1. Вывести все оценки по всем ученикам
         2. Вывести все оценки ученика
         3. Выйти в основное меню
                        ''')
        while True:
            command3 = int(input('Введите команду: '))
            if command3 == 1:
                print('1. Вывести все оценки по всем ученикам')
                for student in students:
                    print(student)
                    for class_ in classes:
                        print(f'\t{class_} - {students_marks[student][class_]}')
                    print()
            elif command3 == 2:
                print('2. Вывести все оценки ученика')
                student = input('Введите имя ученика: ')
                if student in students_marks.keys():
                    for class_ in classes:
                        print(f'\t{class_} - {students_marks[student][class_]}')
                    print()
                else:
                    print('ОШИБКА: неверное имя ученика')
            elif command3 == 3:
                print('3. Выход в основное меню')
                break

    elif command == 4:
        print('''
        Список команд:
         1. Добавить нового ученика
         2. Удалить ученика из списка
         3. Редактировать имя ученика
         4. Список учеников
         5. Выйти в основное меню
                        ''')
        while True:
            command4 = int(input('Введите команду: '))
            if command4 == 1:
                print('1. Добавить нового ученика')
                student = input('Введите имя нового ученика: ')
                if student in students_marks.keys():
                    print('Ученик с таким именем уже есть')
                else:
                    print(f'Ученик {student} успешно добавлен в список')
                    students.append(student)
                    students.sort()
                    students_marks[student] = {}
                    for class_ in classes:
                        students_marks[student][class_] = []
            elif command4 == 2:
                print('2. Удалить ученика из списка')
                student = str (input('Введите имя ученика: '))
                if student in students_marks.keys():
                    students.remove(student)
                    del students_marks[student]
                    print(f'Ученик {student} успешно удален из списка')
                else:
                    print('Ученика с таким именем нет в списке')
            elif command4 == 3:
                print('3. Редактировать имя ученика')
                student1 = input('Введите имя ученика, которое необходимо измениить: ')
                if student1 in students_marks.keys():
                    student_new = input('Введите новое имя ученика: ')
                    students.remove(student1)
                    students.append(student_new)
                    students_marks[student_new] = students_marks.pop(student1)
                    print(f'Имя {student1} успешно изменено на {student_new}')
                else:
                    print('Ученика с таким именем нет в списке')
            elif command4 == 4:
                    print('4. Список учеников: ')
                    for student in students:
                        print(f'{student} ')
                    print()
            elif command4 == 5:
                print('5. Выход в основное меню')
                break

    elif command == 5:
        print('''
        Список команд:
         1. Добавить новый предмет
         2. Удалить предмет
         3. Редактировать название предмета
         4. Вывести список предметов
         5. Выйти в основное меню
               ''')
        while True:
            command5 = int(input('Введите команду: '))
            if command5 == 1:
                print('1. Добавить новый предмет')
                class_ = input('Введите название нового предмета: ')
                if class_ in students_marks[student].keys():
                    print('Предмет с таким названием уже есть')
                else:
                    print(f'Предмет {class_} успешно добавлен в список')
                    classes.append(class_)
                    for student in students:
                        students_marks[student][class_] = []
            elif command5 == 2:
                print('2. Удалить предмет')
                class_ = input('Введите название предмета: ')
                if class_ in students_marks[student].keys():
                    classes.remove(class_)
                    del students_marks[student][class_]
                    print(f'Предмет {class_} успешно удален ')
                else:
                    print('Предмета с таким названием нет')
            elif command5 == 3:
                print('3. Редактировать название предмета')
                print(classes)
                class_ = input('Введите название предмета, который необходимо измениить: ')
                if class_ in students_marks[student].keys():
                    class_new = input('Введите новое название предмета: ')
                    classes.remove(class_)
                    classes.append(class_new)
                    for student in students:
                        students_marks[student][class_new] = students_marks[student][class_]
                        del students_marks[student][class_]
                    print(f'Название предмета {class_} успешно изменено на {class_new}')

                else:
                    print('Предмета с таким названием нет')
            elif command5 == 4:
                    print('4. Изучаемые предметы: ')
                    for class_ in classes:
                        print(f'{class_} ')
                    print()

            elif command5 == 5:
                print('5. Выход в основное меню')
                break

    elif command == 6:
        print('6. Выход из программы')
        break
