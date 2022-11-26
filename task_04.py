numbers = ["1", "2"]
data = open("text.txt", "r")


n = 5
array = []
for i in range(-n, n + 1):
    array.append(i)
print(array)

x = data.readline()
b = data.readline()
result = array[int(x)] * array[int(b)]
print(result)

