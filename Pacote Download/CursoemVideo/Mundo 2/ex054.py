media = 0
maior = 0
molheres = 0
nome_do_veio = ''
for pessoa in range(1, 6):
    print(f'{pessoa} PESSOA')
    nome = input(f'Qual o nome da {pessoa}ª pessoa: ')
    idade = int(input(f'Qual a idade: '))
    media += idade
    sexo = input('Sexo [F/M]: ')
    if idade == 1:
        maior = idade

    elif idade > maior:
        maior = idade
        nome_do_veio = nome
    elif sexo == 'F':
        if idade < 20:
            molheres += 1

mf = media / 5
print(
    f'A média de idade é {mf} anos'
    f'\na pessoa mais velha se chama {nome_do_veio} e tem {maior} anos'
    f'\nhá {molheres} mulheres com menos de 20 anos'
)
