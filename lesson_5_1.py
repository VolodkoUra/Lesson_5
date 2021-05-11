import random
"""
Создать квадратную матрицу размерностью n 
и заполнить ее случайными значениями от 1 до 9
"""
n = int(input("Введите размерность матрицы: "))
for i in range(n):
    for j in range(n):
        res = random.randint(1, 9)
        print(res, end=" ")
    print()
