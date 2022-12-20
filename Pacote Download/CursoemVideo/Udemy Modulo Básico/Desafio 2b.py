from random import randint
novo_cpf = str(randint(10000000000, 99999999999))

    a1 = novo_cpf[:1]
    a1 = int(a1)
    a2 = novo_cpf[1:2]
    a2 = int(a2)
    a3 = novo_cpf[2:3]
    a3 = int(a3)
    a4 = novo_cpf[3:4]
    a4 = int(a4)
    a5 = novo_cpf[4:5]
    a5 = int(a5)
    a6 = novo_cpf[5:6]
    a6 = int(a6)
    a7 = novo_cpf[6:7]
    a7 = int(a7)
    a8 = novo_cpf[7:8]
    a8 = int(a8)
    a9 = novo_cpf[8:9]
    a9 = int(a9)
    u10 = novo_cpf[9:10]
    u10 = int(u10)
    u11 = novo_cpf[10:]
    u11 = int(u11)

    soma1 = (a1*10)+(a2*9)+(a3*8)+(a4*7)+(a5*6)+(a6*5)+(a7*4)+(a8*3)+(a9*2)
    formula1 = 11-(soma1 % 11)
    if formula1 > 9:
        digito_1 = 0
    else:
        digito_1 = formula1

    soma2 = (a1*11)+(a2*10)+(a3*9)+(a4*8)+(a5*7)+(a6*6)+(a7*5)+(a8*4)+(a9*3)+(digito_1*2)
    formula2 = 11-(soma2 % 11)
    if formula2 > 9:
        digito_2 = 0
    else:
        digito_2 = formula2

