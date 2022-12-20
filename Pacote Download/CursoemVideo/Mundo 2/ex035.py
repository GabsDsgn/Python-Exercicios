n = int(input('Digite um numero inteiro: '))
opcao = int(input('[ 1 ] converter para BINÁRIO'
                  '\n[ 2 ] converter para OCTAL'
                  '\n[ 3 ] converter para HEXADECIMAL'
                  '\n Sua opção: '))

if opcao == 1:
    print(
        f'Conversão de {n} em inteiro para binário é {bin(n)}'
    )
elif opcao == 2:
    print(
        f'Conversão de {n} em inteiro para octal é {oct(n)}'
    )
elif opcao == 3:
    print(
        f'Conversão de {n} em inteiro para hexadecimal é {hex(n)}'
    )
else:
    print('Caractere inválido')