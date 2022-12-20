num1 = int(input(
    'Me informe um numero: '
))
num2 = int(input(
    'Me informe mais um numero: '
))
num3 = int(input(
    'Me informe outro numero: '
))
if num1 > num2 and num1 > num3:
    print(
        f'O primeiro numero é o maior, o numero {num1}'
    )
elif num2 > num3 and num2 > num3:
    print(
        f'O segundo numero é o maior, o numero {num2}'
    )
elif num3 > num2 and num3 > num1:
    print(
        f'O terceiro numero é o maior, o numero {num3}'
    )
if num1 < num2 and num1 < num3:
    print(
        f'O primeiro numero é o menor, o numero {num1}'
    )
elif num2 < num3 and num2 < num3:
    print(
        f'O segundo numero é o menor, o numero {num2}'
    )
elif num3 < num2 and num3 < num1:
    print(
        f'O terceiro numero é o menor, o numero {num3}'
    )