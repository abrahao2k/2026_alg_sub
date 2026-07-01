lista = [] # lista vazia

while True:
    info = input("Digite a informação: ")
    lista.append(info)
    res = input("Digitar outro? (s/n) ")
    if res == 'n' :
        break

print(lista)