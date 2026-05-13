'''programa de login'''

import getpass


usuario = input("Nome do usuário: ")
senha = getpass.getpass("Digite a senha: ")

if usuario == "joao" and senha == "miau" :
    print("ACESSO PERMITIDO.")
else:
    print("ACESSO NEGADO.")

