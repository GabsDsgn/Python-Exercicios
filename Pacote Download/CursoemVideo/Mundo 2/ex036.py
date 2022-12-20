while True:

    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))

    if n1 > n2:
        print(
            f'O numero {n1} é MAIOR'
        )
    elif n2 > n1:
        print(
            f'O numero {n2} é MAIOR'
        )
    elif n1 == n2:
        print(
            'Os numeros são IGUAIS'
        )
    continue