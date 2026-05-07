
   Documento de Requisitos: Gestão de Vendas
      1.Requisitos Funcionais (RF) RF01 - Cadastro de Produtos: O sistema deve permitir criar, ler, atualizar e excluir produtos (Nome, Preço e Quantidade em Estoque).
           RF02 - Registro de Venda: O sistema deve permitir selecionar um produto,   informar a quantidade e finalizar a venda.
           RF03 - Histórico de Vendas: O sistema deve listar as vendas realizadas com o valor total de cada uma.
      2.  Regras de Negócio (RN) RN01 - Estoque Mínimo: Uma venda não pode ser    processada se a quantidade solicitada for maior que o estoque disponível.
           RN02 - Atualização de Inventário: Ao confirmar uma venda, o sistema deve subtrair automaticamente a quantidade vendida do saldo de estoque do produto.
           RN03 - Preço Positivo: Não deve ser permitido o cadastro de produtos com valor de venda igual ou inferior a zero.s

