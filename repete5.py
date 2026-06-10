import time # biblioteca de tempo

# contagem regressiva de 10 até 0

# 1a parte - valor inicial
contagem = 10

# 2a parte - teste lógico
while contagem >= 0 :
    
    print(contagem)
    time.sleep(1)   # pausa de 1 segundo
    
    # 3a parte - incremento (mudança na variavel testada)
    contagem = contagem - 1

print("Foguete lançado!")

