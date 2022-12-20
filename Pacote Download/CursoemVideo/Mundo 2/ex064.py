soma = 0
valores = 0

while True:
    n = int(input('Digite um numero (999 para parar): '))

    if n != 999:
        soma += n
        valores +=1
        continue
    else:
        break

print(
    f'A soma de {valores} valores é {soma}'
)
