# TODAS AS TABUADAS DE MULTIPLICAÇÃO DE 1 ATÉ 10
tabuada = 1  #laço1 - valor inicial
while tabuada <= 10 : #laço1 - teste lógico
    
    numero = 1 #laço2 - valor inicial
    while numero <= 10 : #laço2 - teste lógico
        print(f"{tabuada} x {numero} = {tabuada*numero}")
        numero = numero + 1 #laço2 - incremento
    
    tabuada = tabuada + 1 #laço1 - incremento

