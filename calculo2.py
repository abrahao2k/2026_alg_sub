# Faça um programa que pergunta o
# preço da gasolina.
# Em seguida pergunta a quantidade de
# litros abastecidos.
# Calcule e mostre o total gasto.

# float

preço = float(input("Preço da gasolina? "))
litros = float(input("Quantidade de litros? "))
total = preço * litros
print(f"Valor a pagar R$ {total:.2f}")