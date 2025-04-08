class Cachorro:
    def __init__(self, nome,raça,dono,vacinas):
        #atributos
        self.nome = nome #publico
        self.raça = raça #publico
        self.__dono = dono #privado
        self._vacinas = vacinas #protegido

        #metodos
    def get_dono(self):
        print(self.__dono)
    
    def set_dono(self, novoNome):
        self.__dono = novoNome
        print(f'Nome atualizado para {self.__dono}')

    def latir(self):
        print("au au")


cachorro = Cachorro("Mel", "Labrador", "Cleiton", ['virose'])
print(cachorro.nome)
print(cachorro.raça)
cachorro.latir()
print(cachorro._vacinas)
cachorro.get_dono()
cachorro.set_dono("Marcos")
cachorro.get_dono()





