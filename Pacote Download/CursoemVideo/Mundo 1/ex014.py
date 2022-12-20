from math import  trunc


print(
    'Está na hora do Desafio!'
)

num = float(input(
    'Digite um numero decimal: '
))

#print(
#    f'O numero {num} tem sua porção inteira como {num:.0f}'
#)

print(
    f'O numero {num} tem sua porção inteira como {trunc(num)}'
)