d = int(input(
    'O carro foi alugado por quantos dias? '
              ))
km = float(input(
    'Quantos Km rodados? '
))
p = float((d*60)+(km*0.15))
print(
    f'O total a pagar é R${p:.2f}'
)

# Calculo feito baseado em R$60 por dia e R$0,15 por km rodado
