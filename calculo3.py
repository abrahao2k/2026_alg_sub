# crie um programa que pergunta a cotação
# atual do dolar.
# em seguida pergunta o valor em reais que
# o usuário deseja converter.
# calcule e mostre quantos dólares
# vale o dinheiro do usuário.

cotação = float(input("Cotação do dólar: "))
reais = float(input("Valor em Reais: "))
total = reais / cotação
print(f"Seu dinheiro vale {total:.2f} Dólares.")
