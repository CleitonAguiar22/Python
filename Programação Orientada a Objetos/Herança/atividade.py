# Questão 01

class Veiculo:
    # Atributos

    def __init__(self, marca, modelo , ano): 
        self.marca = marca 
        self.modelo = modelo 
        self.ano = ano 

    def info_veiculo(self):
        print(f'Modelo do veiculo: {self.modelo}, Marca do veiculo: {self.marca}, Ano do veiculo: {self.ano}')

class Carro(Veiculo):
    # Atributos

    def __init__(self, marca, modelo, ano, quantidadeDePortas):
        self.quantidadeDePortas = quantidadeDePortas
        super().__init__(marca, modelo, ano)

    # Metodos

    def info_carro(self):
        print(f'{super().info_veiculo()}, Quantidade de portas do carro: {self.quantidadeDePortas}')

    
carro01 = Carro ("Honda", "Civic", 2020, 4)

carro01.info_veiculo()
carro01.info_carro()

# Questão 02


class Funcionario:
    # Atributos

        def __init__(self, nome, salario):
             self.nome = nome
             self.salario = salario

    # Metodos
        def exibir_info(self):
             return(f'Nome do Funcionario: {self.nome}, Salario do Funcionario: {self.salario}') 

class Gerente(Funcionario):

        # Atributos
    def __init__(self, nome, salario, departamento):
         self.departamento = departamento
         super().__init__(nome, salario)
        # Metodos
    def exibir_info_do_gerente(self):
         print(f'{super().exibir_info()}, departamento do funcionario: {self.departamento}')

class Tecnico(Funcionario):
     
     # Atributos
     def __init__(self, nome, salario, turno):
          self.turno = turno
          super().__init__(nome, salario)
    
     # Metodos
     def exibir_info_do_tecnico(self):
          print(f'{super().exibir_info()}, turno do funcionario: {self.turno}')

funcionario01 = Tecnico("Cleiton", 2000, "Integral")

funcionario01.exibir_info()
funcionario01.exibir_info_do_tecnico()

funcionario01 = Gerente("Cleiton", 2000, "TI")

funcionario01.exibir_info()
funcionario01.exibir_info_do_gerente()


# Questão 03

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cuprimentar(self):
        print(f'Olá {self.nome}')

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        self.curso = curso
        super().__init__(nome, idade)

    def info_aluno(self):
        print(f'Nome do aluno: {self.nome}, Idade do Aluno: {self.idade}, Curso: {self.curso}')  


aluno01 = Aluno("Cleiton", 18, "Programação de Rede de Computadores")

aluno01.cuprimentar()
aluno01.info_aluno()
