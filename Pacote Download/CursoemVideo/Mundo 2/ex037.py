ano = int(input('Digite sua data de nascimento: '))
idade = 2022 - ano

print(
    f'Quem nasceu em {ano} terá {idade} anos em 2022!'
)
if idade > 100:
    print(
        'Por favor insira sua verdadeira data de nascimento.'
    )

elif idade == 18:
    print(
        f'Por ter {idade} anos deverá se alistar no exercito IMEDIATAMENTE!'
    )
elif idade < 18:
    print(
        f'Você é novo demais e não precisa se alistar.'
    )
else:
    print(
        f'Seu alistamento já deveria ter ocorrido a {idade-18} anos!'
    )
