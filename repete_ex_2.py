'''2) Modifique o programa anterior de maneira que o usuário
também digite o início e o fim da tabuada, ao invés de ir
de 1 a 10. Ex. Tabuada de: 2, início: 5, fim: 12.
Vai imprimir: 2 x 5 = 10, 2 x 6 = 12, ... 2 x 12 = 24.'''

tab = int(input("Tabuada? "))
ini = int(input("Início? "))
fim = int(input("Fim? "))

while ini <= fim :
    print(f"{tab} x {ini} = {tab*ini}")
    ini = ini + 1


    