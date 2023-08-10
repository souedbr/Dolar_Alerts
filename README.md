# Dolar_Alerts
O projeto consiste na criação de
um sistema de alertas, utilizei de integração para trazer
as informações relacionadas a cotação do dólar diretamente da
internet. Os alertas devem ser enviados sempre que o dólar estiver
abaixo de 5 reais.

### Pontos principais para o bom funcionamento do código:

#### Adicionar ao código os "imports"

- requests
- smtplib
- email.message

#### É preciso pegar as informações desejadas, ou seja, integrei com a API awesomeapi (gratuita) para pegar a informação desejada (Cotação USD-BRL).

- Para conectar utilizei um requests.get(” link da api”) - get: puxar
- requisicao.json( ) - Onde transformei o dicionário python em dicionário json
- Precisei transformar o dicionário json em variável float através do código:

      nome_da_variavel = float(requisicao_dicionario [ ’USDBRL’ ] [ ‘bid’ ])
Observação: Se desejar, é só imprimir na tela a informação relacionada a cotação.

