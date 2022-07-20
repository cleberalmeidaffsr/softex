# uma calculadora simples!]

rep_Cal = 's'

def soma(x, y):
    return x + y

def subtra(x, y):
    return x - y

def multipl(x, y):
    return x * y

def divisao(x, y):
    return x / y

print('Selecione a operação:')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('0 - Sair')

while rep_Cal == 's':
    escolha = input('Escolha a operação digitando o número correspondente (1/2/3/4/0): ')
    
    if escolha == '0':
        print('Saindo do programa')
        break

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input('Coloque o primeiro número: '))
        num2 = float(input('Coloque o segundo número: '))

        if escolha == '1':
            print(num1, '+', num2, '=', soma(num1, num2))
        
        elif escolha == '2':
            print(num1, '-', num2, '=', subtra(num1, num2))
        
        elif escolha == '3':
            print(num1, '*', num2, '=', multipl(num1, num2))
        
        elif escolha == '4':
            print(num1, '/', num2, '=', divisao(num1, num2))
        
        rep_Cal = input('Você quer fazer outro calculo? (s - sim / n - não)')
        
        if rep_Cal == 'n':
            print('Fechando programa. :(')


        
    else:
        print('Essa opção não existe')
        