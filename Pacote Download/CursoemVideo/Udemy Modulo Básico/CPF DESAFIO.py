while True:

    cpf = str(input(
        'Digite o CPF para a verificação: '
    ))
    novo_cpf = cpf[:-2]  # cpf sem os ultimos digitos
    total = 0  # total usado no algoritmo
    reverso = 10

    for c in range(19):  # por que 19? pq no algoritmo são feitas 19 multiplicações
        if c > 8:  # isso vai fazer com q o contador vá de 0 a 9
            c -= 9

        total += int(novo_cpf[c]) * reverso  # o total vai ser multiplicado pelo numero do algoritmo

        reverso -= 1
        if reverso < 2:  # aqui vai ser feito o primeiro e o segundo digito
            reverso = 11
            digito = 11 - (total % 11)  # algoritmo de cpf

            if digito > 9:
                digito = 0
            total = 0  # da um reset no total para o 2º digito
            novo_cpf += str(digito)  # concatena o primeiro e o segundo digito no cpf

    if cpf == novo_cpf:
        print('VALIDO')
    else:
        print('INVALIDO')
