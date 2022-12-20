import math

print(
    'Temos um triângulo retângulo! '
)

co = float(input(
    'Qual é o valor do cateto oposto? '
))

ca = float(input(
    'E o valor do cateto adjacente? '
))

#h = (co**2 + ca**2)**(1/2)
    #calculo manual ^
h = math.hypot(co, ca)

print(
    f'Levando em consideração o cateto oposto como {co} e o adjacente como {ca}, logo, a hipotenusa será {h:.0f}!'
)
