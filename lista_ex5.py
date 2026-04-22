"""
5) Ler o valor correspondente ao salário mensal
(variável SM) de um trabalhador e também o valor
do percentual de reajuste (variável PR) a ser
atribuído. Apresentar o valor do novo salário
(variável NS).
"""

sm = float(input("Salário Mensal: "))
pr = float(input("Percentual de Reajuste: "))
ns = sm + (sm * pr / 100)
print(f"Novo salário = R$ {ns:.2f}")