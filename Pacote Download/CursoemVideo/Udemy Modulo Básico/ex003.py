'''
O len serve como uma contagem de caracteres
Ps. ele tambem conta espaçamentos
'''

nome = str(input(
    'Vamos analisar seu nome, vamo la qual teu nome: '
))
if len(nome) >= 5 and len(nome) <= 8:
    print(
        f'Ok seu nome é comum'
    )
elif len(nome) <= 5:
    print(
        f'Ih alá mini nome KKK'
    )
else: print(
    f'Slc cachorro {nome} mó nome de bixao'
)