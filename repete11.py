# BREAK - FINALIZA O LAÇO IMEDIATAMENTE
# o laço aceita digitação de valores entre 0 e 9
# qualquer outro valor, finaliza o laço
while True:
    numero = int(input("Digite um número entre 0 e 9: "))
    
    if 0 <= numero <= 9 :
        print("Valor aceito.")
    else:
        break  # break - finaliza imediatamente
    
    print("---------------------")


