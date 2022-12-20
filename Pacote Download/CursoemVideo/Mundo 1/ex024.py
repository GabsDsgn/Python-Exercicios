nome = str(input(
    'Qual é o Seu nome: '
)).strip().upper()

print(
    f'O nome {nome} tem {nome.count("A")} letra(s) "A" '
    f'\nO primeiro "A" aparece na posição {nome.find("A")+1} '
    f'\nO ultimo "A" aparece na posição {nome.rfind("A")+1}'
)
