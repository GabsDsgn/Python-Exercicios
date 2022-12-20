print('Progreção aritmetica')
print('-='*10)
termo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a Razão: '))
primeiro = termo
cont = 1
while cont <= 10:
    print(f'{primeiro} > ', end='')
    primeiro += razao
    cont += 1
print('FIM')
