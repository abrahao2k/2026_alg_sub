'''Faça um programa que pergunta a idade do usuário
se for < 12 anos, diga que é criança,
se for < 18 anos, diga que é adolescente
outro valor, diga que é adulto. '''

idade = int(input("Digite a idade: "))

if   idade < 12 : print("Criança")
elif idade < 18 : print("Adolescente")
else            : print("Adulto")

