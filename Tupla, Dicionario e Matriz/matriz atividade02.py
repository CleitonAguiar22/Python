matriz = [[2,4,6,8],
          [10,12,14,16],
          [1,3,5,7],
          [9,11,13,15]]

lista = []

for l in range(4):
    for c in range(4):
        lista.append(matriz[l][c])
print(sum(lista))




