""""#Questão 01

def contador(inicio, fim):
    while(inicio <= fim):
        print(inicio)
        inicio += 1

contador(1, 10)

#Questão 02

def contador(inicio, fim):
    while(inicio <= fim):
        print(inicio)
        inicio += 2

contador(0, 10)

#Questão 03

def indentificarMa():
    numeros = []
    for i in range(3):
        num = int(input("Digite um número: "))
        numeros.append(num)
    print(max(numeros))

indentificarMa()

def indentificarMe():
    numeros = []
    for i in range(3):
        num = int(input("Digite um número: "))
        numeros.append(num)
    print(min(numeros))

indentificarMe()

# Questão 04

def fatorial(num):
    fatoracao = num
    
    while (num > 1):
        num -= 1
        fatoracao *= num
    print(fatoracao)
    
fatorial(0)"""

# Questão 05

def Calculadora():
    num1 = int(input("Digite o primeiro valor: "))
    operador = input("Qual operação você deseja usar: Adição, Subtração, Divisão ou Multiplicação: ")
    
    if (operador.lower() == "adição" or operador.lower() == "adicao"):
         num2 = int(input("Digite o segundo valor: "))
         resultado = num1 + num2
         print(f"A soma entre {num1} e {num2} é  igual à {resultado}")

    elif (operador.lower() == "subtração" or operador.lower() == "subtracao"):
         num2 = int(input("Digite o segundo valor: "))
         resultado = num1 - num2
         print(f"A subtração entre {num1} e {num2} é  igual à {resultado}")

    elif (operador.lower() == "multiplicação" or operador.lower() == "multiplicacao" or operador.lower() == "multiplicaçao"):
         num2 = int(input("Digite o segundo valor: "))
         resultado = num1 * num2
         print(f"A multiplicação entre {num1} e {num2} é  igual à {resultado}")

    elif (operador.lower() == "divisão" or operador.lower() == "divisao"):
         num2 = int(input("Digite o segundo valor: "))
         resultado = num1 / num2
         print(f"A divisão entre {num1} e {num2} é  igual à {resultado}")
         
    else:
        print("Operador digitado não existente")
         
Calculadora()
         
    
    



