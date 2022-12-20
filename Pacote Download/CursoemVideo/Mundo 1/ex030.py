ano = int(input(
    ' Me diga um ano: '
))
anob = ano % 4
if anob == 0:
    print(
        'O ano é bissexto!'
    )
else:
    print(
        'O ano não é bissexto!'
    )