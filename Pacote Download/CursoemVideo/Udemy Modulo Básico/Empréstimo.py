
nome = input(
    'Qual é o seu nome? '
)

idade = int(input(
    'Qual é a sua idade?'
))
idade_minima = 24
idade_maxima = 45

if idade >= idade_minima and idade <= idade_maxima:
    print(
        f'{nome} pode pegar o empréstimo'
    )
elif idade < idade_minima:
    print(
        f'{nome} infelizmente é muito novo para o empréstimo'
    )
else: print(
    f'Infelizmente o(a) senhor(a) {nome} tá caducando já, ta querendo empréstimo pra que doido kkkk'
)