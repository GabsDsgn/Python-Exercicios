secreto = 'abcdef'
digitadas = 'cde'

for letra_secreta in secreto:
    if letra_secreta in digitadas:
        print(letra_secreta, 'está em', digitadas)
    else:
        print(letra_secreta, 'não está em', digitadas, '*')
