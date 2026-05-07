from flask import Flask, render_template, request, redirect, url_for

class UsuarioViewWeb:
    def __init__(self, controller):
        self.app = Flask(__name__)
        self.controller = controller
        self._configurar_rotas()

    def _configurar_rotas(self):
        # Rota principal: Lista produtos
        @self.app.route('/')
        def index():
            # Aqui você pode pedir ao controller/repo a lista de produtos
            return "<h1>E-commerce Web</h1><p>Sistema conectado via Controller!</p><a href='/cadastrar'>Cadastrar Produto</a>"

        # Rota de Cadastro (Exibe formulário e recebe dados)
        @self.app.route('/cadastrar', methods=['GET', 'POST'])
        def cadastrar():
            if request.method == 'POST':
                # Captura dados do formulário HTML
                id = int(request.form['id'])
                nome = request.form['nome']
                preco = float(request.form['preco'])
                qtd = int(request.form['estoque'])
                
                # Chama o Controller (Mantendo a arquitetura!)
                sucesso, msg = self.controller.executar_cadastro(id, nome, preco, qtd)
                return f"<h3>{msg}</h3><a href='/'>Voltar</a>"
            
            # Formulário HTML simples
            return '''
                <form method="post">
                    ID: <input type="number" name="id"><br>
                    Nome: <input type="text" name="nome"><br>
                    Preço: <input type="number" step="0.01" name="preco"><br>
                    Estoque: <input type="number" name="estoque"><br>
                    <input type="submit" value="Salvar">
                </form>
            '''

    def iniciar(self):
        self.app.run(debug=True, port=5000)