from repository.produto_repository import ProdutoRepository
from service.produto_service import ProdutoService
from controller.produto_controller import ProdutoController
from view.usuario_view_web import UsuarioViewWeb  # Importa a nova View

repo = ProdutoRepository()
serv = ProdutoService(repo)
ctrl = ProdutoController(serv)
view_web = UsuarioViewWeb(ctrl)

if __name__ == "__main__":
    print("Servidor rodando em http://127.0.0.1:5000")
    view_web.iniciar()