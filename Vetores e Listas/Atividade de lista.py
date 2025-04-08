# Questão 01

lista = []
vogais = ["a","e","i","o","u"]
for i in range(10):
    caracter = input("Digite um caracter: ")
    if caracter not in vogais:
        lista.append(caracter)
print(lista,"\n", len(lista))

# Questão 02

numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    if not numero%2 == 0:
        impares.append(numero)
    else: pares.append(numero)
print("Todos os numeros: ", numeros, "\n", "Pares: ", pares, "\n", "Impares: ", impares)"""

"""# Questão 03

valor = []

for i in range(10):
    numero = int(input("Digite um número: "))
    valor.append(numero)
print("O valor maximo: ", max(valor), "O menor valor: ", min(valor))

# Questão 04

lista01 = [1,2,3,4,5]
lista02 = [5,4,3,2,1]
lista03 = []
for var range(5):
    lista03.append(lista01[var] * lista02[var])
print(vetor03)
      
# Questão 05

vetor01 = [1,2,3]
vetor02 = [5,4,3]
vetor03 = []
for var in range(3):
    vetor03.append(vetor01[var]*vetor02[var])
print(sum(vetor03))
    
    
