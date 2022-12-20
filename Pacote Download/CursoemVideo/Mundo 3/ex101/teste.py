from ex101 import moeda

p = float(input('Digite o preço: R$'))
print(
    f'A metade de R${p} é {moeda.metade(p)}\n'
    f'O dobro de R${p} é {moeda.dobro(p)}\n'
    f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}'
)
