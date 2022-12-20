num = input(
    'Opa fala ai meu consagrado, preciso de um número inteiro, me diga um: '
)

if not num.isnumeric():
    print(
        'O numero não é inteiro'
    )
else:
    num = int(num)
    if num % 2 == 0:
        print(
        'O número é par'
    )
    elif num % 2 != 0:
        print(
        'O número é ímpar'
    )

