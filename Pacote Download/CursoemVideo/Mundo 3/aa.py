"""
pessoas = {'nome': 'Gabs', 'sexo': 'M', 'idade': 22}
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')

////

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])

"""

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('UF: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
        