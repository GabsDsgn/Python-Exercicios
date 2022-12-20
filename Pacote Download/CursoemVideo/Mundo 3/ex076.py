lista = []
pares = []
impares = []

while True:
    lista.append(int(input("Digite um numero: ")))
    resp = str(input("Quer continuar? [S/N]"))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {lista} \nA lista de pares é {pares} \nA lista de impares é {impares}')
