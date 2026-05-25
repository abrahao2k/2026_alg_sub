v1 = int(input("Primeiro valor: "))
v2 = int(input("Segundo valor: "))
op = input("Operação? +, -, *, / : ")

if   op == "+" : print("Soma =", v1+v2)
elif op == "-" : print("Subtração =", v1-v2)
elif op == "*" : print("Multiplicação =", v1*v2)
elif op == "/" : print("Divisão =", v1/v2)
else           : print("Operador inválido.")


'''
if op == "+" :
    print("soma...")
else:
    if op == "-":
        print("subtração...")
    else:
        if op == "*":
            print("multiplicação...")
        else:
            if op == "/":
                print("divisao...")
            else:
                print("operador inválido.")
'''