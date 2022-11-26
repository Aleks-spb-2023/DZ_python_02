a = float(input())
a = str(a)
summ = 0
while len(a) != 0:
    if a[-1].isdigit():
        summ += int(a[-1])
    a = a[:-1]
print(summ)