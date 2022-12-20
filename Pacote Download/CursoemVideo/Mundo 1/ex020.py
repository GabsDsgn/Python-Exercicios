nome = str(input('Me diga qual é o seu nome: ')).strip()

print(
    f'Em maiúsculas: {nome.upper()}'
    f'\nEm minúsculas: {nome.lower()}'
)
print(
    'Quantas letras ao todo: {}'.format(len(nome)-nome.count(' '))
)
print(
    'Seu primeiro nome tem {} letras: '.format(nome.find(' '))
)
separa = nome.split(

)
print(
    f'Olá {separa[0]}'
)