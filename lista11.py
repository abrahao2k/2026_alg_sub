lista = [10, 35, 14, 10, 29, 53, 27, 21, 2, 49, 10]

soma = sum(lista)

media = sum(lista) / len(lista)

print(soma)
print(media)

print("Maior:", max(lista))
print("Menor:", min(lista))

print("Contagem:", lista.count(10))

lista.clear() # 

print(lista)