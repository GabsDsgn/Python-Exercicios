print("Welcome to Gabie's real states")

valor_casa = int(input('Digite o valor da casa: '))
tempo = int(input('Diga em quantos anos você irá pagar a casa: '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Quantos anos você tem? '))
valor_prestacao = valor_casa / (tempo*12)
porcentagem = salario * 0.3

print(f'Para pagar uma casa de R${valor_casa} em {tempo}anos a prestação será de {valor_prestacao:.2f}')
if valor_prestacao > porcentagem:
    print(
        'Não autorizado você é pobre!!'
    )
elif anos+tempo > 70:
        print(
        'Não autorizado você irá demorar muito tempo até pagar tudo. '
    )
else:
    print('Parabens Concedido!')