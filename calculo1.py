# Faça um programa que pergunta a quantidade
# de lugares em um teatro, depois pergunta
# a quantidade de ingressos vendidos
# e calcula quantos lugares vazios ainda
# restam no local.

lugares = int(input("Quantidade de lugares? "))
ingressos = int(input("Ingressos vendidos? "))
vazios = lugares - ingressos
print(f"Existem {vazios} lugares disponíveis.")

