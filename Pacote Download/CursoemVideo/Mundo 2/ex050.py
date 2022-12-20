num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m')
        tot += 1
    else:
        print('\033[m')
    print(f'{c} ', end='')
print(f'\n\033[m0 numero {num} foi divisivel {tot} vezes')

if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')
    