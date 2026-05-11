''' faça um programa que pergunta quanto o
usuário ganha, depois pergunta quanto o usuário
gasta. calcule o SALDO e diga se está
'dentro do orçamento' se a diferença for zero ou mais,
e diga 'fora do orçamento' se a diferença for negativa.'''

salario = float(input("Digite o salário: "))
gastos  = float(input("Digite os gastos: "))

saldo = salario - gastos
print(f"Saldo: R$ {saldo}")

if saldo >= 0 :
    print("Dentro do orçamento")
else:
    print("Fora do orçamento")





