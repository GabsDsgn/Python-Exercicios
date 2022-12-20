# l1 = ['string', True, 4, -98.7]
# for x in l1:
#     print(f'O tipo de elemento é {type(x)} e seu valor é {x}')
#
#
# secreto = 'abcdef'
# digitadas = 'cde'
#
# for letra_secreta in secreto:
#     if letra_secreta in digitadas:
#         print(letra_secreta, 'está em', digitadas)
#     else:
#         print(letra_secreta, 'não está em', digitadas, '*')
#

secreto = 'caleidoscopio'
digitadas = []
chances = 3

print('--='*15)
print(
    '\033[7;40mOPA FALA AI MEU CONSAGRADO VAMO JOGA UM JOGO\033[m?'
)
print('--='*15)
print(
    '\nO jogo é o seguinte, tenho uma palavra secreta e você deve advinhar ela digitando cada letra até a formar, pronto?\n'
)

while True:
    if chances <= 0:
        print(
            'Você perdeu ;('
        )
        break

    letra = input(
        'Digite uma letra: '
    )
    if len(letra) > 1:
        print(
            'Aaah ai não vale, uma letra só por favor!'
        )
        continue
    if letra.isnumeric():
        print(
            'Uma letra mano, numero não conta.'
        )
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(
            f'AEEEE acertou, a letra {letra} ta certa!'
        )
    else:
        print(
            f'Infelizmente você errou!! A letra {letra} nao existe na frase.'
        )
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:

            secreto_temporario += letra_secreta

        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(
            f'Booa você me venceu, a palavra era {secreto}!'
        )
        break
    else:
        print(
            f'A palavra secreta está assim {secreto_temporario}'
        )
        if letra not in secreto:
            chances -= 1
    print(
        f'Você ainda tem {chances} chances!'
    )
