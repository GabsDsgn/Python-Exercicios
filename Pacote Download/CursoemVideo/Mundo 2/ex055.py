sexo = str(input('Informe o seu sexo: ')).strip().upper()

while sexo not in 'MmFf':
    sexo = str(input('Inválido, insira seu sexo: '))

print(
    'Acabou'
)
