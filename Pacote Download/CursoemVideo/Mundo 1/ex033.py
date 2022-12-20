a1 = int(input(
    'Me diga um ângulo: '
))
a2 = int(input(
    'Me diga mais um ângulo: '
))
a3 = int(input(
    'Me diga outro ângulo: '
))
if (a1+a2) > a3 and (a1+a3) > a2 and (a2+a3) > a1:
    print(
        'É possivel os tornar um triângulo!'
    )
else:print(
    'Não é possivel fazer um triângulo com esses ângulos!'
)