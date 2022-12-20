#
# logged_user = True
#
# if logged_user:
#     msg = 'Usuario Logado'
# else:
#     msg = 'Usuario deve logar'
#
# print(msg)

logged_user = True

msg = 'Usuario logado' if logged_user else 'Usuario deve logar'

print(msg)

idade = 17
e_maior = (idade >= 18)
msg2 = 'Pode acessar' if e_maior else 'Usuario não pode Logar'
print(msg2)

nome = input(
    'Digite seu nome: '
)

print(nome or 'Você nao digitou nada')