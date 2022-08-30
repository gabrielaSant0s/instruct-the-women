a = 10.15
b = 20.03

b = b-a
a = a+b
b = a-b

print(b)
print(a)


array = [7, 4, 8, 6, 9, 10, 8, 2, 4.6]

for elemento1 in range(0, len(array)):
    for i in range(elemento1+1, len(array)):
        if (array[elemento1] > array[i]):
            aux = array[elemento1]
            array[elemento1] = array[i]
            array[i] = aux

print(array)
