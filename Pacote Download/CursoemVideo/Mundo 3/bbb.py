"""
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

# Programa Principal
soma(5, 7)
soma(b=7, a=5)
soma(7, 5)
#soma(5, 4, 7)
"""
"""
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')


# Programa Principal
contador(2, 1, 5)
contador(5, 6, 8, 0, 10)
"""
"""
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
"""
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 3)
soma(9, 4, 3)
