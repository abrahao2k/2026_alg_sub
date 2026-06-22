'''6) Escreva um programa que pergunta o valor de depósito
inicial para uma poupança, e a taxa de rendimento mensal.
Apresente o saldo dos próximos 24 meses, considerando o
rendimento sobre o saldo atual de cada mês.'''

saldo = float(input("Depósito inicial: "))
taxa  = float(input("Taxa de rendimento: "))

cont = 1
while cont <= 24:
    rend = saldo * (taxa/100)
    saldo = saldo + rend
    print(cont, " = R$", saldo)
    cont = cont + 1

