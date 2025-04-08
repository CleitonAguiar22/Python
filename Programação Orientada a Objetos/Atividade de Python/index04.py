def radarDeVelocidade(v = int(input("Digite a sua velocidade: "))):
    if v < 0:
        return print("O valor de sua velocidade não pode ser negativo.")
    if v >= 0 and v <= 20:
        return print("Velocidade baixa.")
    if v >= 21 and v <= 40:
        return print("Valocidade média.")
    if v >= 41 and v <= 60:
        return print("Velocidade alta.")
    else: return print("Velocidade muito alta.")

radarDeVelocidade()