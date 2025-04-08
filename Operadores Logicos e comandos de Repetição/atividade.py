# Questão 01

valor1 = int(input("Digite um número: "))
valor2 = int(input("digite outro número: ")
             
if not valor1 < 0 and  not valor2 < 0:
    print(valor1, "e", valor2, "são positivos")
elif not valor1  > 0 or not valor2 > 0:
    print(valor1."ou", valor2 "são negagativos")

# Questão 02

email = "usuario.adm@exemplo.com"
usuario = "admin"
senha = 1234

digit_email = input("Digite seu email: ")
digit_senha = int(input("Digite sua senha: "))


if not digit_email == "usuario.adm@exemplo.com" or  not digit_senha == 1234:
    usuario = "client"
    
if digit_email == "usuario.adm@exemplo.com" and digit_senha == 1234:
    usuario = "admin"
    
if usuario == "admin":
    print("Acesso permitido.")
    
if not usuario == "admin":
    print("Acesso negado.")

# Questão 03

numero = int(input("Digite um número: "))

if not numero < 0 and numero%2 == 0:
    print("Esse número é Par e Positivo.")
elif not numero  < 0 and numero%2 != 0:
    print("Esse número é Ímpar e Positivo.")
elif not numero > 0:
    print("Esse número é Ímpar.")

# Questão 04

idade = int(input("Digite sua idade: "))
possuiC = input("Digite 'Sim' ou 'Não' se você é possuinte da CNH: ")

if not idade >= 18 or possuiC == "não" or possuiC == "Não":
    print("Você não pode dirigir.")
else: print("Você pode dirigir.")

# Questão 05

i = 0
while i <= 10:
    print(i)
    i += 1

# Questão 06

i = 0
while i <= 20:
    if i%2 == 0:
        print(i)
    i+= 1

# Questão 07

n = int(input("Digite um número: "))
i = 1
soma = 1

while i < n:
    i += 1
    soma += i
print(soma)

# Questão 08

valor = int(input("digite um número: "))

for num in range(1, 11, 1):
    print(valor,"x",num,"=",valor*num)

# Questão 09

valor = int(input("digite um número: "))

while valor >= 0:
    print(valor)
    valor -= 1
# Questão 10

nota1 = int(input("Digite nota_1: "))

nota2 = int(input("Digite nota_2: "))

nota3 = int(input("Digite nota_3: "))

nota4 = int(input("Digite nota_4: "))

nota5 = int(input("Digite nota_5: "))

i = 0

while i < 1:
    media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
    i += 1
print("Média = ",media)

# Questão 11

nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while nome == senha:
    print("Nome e senha não pode ser identicos, digite novamente")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    



