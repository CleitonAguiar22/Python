# Questão 01
class Veiculo:

    def mover(self):
        pass

class Carro(Veiculo):
    def mover():
        print(f'O carro está sendo digirido na estrada.')

class Bicicleta(Veiculo):
    def mover():
        print(f'A bicicleta está sendo pedalada na ciclovia.')
    

def moverVeiculo(Veiculo):
    return Veiculo.mover()

moverVeiculo(Carro)

moverVeiculo(Bicicleta)

# Questão 02

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


class Rentagulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        print(self.largura * self.altura)

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        print(3.14 * self.raio**2)
        

def calcular_area_da_forma(Forma):
    return Forma.calcular_area()

retangulo01 = Rentagulo(10,2)
circulo01 = Circulo(5)

formas = [retangulo01, circulo01]

def calcular_area_formas(formas):
    for f in formas:
        f.calcular_area()

calcular_area_formas(formas)

