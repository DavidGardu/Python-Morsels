'''
I'd like you to write a function that accepts two lists-of-lists 
of numbers and returns one list-of-lists with each of the 
corresponding numbers in the two given lists-of-lists added 
together.
'''
def suma(mat1, mat2):
    nuevo = []
    if len(mat1) == len(mat2):
        for i in range(len(mat1)):
            sumado = []
            for j in range(len(mat1[i])):
                sumado.append(int(mat1[i][j]) + int(mat2[i][j]))
            nuevo.append(sumado)
        return nuevo

a = [[3, 2], [0, 1], [2, 0]]
b = [[5, 4], [2, -1], [5, 9]]
print(suma(a, b))

'''
For the first bonus, modify your add function to accept and "add" 
any number of lists-of-lists.
'''

def suma_mul(*matrices):
    nuevo = []
    for filas in zip(*matrices):
        fila = []
        for valores in zip(*filas):
            total = 0
            for i in valores:
                total += i
            fila.append(total)
        nuevo.append(fila)
    return nuevo

a = [[3, 2], [0, 1], [2, 0]]
b = [[5, 4], [2, -1], [5, 9]]
c = [[3, 2], [-2, 8], [3, 6]]
print(suma_mul(a, b, c))