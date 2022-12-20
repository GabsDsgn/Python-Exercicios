
'''
and: verdadeiro x verdadeiro = verdadeiro
or: verdadeiro x falso = verdadeiro
not serve para codigos do tipo
x = 0 ou x = ''
if not x:
    print(
    'preencha a variavel x'
    )
Assim que preenchida o if se dará por False
in = possui
not in = não possui
ex
'''

nome = str(input(
    'Qual é o seu nome?'
))
variavel = 'a'

if variavel in nome:
    print(
        f'Então {nome} possui a letra {variavel}!'
    )
else:
    print(
        f'{nome} não possui a letra {variavel}!'
    )