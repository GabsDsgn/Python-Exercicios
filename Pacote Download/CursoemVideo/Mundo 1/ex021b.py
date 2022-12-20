num = input(
    'Escolha um número de 0 a 9999: '
)
if not num.isnumeric():
    print(
        'Erro, insira um numero: '
    )

else:
    num = int(num)
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    if 0 > num or num > 9999:
        print(
            'O numero deve ser entre 0 e 9999: '
        )
    else:
        print(
        f'O numero {num} possui: '
        f'\n {m} Milhares'
        f'\n {c} Centenas'
        f'\n {d} Dezenas'
        f'\n {u} Unidades'
    )