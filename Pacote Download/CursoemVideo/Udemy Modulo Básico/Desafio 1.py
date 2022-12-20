# contagem_progressiva = '!@#$%¨&*()'
# contagem_regressiva = ')(*&¨%$#@!'
# x = 0
# y = 0
# for valor in contagem_progressiva:
#     x += 1
#     print(x)
# for valor in contagem_regressiva:
#     y -= 1
#     print(y)

#SOLUÇÃO

for p, r in enumerate(range(10, 1, -1)):
    print(p,r)
