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

r = random.shuffle(lista)

print(
    'A ordem de apresentação será {}'.format(lista)
)