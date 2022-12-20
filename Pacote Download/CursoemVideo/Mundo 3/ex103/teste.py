import moeda

p = float(input('Digite o preço: R$'))
print(
    f'A metade de R${moeda.moeda(p)} é {moeda.metade(p, True)}\n'
    f'O dobro de R${moeda.moeda(p)} é {moeda.dobro(p, True)}\n'
    f'Aumentando 10%, temos R${moeda.aumentar(p, 10, True)}'
)
