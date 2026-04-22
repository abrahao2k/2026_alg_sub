"""
1) Ler uma temperatura em graus Celsius e
apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é F ← (9 * C + 160) / 5,
sendo F a temperatura em Fahrenheit e C a
temperatura em Celsius.
"""
c = float(input("Temperatura em Celsius: "))
f = (9 * c + 160) / 5
print(f"Temperatura em Fahrenheit: {f:.1f}")


