import random
"""
Написать игру. Пользователь должен угадать число.
Сперва вводиться диапазон угадывания. После колличество попыток.
В случае правильного ответа - выводить You are the winner.
В случае неправильного давать игроку подсказку(больше или меньше искомое число).
Если за указанное количество попыток число не угадано - выводить:
You are the loser и правильное число
"""
print("Введите диапазон чисел!!!")
x = int(input("Введите первое число диапазона: "))
y = int(input("Введите второе число диапазона: "))
n = int(input("Введите количество попыток: "))
winner = random.randint(x, y)

i = 1
while i <= n:
    l = int(input("Испытай удачу! Введи число: "))
    if l == winner:
        print("You are the winner")
        n +=1
        break
    elif l > winner:
        print("Необходимое число меньше!")
        n +=1
    elif l < winner:
        print("Необходимое число больше!")
        n += 1
    else:
        print("You are the loser")