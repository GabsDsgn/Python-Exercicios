while True:

    preco = float(input('Valor das compras R$'))
    print('METÓDOS DE PAGAMENTO'
          '\n[ 1 ] à vista dinheiro/cheque'
          '\n[ 2 ] à vista cartão'
          '\n[ 3 ] 2x no cartão'
          '\n[ 4 ] 3x ou mais no cartão')
    mpg = input('Qual é a opção: ')

    if not mpg.isnumeric():
        print('Por favor Insira um número')
        continue

    mpg = int(mpg)

    if mpg == 1:
        preco2 = preco - (preco * 0.1)
    elif mpg == 2:
        preco2 = preco - (preco * 0.05)
    elif mpg == 3:
        preco2 = preco
    elif mpg == 4:

        np = input('Quantas parcelas?')

        if not np.isnumeric():
            print('Por favor Insira um número')
            continue

        np = int(np)

        if np <= 2:
            preco2 = preco
            parcelas = preco2 / np

            print(f'Sua compra será parcelada em {np}x de R${parcelas} SEM JUROS')
        elif np > 2:

            preco2 = preco + (preco * 0.2)

            parcelas = preco2 / np

            print(f'Sua compra será parcelada em {np}x de R${parcelas} COM JUROS')
            break

    else:
        print('por favor insira um numero valido!')
        continue

print(
    f'Sua compra de R${preco} vai custar R${preco2} no final.'
)
