'''Escreva um programa que pergunta qual a melhor escola 
de Mossoró. Se o usuário responder IFRN, diga que 
acertou, se for outra escola, diga que errou.'''

escola = input("Qual a melhor escola? ")

#if escola.lower() == "ifrn" : # letras minúsculas
#    print("Você acertou.")

if escola.upper() == "IFRN" :  # letras maiúsculas
    print("Você acertou.")
else:
    print("Errrroooouuuuuu.")

