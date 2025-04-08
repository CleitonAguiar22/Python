def trocarValores(x = 2, y = 1):
    print(f'Valor de X: {x}, Valor de Y: {y}')
    z = x
    x = y
    y = z
    return print(f'Valor de X: {x}, Valor de Y: {y}') 

trocarValores()