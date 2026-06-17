# CONTINUE - reinicia o laço (volta pra linha do while)
# SOMAR 5 VALORES INTEIROS DIGITADOS PELO USUÁRIO
# SE DIGITAR VALOR NEGATIVO, USAR continue PARA reiniciar
# a repetição atual
contador = 0
soma = 0
while contador < 5 :
    numero = int(input("Digite um número positivo: "))
    if numero < 0:
        print("Inválido")
        continue            # sobe para o while
    
    contador = contador + 1 # aumenta o contador
    soma = soma + numero    # faz a soma

else:                         # se o laço encerrar por
    print("O total é", soma)  # break, NÃO executa o else

