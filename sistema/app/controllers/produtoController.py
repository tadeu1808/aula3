from ..models.produto import Produto
from ..database.database import BancoFake

class produtoController:
    
    def __init__(self):
        self.db = BancoFake()
    
    def criar_produto(self, produto, preco):
        novo_produto = Produto(produto, preco)
        #converter para dict - JSON
        dict_produto = {
            "produto": novo_produto.produto,
            "preco": novo_produto.preco,
            
        }
        #salvar no banco
        self.db.adicionar_produto(dict_produto)
        print("produto cadastrado com sucesso!")
        
    def listar_produtos(self):
        return self.db.listar_produtos()
        
        