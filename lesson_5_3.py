"""
Дана целочисленная матрица А[n,m].
Посчитать количество элементов матрицы,
превосходящих среднее арифметическое значение
элементов матрицы и сумма индексов которых четна.
"""
matrix = [[3, 5, 1, 8], [2, 9, 6, 7], [2, 4, 6, 8]]
res = 0
ind = 0
for index, value in enumerate(matrix):
    for i, j in enumerate(value):
        ind += 1
        res += j

arifm = res/ind
print(arifm)

t = 0
for x, y in enumerate(matrix):
    for i, j in enumerate(y):
        if j > arifm and (x + i) % 2 ==0:
            print(j)
            t +=1
print(t)



