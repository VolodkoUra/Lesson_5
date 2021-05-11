import random
"""
Создать квадратную матрицу размерностью n и 
заполнить ее случайными значениями. Найти 
сумму всех элементов матрицы, которые кратны 3."""

n = int(input("Введите размерность матрицы: "))
result = 0
for i in range(n):
    for j in range(n):
        res = random.randint(1, 9)
        print(res, end=" ")
        if res % 3 == 0:
            result += res
    print()
print("Cумма всех чисел матрицы кратные 3: ", result)