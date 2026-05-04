'''pergunte a idade do usuário e mostre a frase
de acordo com a tabela:
< 12 anos         - criança
de 12 até 17 anos - adolescente
> 17 anos         - adulto '''

idade = int(input("Digite a idade: "))

if idade < 12 :
    print("Você é criança.")

if idade >=12 :
    if idade <=17 :
        print("Você é adolescente.")

if idade > 17 :
    print("Você é adulto.")