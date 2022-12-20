def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco *taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-='*30)
    print('RESUMO DO VALOR'.center(30))
    print('-=' * 30)
    print(
        f'Preço analizado: \t{moeda(preco)}\n'
        f'Dobro do preço: \t{dobro(preco, True)}\n'
        f'Metade do preço: \t{metade(preco, True)}\n'
        f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}\n'
        f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}'
    )
    print('-=' * 30)
