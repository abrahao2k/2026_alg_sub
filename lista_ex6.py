'''6) Em uma eleição sindical concorreram ao cargo de
presidente três candidatos (A, B e C). Durante a
apuração dos votos foram computados votos nulos e
votos em branco, além dos votos válidos para cada
candidato. Deve ser criado um programa de computador
que efetue a leitura da quantidade de votos válidos
para cada candidato, além de efetuar também a leitura
da quantidade de votos nulos e votos em branco. Ao
final o programa deve apresentar o número total de
eleitores, considerando votos válidos, nulos e em
branco; o percentual correspondente de votos válidos
em relação à quantidade de eleitores; o percentual
correspondente de votos válidos de cada candidato em
relação à quantidade de eleitores, além do percentual
de votos brancos e votos nulos;'''

a = int(input("Candidato A: "))
b = int(input("Candidato B: "))
c = int(input("Candidato C: "))
nulo = int(input("Votos nulos: "))
branco = int(input("Votos brancos: "))

total = a + b + c + nulo + branco
print("Total de eleitores = ", total)

per_validos = (a + b + c) / total * 100
print(f"Votos válidos = {per_validos:.1f}%")

print(f"Candidato A = {a/total*100:.1f}%")
print(f"Candidato B = {b/total*100:.1f}%")
print(f"Candidato C = {c/total*100:.1f}%")
print(f"Nulos = {nulo/total*100:.1f}%")
print(f"Brancos = {branco/total*100:.1f}%")
