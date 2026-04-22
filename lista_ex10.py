"""10) O cardápio de uma lanchonete é dado abaixo.
Prepare um algoritmo que leia a quantidade de cada
item que você consumiu e calcule a conta final.

Hambúrguer................ R$ 13,00  
Cheeseburguer............... R$ 8,00  
Fritas..................... R$ 7,50  
Refrigerante............... R$ 6,90  
Milkshake................. R$ 23,00
"""

h = int(input("Quantidade de Hambúrguer: "))
c = int(input("Quantidade de Cheeseburguer: "))
f = int(input("Quantidade de Fritas: "))
r = int(input("Quantidade de Refrigetante: "))
m = int(input("Quantidade de Milkshake: "))

total = h*13 + c*8 + f*7.5 + r*6.9 + m*23

print(f"Total da conta: R$ {total}")
        