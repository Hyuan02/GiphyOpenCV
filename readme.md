#Visualizador de GIF Open CV

### Uso

Para utilizar o visualizador de gif, primeiramente coloque 
imagens no diretório _assets_ que se encontra no projeto.
Após isso execute o arquivo `main.py` no IDE de sua 
preferência.

O código se encontra devidamente comentado e documentado.

### Estrutura de dados

A estrutura de dados escolhida foi a **Lista Encadeada**,
pela facilidade de armazenar a referência 
ao próximo nó, em sua estrutura de dados, 
facilitando a reprodução de GIF's, que são 
sequências lineares de imagens.

---------
Para a escolha de um quadro a ser alterado, foi utilizado
uma função de simulação de índice, em que retorna o elemento
correspondente ao índice pedido, navegando entre as 
referências da lista.