from random import randint
from time import sleep
from operator import itemgetter
jogo = {'p1': randint(1, 6),
        'p2': randint(1, 6),
        'p3': randint(1, 6),
        'p4': randint(1, 6)}
ranking = []
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('RANKING DOS JOGADORES')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
