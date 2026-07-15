# listas

cores = ["azul", "branco", "cinza", "dourado"]
           #0        #1       #2        #3
print(cores)
print(cores[2])
# atualizar
cores[1] = "verde"
print(cores)
print(cores.index("dourado")) #em qual posição está

print(len(cores)) # quantos elementos tem na lista

# adicionar um novo elemento
cores.append("preto")
print(cores)

cores.remove("cinza") # remover pelo elemento
print(cores)

#verificar se um elemento está na lista
if "branco" in cores: print("Existe")
else: print("Não encontrado")

# remover pela posição
cores.pop(2)
print(cores)

# ordenar os dados
cores.sort()
print(cores)

cores.reverse()  # inverte a lista
print(cores)

