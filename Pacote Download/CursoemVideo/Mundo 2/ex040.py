a1 = int(input(
    'Me diga um segmento: '
))
a2 = int(input(
    'Me diga mais um segmento: '
))
a3 = int(input(
    'Me diga outro segmento: '
))
if (a1+a2) > a3 and (a1+a3) > a2 and (a2+a3) > a1:
    print(
        'É possivel os tornar um triângulo!'
    )

    if a1 == a2 ==a3:
        print(
            'O triângulo é EQUILÁTERO'
        )
    elif a1 == a2 or a2 == a3 or a1 ==a3:
        print(
            'O triângulo é ISÓCELES'
        )

    else:
        print(
            'O triângulo é ESCALENO'
        )
else:print(
    'Não é possivel fazer um triângulo com esses ângulos!'
)
