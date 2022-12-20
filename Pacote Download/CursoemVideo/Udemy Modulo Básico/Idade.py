nome = input(
    'Qual é o seu nome? '
)
idade = int(input(
    'Qual a sua idade? '
))

e = (idade > 17)

altura = float(input(
    'Qual a sua altura? ')
)
peso = float(input(
    'Qual é o seu peso? '
))
imc = peso/(altura**2)

print(
    f'Nome: {nome}'
    f'\n Idade: {idade}'
    f'\n É maior de idade: {e}'
    f'\n Altura: {altura}'
    f'\n Peso: {peso}'
    f'\n Seu imc é: {imc:.1f}'
)
# Calculo do imc = peso / (altura * altura)