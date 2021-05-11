"""
Создать список учеников подобной структуры.
Определить средний балл оценок по всем предметам,
и вывести сведения о студентах, средний балл которых больше 4.
"""
pupils = [
    {
        'firstname': 'Masha',
        'Group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
    },
    {
        'firstname': 'Roma',
        'Group': 42,
        'physics': 3,
        'informatics': 4,
        'history': 2,
    },
    {
        'firstname': 'Toma',
        'Group': 42,
        'physics': 9,
        'informatics': 10,
        'history': 8,
    }
]

for i in pupils:
    result = 0
    j = 0
    for item, value in i.items():
        if item == 'physics' or item == 'informatics' or item == 'history':
           result+=value
           j +=1
    if (result/3) >=4:
        print("{} средний балл {}".format(i['firstname'], (result/3)))
