class MainView:
    def __init__(self, controller):
        self.controller = controller

    def exibir_menu(self):
        while True:
            print("\n--- SISTEMA E-COMMERCE ---")
            print("1. Cadastrar Produto")
            print("0. Sair")
            op = input("Opção: ")

            if op == "1":
                id = int(input("ID: "))
                nome = input("Nome: ")
                preco = float(input("Preço: "))
                qtd = int(input("Estoque: "))
                
                sucesso, msg = self.controller.executar_cadastro(id, nome, preco, qtd)
                print(msg)
            elif op == "0": break