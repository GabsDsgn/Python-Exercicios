'''
While lê se por enquanto
'''
x = 0
y = 0
'''
while x < 10:
    x += 1
    print(x)
'''

print('Acabou')

while True:
    num_1 = input(
        'Digite um numero: '
    )
    num_2 = input(
        'Digite um numero: '
    )
    operador = input(
        'Digite um operador: '
    )
    sair = input(
        'Deseja sair? [s]im [n]ão: '
    )
    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um numero.')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)
    #(+,-,/,*)
    if operador == '+':
        print('O resultado é', num_1+num_2)
    if operador == '-':
        print('O resultado é', num_1-num_2)
    if operador == '/':
        print('O resultado é', num_1/num_2)
    if operador == '*':
        print('O resultado é', num_1*num_2)

