from random import randint
from time import sleep
lista = []
print('JOGA NA MEGA SENA')
quant = int(input('Quantos jogos vc quer que eu sorteie? '))
jogos = []
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 5, f' SORTEANDO {quant} JOGOS', '-=' * 5)
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')
    sleep(1)
