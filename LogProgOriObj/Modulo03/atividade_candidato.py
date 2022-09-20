import enum
from glob import glob

class candidato(enum.Enum):
    branco = 0
    cand_x = 887
    cand_y = 847
    cand_z = 515
    
global votei_x
global votei_y
global votei_z
global votei_branc
global votei_nul

votei_x = 0
votei_y = 0
votei_z = 0
votei_branc = 0
votei_nul = 0

print('-----Votação Iniciada-----\n')
print('Número dos candidatos: \n Candidato X: 887 \n Candidato Y: 847 \n Candidato Z: 515 \n voto em branco: 0 \n')
print('Qualquer outro número ou caracter fora do escopo será considerado Nulo. \n')

while True:
 
    votacao = int(input('Digite o número do seu candidato: '))

    if(votacao == candidato.cand_x.value):
        votei_x = votei_x + 1

    elif(votacao == candidato.cand_y.value):
        votei_y = votei_y + 1

    elif(votacao == candidato.cand_z.value):
        votei_z = votei_z + 1

    elif(votacao == candidato.branco.value):
        votei_branc = votei_branc + 1

    elif(votacao > 0 and votacao < 515):
        votei_nul = votei_nul + 1

    elif(votacao > 515 and votacao < 847):
        votei_nul = votei_nul + 1

    elif(votacao > 847 and votacao < 887):
        votei_nul = votei_nul + 1

    elif(votacao > 887):
        votei_nul = votei_nul + 1

    repetir = int(input('Você deseja votar novamente? \n |1 para Sim | 2 para Não| '))

    if(repetir == 1):
        True
    else: 
        print('Finalizando votação.')
        print(f'A quantidade de votos do candidato X foi de: {votei_x}')
        print(f'A quantidade de votos do candidato Y foi de: {votei_y}')
        print(f'A quantidade de votos do candidato Z foi de: {votei_z}')
        print(f'A quantidade de votos nulos foi de: {votei_nul}')
        print(f'A quantidade de votos brancos foi de: {votei_branc}')

        if(votei_x > votei_y and votei_x > votei_z):
            print(f'O candidato vencedor foi CANDIDATO X! com {votei_x} votos no total!')
        elif(votei_y > votei_x and votei_y > votei_z):
            print(f'O candidato vencedor foi CANDIDATO Y! com {votei_y} votos no total!')
        elif(votei_z > votei_x and votei_z > votei_y):
            print(f'O candidato vencedor foi CANDIDATO Z! com {votei_z} votos no total!')
        break

    