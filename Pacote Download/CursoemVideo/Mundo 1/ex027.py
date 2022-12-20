velocidade = int(input(
    'Qual era a velocidade do seu carro em Km/h? '
))
multa = (velocidade - 80)*7
if 80 < velocidade:
    print(
        f'Seu carro foi multado em R${multa}, ande mais devagar.'
    )
    if velocidade >= 120:
        print(
            'TA LOCO TIOZAO ACHA Q VAI VOAR É'
        )
else:print(
    'parabens vc está dentro do limite'
)