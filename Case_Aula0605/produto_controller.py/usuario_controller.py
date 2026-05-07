class ProdutoController:
    def __init__(self, service):
        self.service = service

    def executar_cadastro(self, id, nome, preco, estoque):
        return self.service.cadastrar_produto(id, nome, preco, estoque)