sl = float(input(
    'Opa eae meu bom, você terá um aumento de salário devido aos seus esforços.'
    '\nPoderia me informar o seu salário atual? '
))
if sl >= 1250:
    au = sl * 0.1
    sl2 = sl+au
    print(
        f'Seu salário de R${sl} será de R${sl2}, parabens! '
    )
else:
    au = sl *0.15
    sl2 = sl+au
    print(
        f'Seu salário de R${sl} será de R${sl2}, parabens! '
    )