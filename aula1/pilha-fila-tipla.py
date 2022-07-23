# ultimo item da lista é o primeiro que sai
def pilha():
    array = [1, 2, 3]
    array.pop(2)
    print(array)
    array.pop(1)
    print(array)


pilha()


# fila só é possível remover os elementos do inicio e acrescentar elementos no final
def fila(array):
    print(array)
    array.append(4)
    array.pop(0)
    print(array)


fila([1, 2, 3])

# tupla - listas imutáveis, dados ordenados
tupla = (5, 6, 7)
print(tupla)
# tupla[0] = 2
# print(tupla)
