tot = totmil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Qual o nome do produto: '))
    preco = float(input('Qual é o preço do produto: '))
    tot += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break

print(f'O total da compra foi R${tot:.2f}'
      f'\ntemos {totmil} produtos custando mais de mil reais'
      f'\nO produto mais barato foi {barato} que custa R${menor:.2f}')
