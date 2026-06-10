# jogo de adivinhar o número
import random   # biblioteca de números aleatórios
sorteado = random.randint(1,100)  # inteiro aleatório entre 1 e 100
tentativas = 0
numero = 0

while numero != sorteado:
    numero = int(input("Digite um número: "))
    tentativas = tentativas + 1
    
    if numero == sorteado:
        print("Parabéns, você acertou.")
        print(f"Demorou {tentativas} rodadas.")
    
    elif numero > sorteado :
        print("Número muito alto.")
        print("Tente um número MENOR.")
    
    elif numero < sorteado :
        print("Número muito baixo.")
        print("Tente um número MAIOR.")
    