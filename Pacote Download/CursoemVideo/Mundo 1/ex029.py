km = int(input(
    'Ih qual foi, o molecote vai dar uma viajada, vai é simbora daq, me fala ai quantos km a distancia até la: '
))
viaje_curta = km*0.5
viaji_longa = km*0.45
if km > 200:
    print(
        f'O preço da tua viaji vai se R${viaji_longa}'
    )
else:
    print(
        f'O preço da tua viaji vai ser R${viaje_curta}'
    )