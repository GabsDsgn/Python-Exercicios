usuario = str(input(
    'Nome de usuário: ')
)
senha = int(input(
    'Informe a senha: '
))
ubd = 'Gabietxt'
sbd = 123456

if usuario == ubd and senha == sbd:
    print(
        f'Você está logado!'
    )
else: print(
    f'Acesso negado, Usuário ou Senha incorretos!'
)