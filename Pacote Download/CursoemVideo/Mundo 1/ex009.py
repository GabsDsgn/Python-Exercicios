
print(
    'Extra, Extra, todos os produtos da prateleira X estão com 5% de desconto!!!'
)

v = float(
    input('Qual o valor do produto R$:')
)

d = float(v*0.05)

vf = v-d
print(
    f'Certo o produto que antes era R${v:.2f},está com o desconto de R${d:.2f} e agora estará custando R${vf:.2f} aproveite!!'
)