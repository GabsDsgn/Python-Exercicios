n = int(input('Escolha um numero inteiro:'))
nsoma = int(n+1)
nsub = int(n-1)
ndob = int(n*2)
ntrip = int(n*3)
nraiz = int(n**(1/2))
print(
      f'Certo o número é {n}, seu sucesor é {nsoma}, o antecessor é {nsub}, o dobro é {ndob},'
      f'o triplo é {ntrip}, e a raiz quadrada dele é {nraiz}'
      )

'''
 Eu poderia ter feito apenas com uma variavel, a variavel n, e na hora do codigo print em cada chaves eu colocaria, exemplo: {n+1}
O codigo poderia ter ficado assim
 print(
      f'Certo o número é {n}, seu sucesor é {n+1}, o antecessor é {n-1}, o dobro é {n*2},'
      f'o triplo é {n*3}, e a raiz quadrada dele é {n**(1/2)}'
      )
 Fazendo assim com que economizasse memoria do sistema
 A raiz quadrada pode ser feita dessa forma pow(n,(1/2)
'''