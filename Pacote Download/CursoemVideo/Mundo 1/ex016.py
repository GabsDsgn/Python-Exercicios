from math import sin, cos, tan, radians
angulo = float(input(
    'Me diz um ângulo que você deseja : '
))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print(
    f'O ângulo {angulo} tera como:\n'
    f'Seno = {seno:.2f}\n'
    f'Cos = {cos:.2f}\n'
    f'tan = {tan:.2f}'
)

