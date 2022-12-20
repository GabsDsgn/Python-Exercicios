"""
def conta(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols no campeonato')


conta(g=5)
"""""
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato')


n = str(input("Nome do Jogador: "))
g = str(input("Número de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
