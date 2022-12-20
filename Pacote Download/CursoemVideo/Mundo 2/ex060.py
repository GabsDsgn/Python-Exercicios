print('Progreção aritmetica')
print('-='*10)
termo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a Razão: '))
primeiro = termo
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{primeiro} > ', end='')
        primeiro += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar: '))
print(f'PA finalizada com {total} termos mostrados')
