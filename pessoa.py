# pessoa

class Pessoa:
    
    # metodo construtor
    #é chamado auando criamos um objeto
    
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura 

    def apresentar(self):
        print(f'Olá meu nome é {self.nome} e tenho')
        print(f'{self.idade} anos e tenho')
        print(f'{self.altura} de altura')
        print()

p1 = Pessoa("Rafael", 34, "1.50")
p2 = Pessoa("Guilherme", 7, "1.35")
p3 = Pessoa("Alberto", 18, "1.95")

p1.apresentar()
p2.apresentar()
p3.apresentar()

