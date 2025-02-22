#main
from sistema.app.controllers.clienteController import clienteController

def exibir_menu():
    
    print("\n ===== Menu =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar Cliente")
    print("3 - Cadastrar produto")
    print("4 - Listar Produto")
    print("0 - Sair do sistema")
    
def main():
    cntrlCliente = clienteController()
    while True:
        exibir_menu()    
        opc = input ("Escolha uma opção: ")
        
        if opc == "1":
            nome = input("nome do cliente:")
            email = input("E-mail:")
            idade = int(input("Idade:"))
            cntrlCliente.criar_cliente(nome, email, idade)
            
        elif opc == "2":
            clientes = cntrlCliente.listar_clientes()
            for index, cliente in enumerate(clientes, 1):
                #index é a posição do cliente listado
                print(f"{index}. {cliente}")            
            
        elif opc == "3":
            nome = input("Nome do produto:")
            preco = float(input("Preço:"))
            
        elif opc == "4":
            print("listar")
            
        elif opc == "0":
            print("Saindo do sistema...")    
            break
        else:
            print("opção invalida, tente novamente")
            
if __name__ == "__main__":
    main()
    
    #python main.py     
            
                              
                                            
