while True:

    nota1 = float(input('Digite sua nota no final do primeiro bimestre: '))
    nota2 = float(input('Digite sua nota no final deste bimestre: '))
    media = (nota1+nota2) / 2

    print(
        f'Tirando {nota1} e {nota2}, a média do aluno é {media}'
    )
    if media < 5:
        print(
            'O aluno foi REPROVADO!'
        )
        break
    elif 5 <= media <= 6.9:
        print(
            'O aluno está de RECUPERAÇÃO!'
        )
        break
    elif 7 <= media <= 10:
        print(
            'O aluno foi APROVADO!'
        )
        break
    else:
        print(
            'Por favor insira as notas certas.'
            )
        continue
