"""
print('oi')
print('oi')
print('oi\n')

for c in range(1, 4):
    print('oi')
print('FIM\n')

for cu in range(1, 5):
    print(cu)

for cum in range(5, 0, -1):
    print(cum)

for cumm in range(0, 6, 2):
    print(cumm)


inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for c in range(inicio, fim+1, passo):
    print(c)
"""

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório dos valores é igual a {s}')
