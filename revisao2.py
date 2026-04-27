''' 2. Faça um programa que pergunta o valor de 
uma compra, e quanto dinheiro foi dado (maior).
Calcule e mostre o troco do cliente. '''

valor_compra = float( input("Valor da compra: ").replace(',','.'))
dinheiro = float( input("Dinhero pago: ").replace(',','.'))
print(f"Troco: R$ {(dinheiro - valor_compra):.2f}")



