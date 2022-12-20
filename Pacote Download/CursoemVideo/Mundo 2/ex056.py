from random import randint

num = randint(0,10)
resposta = int(input('Me diga qual foi o numero que eu pensei: '))
tentativas = 0

while resposta != num:
    resposta = int(input('Resposta errada, tente de novo: '))
    tentativas += 1

print(f'Acertou com {tentativas} tentativas, Párabens')
