import random

a1 = str(input(
    'Primeiro aluno: '
))
a2 = str(input(
    'Segundo aluno: '
))
a3 = str(input(
    'Terceiro aluno: '
))
a4 = str(input(
    'Quarta pessoa: '
))
lista = [a1, a2, a3, a4]

r = random.choice(lista)

print(
    f'O sorteado para apagar o quadro é {r}, meus parabens kkkk'
)
