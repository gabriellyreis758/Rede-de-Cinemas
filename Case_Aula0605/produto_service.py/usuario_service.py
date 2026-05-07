class ProdutoService:
    def __init__(self, repository):
        self.repo = repository

    def cadastrar_produto(self, id, nome, preco, estoque):
        if preco <= 0:
            return False, "Erro: Preço deve ser positivo."
        
        try:
            # Aqui poderias criar um objeto Model se tivesses a pasta model
            # Para manter enxuto, passamos os dados diretamente ao repo
            class ProdutoDTO: pass # Objeto temporário
            p = ProdutoDTO()
            p.id, p.nome, p.preco, p.estoque = id, nome, preco, estoque
            
            self.repo.salvar(p)
            return True, "Produto guardado com sucesso!"
        except Exception as e:
            return False, f"Erro: {e}"