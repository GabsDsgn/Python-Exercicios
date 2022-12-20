import random
"""
r = randint(0,3)

if r == 1:
    r = 'pedra'
elif r == 2:
    r = 'papel'
elif r == 3:
    r = 'tesoura'
"""

pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
lista = [pedra, papel, tesoura]

r = random.choice(lista)

print('Vamos jogar jokempô!'
      '\n[ 0 ] PEDRA'
      '\n[ 1 ] PAPEL'
      '\n[ 2 ] TESOURA')
jogador = int(input('Qual sua opção: '))

if jogador == 0:
    if r == pedra:
        print('Empate! Pedra x Pedra')
    elif r == papel:
        print('O computador Venceu! Pedra x Papel!')
    else:
        print('O jogador Venceu! Pedra x Tesoura')
elif jogador == 1:
    if r == pedra:
        print('O jogador Venceu! Papel x Pedra')
    elif r == papel:
        print('Empate! Papel x Papel')
    else:
        print('O computador Venceu! Papel x Tesoura!')
else:
    if r == pedra:
        print('O computador Venceu! Tesoura x Pedra')
    elif r == papel:
        print('O jogador venceu! Tesoura x Papel')
    else:
        print('Empate! Teroura x Tesoura')
