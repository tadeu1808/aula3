class Produto:
    
        def __init__(self, produto, preco):
            self.produto = produto
            self.preco = preco
        
        def __str__(self):
            return f"Produto(nome={self.produto}, preco={self.preco})"            
        
