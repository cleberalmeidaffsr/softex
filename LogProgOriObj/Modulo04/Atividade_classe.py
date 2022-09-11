class Televisao:
    def __init__(self, marca, polegadas, preço):
        self.marca = marca
        self.polegadas = polegadas
        self.preço = preço
    def mudar_volume(self, volume):
        if volume == '+':
            print('Aumentando volume')
        elif(volume == '-'):
            print('Diminuindo volume')
    def ligar_televisao(self):
        print('Televisão ligada!')

Televisao.ligar_televisao(True)
televisao1 = Televisao('Samsung', '85 polegadas', '90.000 Reais')
print(televisao1.marca)
televisao2 = Televisao('Samsung', '32 polegadas', '1.288 Reais')
print(televisao2.polegadas)
televisao3 = Televisao('LG', '65 polegadas', '8.500 Reais')
print(televisao3.preço)

Televisao.mudar_volume(televisao1,'+')
