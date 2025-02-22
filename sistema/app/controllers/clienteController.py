from ..models.cliente import Cliente
from ..database.database import BancoFake

class clienteController:
    
    def __init__(self):
        self.db = BancoFake()
    
    def criar_cliente(self, nome, email, idade):
        novo_cliente = Cliente(nome, email, idade)
        #converter para dict - JSON
        dict_cliente = {
            "nome": novo_cliente.nome,
            "email": novo_cliente.email,
            "idade": novo_cliente.idade
        }
        #salvar no banco
        self.db.adicionar_cliente(dict_cliente)
        print("Cliente cadastrado com sucesso!")
        
    def listar_clientes(self):
        return self.db.listar_clientes()
        
        




#print("Listar Clientes")
        
        