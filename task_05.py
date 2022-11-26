from random import randint
n = int(input("Введите длину списка чисел от 1 до N   "))



array = []
for i in range(1, n + 1):
    array.append(i)
print(array)
for i in range(n):
    y = randint(0, n - 1)
    x = randint(0, n - 1)
    array[x], array[y] = array[y], array[x]
print("Перемешанный список : ", array)