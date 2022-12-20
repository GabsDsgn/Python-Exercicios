lista = [
    ['Joao', 'Bags', 'Lara'],
    ['zi', 'my', 'gi'],
    ['chiish', 'akio', 'nog'],
]

for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)

lista2 = ['joao', 'gabs', 'nogs',1,2,3,4,5,7,8,988887]

n1, n2, *outra_lista_sera_criada, ultimo_valor_da_lista_criada = lista2
print(n2, ultimo_valor_da_lista_criada)