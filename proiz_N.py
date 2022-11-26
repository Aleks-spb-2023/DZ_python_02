multiplier = 1
n = int(input())
array = []
for i in range(1,n + 1):
    array.append(multiplier * i)
    multiplier = multiplier * i
print(array)