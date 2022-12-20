num = int(input('Escolha um numero para o inicio da PA: '))
constante = int(input('Insira o valor da constante: '))
decimo = num + (10 - 1) *constante
for c in range(num, decimo, constante):
    print(f'{c}', end=' > ')
print('ACABO')
