'''Escreva um programa que peça ao usuário para inserir números
inteiros positivos e os armazene em uma lista. O programa
deve continuar pedindo números até que o usuário insira
um número negativo. Em seguida, exiba a lista resultante.'''

lista = []  # lista vazia
numero = 0
while numero >= 0 :
    numero = int(input("Digite um número: "))
    if numero >=0 :
        lista.append(numero)

print(lista)
