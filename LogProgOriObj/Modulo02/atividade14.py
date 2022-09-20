quantRodas = int(input("Digite a quantidade de rodas existentes do veículo: "))
quantPessoas = int(input("Digite a quantidade de pessoas que cabem nesse veículo: "))
pesoKg = float(input("Digite o peso em Kg desse veículo: "))

if quantRodas <= 3 and quantRodas >= 2:
    print("Habilitação indicada: Tipo A");
elif quantRodas == 4 and quantPessoas <= 8 and pesoKg <= 3500:
    print("Habilitação indicada: Tipo B");
elif quantRodas >= 4 and pesoKg >= 3500 and pesoKg <= 6000:
    print("Habilitação indicada: Tipo C");
elif quantRodas >= 4 and quantPessoas >= 8:
    print("Habilitação indicada: Tipo D");
elif quantRodas >= 4 and pesoKg >= 6000:
    print("Habilitação indicada: Tipo E");
