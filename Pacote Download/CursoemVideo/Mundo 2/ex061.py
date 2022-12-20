termos = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
repeticao = 3
print(f'{t1} > {t2}', end='')
while repeticao < termos:
    t3 = t1 + t2
    print(f' > {t3}', end='')
    t1 = t2
    t2 = t3
    repeticao +=1
print(' > FIM')
