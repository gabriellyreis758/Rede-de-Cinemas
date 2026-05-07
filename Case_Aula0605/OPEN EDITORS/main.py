from repository.produto_repository import ProdutoRepository
from service.produto_service import ProdutoService
from controller.produto_controller import ProdutoController
from view.main_view import MainView

# Injeção de Dependências seguindo a arquitetura
repo = ProdutoRepository()
serv = ProdutoService(repo)
ctrl = ProdutoController(serv)
view = MainView(ctrl)

if __name__ == "__main__":
    view.exibir_menu()