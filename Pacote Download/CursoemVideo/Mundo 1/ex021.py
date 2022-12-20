num = input(
    'Escolha um número de 0 a 9999: '
)
n = str(num)
if not num.isnumeric():
    print(
        'Erro, insira um numero: '
    )

else:
    num = int(num)
    if 0 > num or num > 9999:
        print(
            'O numero deve ser entre 0 e 9999: '
        )
    else:
        print(
        f'O numero {num} possui: '
        f'\n {n[:1]} Milhares'
        f'\n {n[1:2]} Centenas'
        f'\n {n[2:3]} Dezenas'
        f'\n {n[3:]} Unidades'
    )