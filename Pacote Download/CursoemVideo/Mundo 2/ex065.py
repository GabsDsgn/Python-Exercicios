while True:

    num = int(input('Quer ver a tabuada de qual valor: '))
    if num < 0:
        print('Processo de tabuada encerrado.')
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    continue
