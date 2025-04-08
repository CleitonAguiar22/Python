# Questão 01

class Circulo: # Criação da Classe "Circulo"
    # Atributos

    def __init__(self, raio): # Função da Classe "Circulo", que estrutura o objeto.
        self.raio = raio  # Atributo "raio". 
    
    #Metodos 

    def calcularPerimetro(self): # Função da Classe "Circulo", que calcula o Perimetro de um objeto.
        print(round(((2*3.14)*self.raio), 2)) # Mostrar o calculo seguinte no prompt.

    def calcularArea(self): # Função da classe "Circulo", que calcula o Area de um objeto.
        print(round(3.14*self.raio**2, 2)) # Mostrar o calculo seguinte no prompt.

circulo = Circulo(10) # Criação do objeto "circulo" da classe "Circulo".

print(circulo.raio) # mostrar o atributo "raio" no prompt
circulo.calcularPerimetro() # Execução a função "calcularPerimetro"
circulo.calcularArea() # Execução a função "calcularArea"

# Questão 02

class Retangulo: # Criação da Classe "Retangulo"
    # Atributos


    def __init__(self, largura, altura): # Função da Classe "Retangulo", que estrutura o objeto.
        self.largura = largura # Atributo "largura".
        self.altura = altura # Atributo "altura".


    #Metodos

    def calcularArea(self): # Função da classe "Retangulo", que calcula a Area de um objeto.
        print(round(self.altura*self.largura, 2)) # Mostra o calculo seguinte no prompt.
    
    def calcularPerimetro(self): # Função da classe "Retangulo", que calcula a Perimetro de um objeto.
        print(round(self.largura*2 + self.altura*2,2)) # Mostra o calculo seguinte no prompt.

retangulo = Retangulo(2, 5) # Criação do objeto "retangulo" da classe "Retangulo".
retangulo.calcularArea() # Execução da função "calcularArea"
retangulo.calcularPerimetro()  # Execução a função "calcularPerimetro"

# Questão 03
class ContaBancaria: # criação da classe  "Conta_bancaria".
    # Atributos
    
    def __init__(self, numeroDaConta, nomeDoTitular, saldo): # função da classe "ContaBancaria" , que estrutura um objeto.
        self.numeroDaConta = numeroDaConta #  Atributo "numero da conta".
        self.nomeDoTitular = nomeDoTitular# Atributo "nome do titular".
        self.__saldo = saldo # Atributo "saldo" (Privado).

    # Metodos

    def depositar(self, valor: float): # função da classe "ContaBancaria", que faz um "deposito" no saldo.
        if valor > 0: # condicional valor "positivo".
            self.__saldo += valor # o saldo irá incrementar o "valor" a ele mesmo.
    
    def sacar(self, valor: float): # função da classe "ContaBancaria", que faz um "saque" no saldo.
        if self.__saldo < valor: # condicional "IF", se o saldo for menor que o "valor" requisitado terá uma resposta.
            print(f'impossivel sacar {valor}, saldo insuficiente') # mostra na tela a seguinte mensagem,
        else: self.__saldo -= valor #condicinal "Else", irá tirar do "saldo" o "valor".

    def get_saldo(self): # função da classe "ContaBancaria", que mostra no promt o "saldo".
        print(f'A conta atualmente tem {self.__saldo}') # mostra no prompt o "saldo".

    
conta01 = ContaBancaria(0, "Cleiton", 1000) # Criação do objeto "conta01" da classe "ContaBancaria";

conta01.get_saldo() # função "get_saldo" para objeto "conta01" 
conta01.depositar(500) # função "depositar" para o objeto "conta01"
conta01.sacar(1500) # função "sacar" para o objeto "conta01"
conta01.get_saldo() # função "get_saldo" para objeto "conta01"


# Questão 04

class Carro: # Criação da Classe "Carro"
    # Atributos

    def __init__(self, marca, modelo , velocidadeAtual): # Função da classe "Carro", que estrutura o objeto
        self.marca = marca # Atributo marca
        self.modelo = modelo # Atributo modelo
        self.__velocidadeAtual = velocidadeAtual # Atributo valocidadeAtual (Privado)

    # Metodos

    def acelerar(self, velocidade): # função da classe "Carro" que "acelera" o objeto
        self.__velocidadeAtual += velocidade # incrementa a "self.__velocidadeAtual" o valor de "velocidade"
        print(f'você acelerou: {velocidade} KM/h') # Mostra na tela uma mensagem e o valor de "velocidade".
    
    def frear(self): # função da classe "Carro" que "freia" o objeto
        self.__velocidadeAtual = 0 # seta o valor de self.__velocidadeAtual para "0".
        print(f'Você freou') # mostra na tela uma mensagem.

    def get_velocidadeAtual(self): # função da classe "Carro", que mostra a "velocidade atual" de um objeto
        if self.__velocidadeAtual <= -1: # condicional, self.__velocidadeAtual é menor ou igual a "-1"?
            print("O carro não pode estar em uma velocidade negativa.") # mostra uma mensagem na tela.
        elif self.__velocidadeAtual == 0: # condicional, self.__velocidadeAtual é igual a "0"?
            print(f'Você está parado: {self.__velocidadeAtual}') # mostra uma mensagem na tela e o valor atual de self.__velocidadeAtual
        elif self.__velocidadeAtual > 0 and self.__velocidadeAtual < 20: # condicional, self.__velocidadeAtual é maior que 0 e menor que 20?
            print(f'Você está devagar: {self.__velocidadeAtual}') # mostra uma mensagem na tela e o valor atual de self.__velocidadeAtual
        elif self.__velocidadeAtual > 20 and self.__velocidadeAtual < 60: # condicional, self.__velocidadeAtual
            print(f'Você está andando normal: {self.__velocidadeAtual}')
        elif self.__velocidadeAtual > 60 and self.__velocidadeAtual < 100:
            print(f'você está rapido: {self.__velocidadeAtual}')
        elif self.__velocidadeAtual > 100:
            print(f'Você está muito rapido: {self.__velocidadeAtual}')

carro01 = Carro("Cadilac", "Escalade", 0)

carro01.acelerar(15)
carro01.get_velocidadeAtual()
carro01.frear()
carro01.get_velocidadeAtual()
carro01.acelerar(50)
carro01.get_velocidadeAtual()
carro01.frear()
carro01.get_velocidadeAtual()
carro01.acelerar(100)
carro01.get_velocidadeAtual()


# Questão 05

class Livro:

    # Atributos

    def __init__(self, titulo, autor, numeroDePaginas, estoque):
        self.titulo = titulo
        self.autor = autor
        self.numeroDePaginas = numeroDePaginas
        self.estoque = estoque

    # Metodos

    def emprestar(self, titulo, autor, dataDoEmprestimo, quantidadeDoLivro):
        if titulo == self.titulo and autor == self.autor and self.estoque > 0:
            self.estoque -= quantidadeDoLivro
            print(f'Livro emprestado na data: {dataDoEmprestimo}')
        else: print(f'Livro não encontrado ou estoque insuficiente.')

    def devolver(self, titulo, autor , dataDaDevolução, quantidadeDoLivro):
        if  titulo == self.titulo and autor == self.autor :
            self.estoque += quantidadeDoLivro
            print(f'Livro devolvido na data: {dataDaDevolução}')
        else: print(f'Livro não indetificado')

    def verificarEstoque(self, titulo, autor):
        if  titulo == self.titulo and autor == self.autor :
            print(f'O estoque desse livro é {self.estoque}')
    
livro01 = Livro("Dom Casmurro", "Machado De Assis", 312, 1)

livro01.emprestar("Dom Casmurro", "Machado De Assis", "08/04/2024", 1)
livro01.verificarEstoque("Dom Casmurro", "Machado De Assis")
livro01.emprestar("Dom Casmurro", "Machado De Assis", "08/04/2024", 1)
livro01.devolver("Dom Casmurro", "Machado De Assis", "08/04/2024", 1)
livro01.verificarEstoque("Dom Casmurro", "Machado De Assis")
