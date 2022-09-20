from re import S
import time

def calcular(number1, number2, op):
    if op == "+":
        return number1 + number2
    elif op == "-":
        return number1 - number2
    elif op == "*":
        return number1 * number2
    elif op == "/":
        return number1 / number2
    else:
        return 0

print("Iniciando calculadora... aguarde.")
time.sleep(5)

number1 = float(input("Digite um número: "))
time.sleep(1)

number2 = float(input("Digite o segundo número: "))
time.sleep(1)

op = input("Qual operação você deseja fazer? \n Soma(+) \n Subtração(-) \n Multiplicação(*) \n Divisão(/) \n")
time.sleep(1)

print("Aguarde um momento, estamos calculando...")
time.sleep(5)

print(number1, op, number2, '=', calcular(number1, number2, op))