veiculos = []  # lista vazia

while True:
    modelo = input("Digite o modelo: ")
    cor = input("Digite a cor: ")
    ano = input("Digite o ano: ")
    
    veiculos.append([modelo,cor,ano])
    
    resposta = input("Cadastrar outro? (s/n) ")
    if resposta == 'n':
        break

print(veiculos)

