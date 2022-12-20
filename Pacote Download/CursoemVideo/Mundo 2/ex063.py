resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
media = soma / quant
print(
    f'Você digitou {quant} numeros e a media entre eles é {media}'
    f'\nO maior foi {maior} e o menor foi {menor}'
)
