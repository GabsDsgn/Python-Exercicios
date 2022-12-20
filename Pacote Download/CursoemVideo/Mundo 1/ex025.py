n = str(input('Qual é o seu nome? ')).strip()
nome = n.split()
print(
    f'Seu nick name será: '
    f'\n{nome[0]} {nome[len(nome)-1]}'
)