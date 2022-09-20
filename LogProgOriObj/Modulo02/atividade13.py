nomeAluno = input("Digite o nome do Aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
faltas = int(input("Digite as faltas do Aluno: "))
media = (nota1 + nota2)/2

if media >= 7.0 and faltas <= 3 :
    print("Parabéns", nomeAluno , "você foi aprovado.")
else :
    print(nomeAluno, ", você está reprovado. :(")