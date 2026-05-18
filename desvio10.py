''' pergunte qual o turno que o aluno
estuda (manhã, tarde ou noite). Se digitar
um desses, mostre a mensagem "Turno registrado".
Para qualquer outro, mostre "Turno inválido". '''

turno = input("Qual o turno do aluno? ")

if turno=="manhã" or turno=="tarde" or turno=="noite":
    print("Turno registrado.")
else:
    print("Turno inválido.")

