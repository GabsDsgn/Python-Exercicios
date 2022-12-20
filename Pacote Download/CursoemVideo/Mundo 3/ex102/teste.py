import moeda

p = float(input('Digite o preço: R$'))
print(
    f'A metade de R${moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}\n'
    f'O dobro de R${moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}\n'
    f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}'
)
