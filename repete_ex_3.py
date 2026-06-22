'''3) Crie um programa em que o usuário digite 10 números
e o programa apresente a soma desses números. Dica: use
uma variável para acumular a soma dos números, como no
exemplo: soma = soma + numero. '''

soma = 0

cont = 1
while cont <= 10:
    num = int(input("Digite um número: "))
    soma = soma + num
    cont = cont + 1

print("Total =", soma)