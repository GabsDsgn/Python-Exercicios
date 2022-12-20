from datetime import date

ano = int(input('Digite sua data de nascimento: '))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print(
        f'Com {idade} anos Você é Mirim'
    )
elif idade <= 14:
    print(
        f'Com {idade} anos Você é Infantil'
    )
elif idade <= 19:
    print(
        f'Com {idade} anos Você é Júnior'
    )
elif idade <= 25:
    print(
        f'Com {idade} anos Você é Sênior'
    )
else:
    print(
        f'Com {idade} anos Você é Master'
    )
