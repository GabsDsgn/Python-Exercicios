"""
pessoa = []
cadastrados = []

pesado = 0
leve = 100000
npesados = []
nleves = []

num = int(input('Quantas pessoas serão cadastradas? '))

for c in range(0, num):
    nome = (str(input('Nome: ')))
    pessoa.append(nome)
    peso = (int(input('Peso: ')))
    pessoa.append(peso)
    cadastrados.append(pessoa[:])
    if peso > pesado:
        pesado = peso
        npesados.clear()
    elif peso == pesado:
        npesados.append(nome)
    elif peso < leve:
        leve = peso
        nleves.clear()
    elif peso == leve:
        nleves.append(nome)
    else:
        pass
    pessoa.clear()

print(f'Foram cadastrados assim no sistema (nome e peso respectivamente) {cadastrados} '
      f'\nO(s) mais pesado(s) com {pesado}kg, é(foram) {npesados} \nO(s) mais leve(s) com {leve}kg, é(foram) {nleves} ')
"""

temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Os dados foram {princ}')
print(f'Ao todo,  você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print(f'O menor peso foi de {men}Kg. Peso de', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end='')
