# Indice
#        0123456789.......................33
frase = 'O rato roeu a ropa do rei de roma'#Iterável
tamanho = len(frase)
contador = 0
nova_str = ''

input_do_usuario = input(
    'Qual letra você deseja tornar maiuscula? '
)
input_do_usuario = input_do_usuario.upper()

if input_do_usuario == 'ALL':
    frase = frase.upper()
else: input_do_usuario = input_do_usuario.lower()

#Iteração <- Iterar
while contador < tamanho:
    # print(frase[contador], contador)
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_str += input_do_usuario.upper()
    else:
        nova_str += letra
    contador += 1
    print(nova_str)
