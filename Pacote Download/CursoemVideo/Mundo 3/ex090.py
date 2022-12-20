"""
def calcA():
    print('-='*30)
    print('AREA DO QUADRILÁTERO')
    l = float(input('Digite o valor da largura: '))
    c = float(input('Digite o valor do comprimento: '))
    a = c * l
    print(f'A área do quadrilátero de lado {l:2f} e {c:2f} é {a:2f}')


# Programa Principal

calcA()
"""
def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg}x{comp} é de {a}m2.')

print(' Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
