
   ***Documento de Requisitos: Gestão de Vendas***
   
      1.  Requisitos Funcionais (RF) RF01 - Cadastro de Produtos: O sistema deve permitir criar, ler, atualizar e excluir produtos (Nome, Preço e Quantidade em Estoque).
           RF02 - Registro de Venda: O sistema deve permitir selecionar um produto,   informar a quantidade e finalizar a venda.
           RF03 - Histórico de Vendas: O sistema deve listar as vendas realizadas com o valor total de cada uma.
           
      2.  Regras de Negócio (RN) RN01 - Estoque Mínimo: Uma venda não pode ser    processada se a quantidade solicitada for maior que o estoque disponível.
           RN02 - Atualização de Inventário: Ao confirmar uma venda, o sistema deve subtrair automaticamente a quantidade vendida do saldo de estoque do produto.
           RN03 - Preço Positivo: Não deve ser permitido o cadastro de produtos com valor de venda igual ou inferior a zero.s


1. ***Visão Geral*** 
      
O projeto consiste no desenvolvimento de um sistema enxuto voltado para a Gestão de Vendas e Controle de Inventário. O objetivo central foi criar uma aplicação funcional que integrasse as melhores práticas de  engenharia de software, garantindo a coerência entre o planejamento documental (diagramas) e a implementação técnica.


2. ***Arquitetura e Padrões de Projeto***
   
Para garantir a escalabilidade e a manutenção do sistema, foi adotada a arquitetura em camadas seguindo o padrão MVC (Model-View-Controller), complementado pelas camadas de Service e Repository:

. View: Interface de interação (implementada em versões Terminal e Web/Flask).

. Controller: Intermediário que gerencia o fluxo de dados entre a interface e a lógica.

. Service: Concentra as Regras de Negócio, como validação de preços positivos e verificação de disponibilidade de estoque.

. Repository: Responsável pela abstração do acesso aos dados e persistência.

. Model: Representação das entidades do domínio (Produto e Venda).


3. ***Persistência de Dados***
A persistência foi realizada através do SQLite, um sistema de gerenciamento de banco de dados relacional embutido. A escolha justifica-se pela sua portabilidade e eficiência em ambientes de desenvolvimento ágil, permitindo que os dados de produtos e histórico de transações sejam mantidos de forma íntegra e permanente.


4. ***Metodologia de Desenvolvimento***
O desenvolvimento seguiu uma abordagem orientada à consistência documental, onde:

- Requisitos e Regras de Negócio definiram as restrições do sistema.

- Diagramas de Casos de Uso e Atividade mapearam o comportamento esperado.

- Diagramas de Classe e Sequência nortearam a estrutura do código e a interação entre as camadas.

- A Implementação refletiu rigorosamente o que foi planejado nos artefatos de UML.


5. ***Conclusão***
O sistema cumpre os requisitos de um desenvolvimento orientado ao tempo de aula, entregando uma ferramenta capaz de cadastrar produtos e registrar vendas com baixa automática de estoque, respeitando princípios de modularização e separação de responsabilidades.

