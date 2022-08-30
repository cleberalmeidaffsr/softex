class Televisão:
    def __init__(self, marca, polegadas, preço):
        self.marca = marca
        self.polegadas = polegadas
        self.preço = preço
    def mudar_volume(self, volume):
        if volume == '+':
            print('Aumentando volume')
        elif(volume == '-'):
            print('Diminuindo volume')
    def ligar_televisão(self):
        print('Televisão ligada!')

Televisão.ligar_televisão(True)
televisão1 = Televisão('Samsung', '85 polegadas', '90.000 Reais')
print(televisão1.marca)
televisão2 = Televisão('Samsung', '32 polegadas', '1.288 Reais')
print(televisão2.polegadas)
televisão3 = Televisão('LG', '65 polegadas', '8.500 Reais')
print(televisão3.preço)

Televisão.mudar_volume(televisão1,'+')
