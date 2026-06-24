'''7) Escreva um programa que pergunta o valor inicial
de uma dívida, a taxa mensal de juros e o valor 
que será pago a cada mês. Informe o número de meses
necessários para quitar a dívida, o total pago 
e quanto de juros foi pago.'''
divida  = float(input("Dívida? "))
txjuros = float(input("Taxa de Juros? "))
parcela = float(input("Parcela? "))
pago  = 0
juros = 0
mes   = 0
while divida > 0 :
    if divida > parcela:
        pago = pago + parcela
        divida = divida - parcela     
        jurosmes = divida * (txjuros/100)
        juros = juros + jurosmes
        divida = divida + jurosmes
    else:
        pago = pago + divida
        divida = 0
    mes = mes + 1
print("Meses: ", mes)
print("Total: ", pago)
print("Juros: ", juros)