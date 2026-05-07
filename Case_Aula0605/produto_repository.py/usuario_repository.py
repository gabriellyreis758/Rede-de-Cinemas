import sqlite3

class ProdutoRepository:
    def __init__(self):
        self.conn = sqlite3.connect("vendas.db")
        self.cursor = self.conn.cursor()
        self._criar_tabela()

    def _criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                estoque INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def salvar(self, produto):
        self.cursor.execute("INSERT INTO produtos VALUES (?, ?, ?, ?)", 
                            (produto.id, produto.nome, produto.preco, produto.estoque))
        self.conn.commit()

    def buscar_todos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()