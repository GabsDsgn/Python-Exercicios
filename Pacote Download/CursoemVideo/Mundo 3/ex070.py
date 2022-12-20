while True:

    cont = (
        'zero', 'um', 'dois', 'tres', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'douze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte'
            )
    while True:
        num = int(
            input(
                'Digite um numero ente 0 e 20: '
            )
        )
        if 0 <= num <= 20:
            break
        print('tente novamente', end=' ')

    print(
        f'Você digitou o numero {cont[num]}'
    )
    resp = input(
        'Você quer continuar? [S/N] '
    )
    if resp.upper() == 'S':
        continue
    else:
        break

print(
    'PROCESSO FINALIZADO'
)
