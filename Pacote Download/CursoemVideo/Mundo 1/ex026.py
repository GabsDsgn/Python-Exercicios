import random
"""
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista = [n1, n2, n3, n4, n5]
r = random.choice(lista)
"""
r = random.randint(0,5)
resposta = int(input(
    'O numero sorteado foi: '
))
if resposta == r:
    print(
        'Cacete você é pica, acertou mizeravi'
    )
else:
    print(
        f'burrão nunca acreditei, pensei em {r}'
          )