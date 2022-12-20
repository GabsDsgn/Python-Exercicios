from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoa}ª nasceu: '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1

print(
    f'Ao todo tivemos {totmaior} pessoas maiores de idade'
    f'\nE tambem tivemos {totmenor} pessoas menores'
)
