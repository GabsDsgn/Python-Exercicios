valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print(f'Voce digitou {len(valores)} elementos. ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O numero 5 está dentro da lista')
else:
    print('O numero 5 não foi encontrado na lista')
