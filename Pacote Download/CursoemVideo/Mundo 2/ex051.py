frase = str(input('Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não temos um palindromo')
