''' 4. Crie um programa que calcula e mostra o IMC
(índice de massa corporal). O programa pergunta o
peso e a altura da pessoa e usa a formula
IMC = peso / altura ² '''

peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / altura ** 2
print("IMC = ", imc)

if imc <= 18 : print("Abaixo do peso")
elif imc <= 24 : print("Peso normal")
else: print("Acima do peso")
