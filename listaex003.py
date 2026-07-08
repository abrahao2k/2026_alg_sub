'''Exercício 3: Nomes em uma Lista 
Peça ao usuário para inserir nomes em uma lista usando um
loop "while". Continue pedindo nomes até que o usuário
insira a palavra "fim". Em seguida, exiba a lista de 
nomes. '''

nomes = list()  # lista vazia

while True:
    nome = input("Digite um nome: ")
    
    if nome.lower() == "fim":
        break
    
    nomes.append(nome)

print(nomes)