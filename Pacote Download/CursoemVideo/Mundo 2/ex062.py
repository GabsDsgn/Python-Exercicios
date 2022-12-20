n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input(
        'Digite um numero: '
    ))
    if n == 999:
        break
    cont += 1
    soma += n
print(
    f'Você digitou {cont} numeros e a soma é igual a {soma}'
)
