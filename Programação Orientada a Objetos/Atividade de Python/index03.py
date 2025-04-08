def valorMaior(a = int(input("Digite um número: ")), b = int(input("Digite outro número: "))):
    if a == b:
        return print("Os valores são iguais")
    if a > b:
        x = a
        return print(f'{x} é maior')
    else: x = b 
    return print(f'{x} é maior')

valorMaior()