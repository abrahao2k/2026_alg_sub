tempo = int(input("Tempo de permanência (minutos): "))
veiculo = input("Qual o veículo (carro/moto): ")
if tempo <= 10 :
    print("Tarifa: GRÁTIS")
else:
    if veiculo == "carro":
        print("Tarifa: R$ 12,00")
    else:
        print("Tarifa: R$ 6,00")

