# Questão 01

numeros = [ ]
for var in  range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)
    print(numeros[::-1])

# Questão 02

valores = [ ]
for var in  range(10):
    valor = float(input("Digite um número real: "))
    valores.append(valor)
    print(sum(valores))

# Questão 03

notas = [ ]
for var in  range(4):
    nota = float(input("Digite um número real: "))
    notas.append(nota)
    print(sum(notas)/len(notas))
