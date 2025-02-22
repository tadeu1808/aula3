import json
from pathlib import Path

class BancoFake:
    
    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": [], "produtos": []}
        self._carregar()
    def _carregar(self):
        """
        Carrega dados do arquivo JSOn, se existir. 
        Caso não exista, inicia com dados vazios       
        """        
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            #abrindo arquivo no modo leitura em utf-8
            with open(caminho, 'r', encoding="utf-8") as data:
                #salvando dados que ja exitem no arquivo
                #variavel dados
                self.dados = json.load(data)
        else:
            self._salvar()
            
    def _salvar(self):
        #salvar o coneudo delf.daddos no qrquivo JSON, abrimndo arquivo no W, escrita
        with open(self.arquivo_db, "w", encoding="utf-8") as f:
            #realizando dump (python para Json) para salvar no banco
            json.dump(self.dados, f, ensure_ascii=False, indent=4)
    def adicionar_cliente(self, cliente_dict):
        self.dados["clientes"].append(cliente_dict)
        self._salvar()
        
    def adicionar_produto(self, dict_produto):
        self.dados["produtos"].append(dict_produto)
        self._salvar()    
        
    def listar_clientes(self):
        return self.dados["clientes"]
    
    def listar_produtos(self):
        return self.dados["produtos"]
    
    
        