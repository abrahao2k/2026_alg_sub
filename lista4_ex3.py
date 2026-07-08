'''3. Crie um programa que sorteie 10 números
entre 1 e 100 e guarde-os numa lista. Ordene 
a lista em ordem crescente e imprima na tela
os valores sorteados.'''

import random
numeros = []
cont = 1
while cont <= 10:
    sorteio = random.randint(1,100)
    numeros.append(sorteio)
    cont = cont + 1

numeros.sort() # ordena os valores
print(numeros)
