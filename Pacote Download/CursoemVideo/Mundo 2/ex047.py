
"""
n = int(input('Insira um valor: '))
n2 = n
q = 0
for t in range(1, 11):
    q += 1
    print(f'O resultado de {n} vezes {q} é: ')
    n2 = n * q
    print(f'{n2}')
"""

num = int(input('Digite um numero: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num*c}')