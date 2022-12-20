from random import randint

n = (
    randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
)

print(
    f'Os valores sorteados foram ', end=' '
)

for cont in n:
    print(
        f'{cont}', end=' '
    )

print(
    f'\nO maior numero sorteado foi {max(n)}'
    f'\ne o menor foi {min(n)}'
)
