'''crie um programa que pergunta o curso de um aluno
e a série que ele frequenta. se for aluno de informática
da 3a serie ou maior, diga que tem vaga de estágio.
qualquer outro curso, ou serie abaixo, não tem estágio'''

curso = input("Digite o curso: ")
serie = int(input("Digite a série: "))

if curso == "informática" and serie >= 3 :
    print("Tem vaga de estágio.")

else:
    print("Não tem estágio.")