maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input(f'Qual o peso da {pessoa}ª pessoa: '))

    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(
    f'O maior peso foi de {maior}'
    f'E o menor foi de {menor}'
)
