#funçoes pre-definidas para as futuras operacoes
def soma (n1, n2):
    resultado = n1 + n2
    return resultado

def subtracao (n1, n2):
    resultado = n1 - n2
    print(resultado)

def multiplicacao (n1, n2):
    resultado = n1 * n2
    print(resultado)

def divisao (n1, n2):
    resultado = n1 / n2
    print(resultado)

#mensagem de entrada
print('Esse programa é uma Calculadora, Vamos começar a montar nossas operações? ')

#variaveis de entrada para a calculadora
n1 = float(input('Digite o primeiro numero para operação: '))
n2 = float(input('Digite o segundo numero para operação: '))

#mensagem para selecionar os operadores
print('selecione um dos operadores: ')

#variavel para selecionar qual tipo de operador escolher
operador = int(input('1) Adição \n2) Subtração \n3) Multiplicacao \n4 Divisão. \nR. : '))

#validacao de operador mediante escolha do usuario
if (operador == 1):
    soma = soma(n1, n2)
    print(soma)

if (operador == 2):
    subtracao = subtracao(n1, n2)
    print(subtracao)

if (operador == 3):
    multiplicacao = multiplicacao(n1, n2)
    print(multiplicacao)

if (operador == 4):
    divisao = divisao(n1, n2)
    print(divisao)

if (operador > 4):
    print('Operador invalido!! Por favor insira um outro operador. ')

