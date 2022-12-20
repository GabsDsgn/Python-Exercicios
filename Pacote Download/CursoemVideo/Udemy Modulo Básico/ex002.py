h = input(
    'Olá que horas são? (por favor digite em numeros inteiros): '
)

h = int(h)

if 0 <= h <= 5:
    print(
        'Vai dormir meu parça ta tarde!'
    )
elif 6 <= h <= 12:
    print(
        'Bom dia meu amigo, vamo acordar!!'
    )

elif 13 <= h <= 18:
    print(
        'Boa tarde!!'
    )
elif 19 <= h <= 23:
    print(
        'Boa noite gafanhoto, até amanhã!'
    )