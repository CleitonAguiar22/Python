# Questão 1

senha = 12345
digite_senha = int(input("Digite sua senha: "))
if digite_senha == senha:
    print("Senha correta.")
else: print("Senha incorreta.")

# Questão 2

digite_numero = int(input("Digite um número: "))
if digite_numero%2 == 0:
    print("Este número é Par.")
else: print("Este número é Ímpar.")

# Questão 3

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num2 > num1:
    print(f'{num1} é menor que {num2}')
else: print("Os números são iguais")

# Questão 4

altura = float(input("Digite sua altura: "))

if altura < 1.50:
    print("Você é baixo.")
elif altura < 1.80:
    print("Você tem altura média")
else: print("Você é alto")

# Questão 5

altura = float(input("Digite sua altura: "))
peso = int(input("Digite seu peso: "))

IMC = peso / (altura*altura)

if IMC < 18.5:
    print("Abaixo do peso.")
elif IMC < 24.9:
    print("Peso ideal.")
elif IMC < 29.9:
    print("Sobrepeso.")
else: print("Obesidade")


# Questão 6

letra = str(input("Digite uma letra: "))

if letra == "a":
    print("Está letra é uma Vogal")
elif letra == "e":
    print("Está letra é uma Vogal")
elif letra == "i":
    print("Está letra é uma Vogal")
elif letra == "o":
    print("Está letra é uma Vogal")
elif letra == "u":
    print("Está letra é uma Vogal")
    
else: print("Esta letra é uma Consoante")
