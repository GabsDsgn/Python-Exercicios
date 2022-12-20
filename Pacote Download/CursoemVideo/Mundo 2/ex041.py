print('Vamos calcular seu Indice de Massa Corporal')
massa = float(input('Por favor insira seu peso(kg): '))
altura = float(input('Digite sua altura: '))

imc = massa / (altura*altura)

if imc < 18.5:
    print('Você está abaixo do peso, consulte um nutricionista'
          f'imc = {imc:.2f}')
elif 18.5 <= imc < 25:
    print('Você está com o imc ideal :)'
          f'imc = {imc:.2f}')
elif 25 <= imc < 30:
    print('Você está com sobrepeso, consulte um nutricionista'
          f'imc = {imc:.2f}')
elif 30 <= imc < 45:
    print('Você já está classificado como obesidade , por favor consulte um nutricionista!'
          f'imc = {imc:.2f}')
else:
    print('Você já está em um nivel morbido de obesidade, consulte um nutricionista ou haverá sérias consequencias!'
          f'imc = {imc:.2f}')
