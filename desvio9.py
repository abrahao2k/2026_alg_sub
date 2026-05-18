''' faça um programa que pergunta
um sabor de sorvete. se for morango
ou chocolate, mostre a mensagem
"TEMOS ESSE SABOR", para qualquer outro
mostre "ESTÁ FALTANDO" '''

sabor = input("Qual o sabor desejado? ")

if sabor == "morango" or sabor == "chocolate":
    print("Temos esse sabor.")
else:
    print("Está faltando.")
    
