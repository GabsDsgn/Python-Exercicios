print('--='*11)
print(
    'Bem vindo ao cadastro do \033[7;40mHerói\033[m !!'
)
print('--='*11)

nome = str(input(
    'Qual é o seu nome? '
))

print(
    f'Certo {nome} vamos começar! '
)
ego = input(
    'Qual é o seu nome de héroi? '
)
ranks = input(
    'Qual é o seu rank de herói?'
    '\n Lista de ranks'
    '\n SS'
    '\n S'
    '\n A'
    '\n B'
    '\n C'
    '\n : '
)
if ranks.upper() == 'SS':
    print(
        'Ou tu é o bixão ou ta com o ego la em cima, vai descendo a bola ai parça!'
    )
elif ranks.upper() == 'S':
    print(
        'CARAI AI SIM PARÇA'
    )
elif ranks.upper() == 'A':
    print(
        'Nice já ta bemzao mano continua assim que tu chega a perfeição!'
    )
elif ranks.upper() == 'C':
    print(
        'ou tu é um merdão ou ta com a auto estima la em baixo, se anima campeão vc consegue!'
    )
else: pass
comida = input(
    'O que você mais gosta de comer? '
)
if comida.upper() == 'BUCETA' or comida.upper() == 'BUNDA' or comida.upper() == 'CU' or comida.upper() == 'PINTO' or comida.upper() == 'PIROCA' or comida.upper() == 'PAU' == comida.upper() == 'XERECA':
    print(
        'CALMA LA MEU COLEGA DEIXA DE SER SAFADO RAPAZ TOME TENTO, vai comer hamberg agora!'
    )
    comida = 'hamberg'
else: pass
classe = input(
    'Qual é o sua classe?'
    '\n Lista de classe'
    '\n Melee'
    '\n Ranged'
    '\n Mage'
    '\n Summoner'
    '\n : '
)

print(
    'Pois bem Senhor(a) aqui estão seus dados:'
    f'\nAlter-ego: {ego}'
    f'\nRank: {ranks}'
    f'\nO que mais gosta de comer: {comida}'
    f'\nClasse: {classe}'
)
