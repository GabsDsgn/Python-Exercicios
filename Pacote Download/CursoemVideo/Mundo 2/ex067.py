maior = 0
home = 0
molhe = 0


while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    if idade > 18:
        maior += 1
    if sexo == 'M':
        home += 1
    if sexo == 'F':
        if idade < 20:
            molhe += 1

    f = str(input('Quer continuar? [S/N] ')).upper()
    if f == 'S':
        continue
    else:
        break

print(f'Total de pessoas maiores de idade {maior}'
      f'\nTemos {home} homens cadastrados.'
      f'\nTemos um total de {molhe} mulheres com menos de 20 anos.')
