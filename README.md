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

No meu código, com ajuda do ChatGPT inseri um dicionário com uma lista específica contendo todos os e-mails desejados, através do código:
      
`destinatarios {`

`‘ meuemail@gmail.com ’: ‘ nome_da_pessoa ’
‘ meuemail@gmail.com ’: ‘ nome_da_pessoa ’`

`}`

##### Em seguida, criei uma função padrão para enviar alertas via e-mail, através do código abaixo:

    def criar_corpo_email (nome_destinatario, cotacao):
       corpo_email = f"""
    <p>Olá {nome_destinatario}, O DÓLAR ATINGIU SEU MENOR PATAMAR!
        A Cotação Atual é: R${cotacao}</p>"""
    return corpo_email

##### Nesta etapa deve-se inserir a chave de acesso fornecida pelo o Google.

    def enviar_email(corpo_email, destinatario):
      msg = email.message.Message()
      msg['Subject'] = "O DÓLAR BAIXOU, APROVEITE!"
      msg['From'] = 'dadosensivel@gmail.com'
      msg['To'] = 'dadosensivel@gmail.com'
      password = 'ejklgfod*******'
      msg.add_header('Content-Type', 'text/html')
      msg.set_payload(corpo_email)

      s = smtplib.SMTP('smtp.gmail.com: 587')
      s.starttls()
      # Login Credentials for sending the mail
      s.login(msg['From'], password)
      s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

##### Nesta etapa criei uma condicional onde definimos o alerta apenas para o caso do dólar ficar abaixo de 5 reais.

    for email_destinatario, nome_destinatario in destinatarios.items():
      if cotacao < 5 and email_destinatario == 'dadosensivel@gmail.com':
        corpo_email = criar_corpo_email(nome_destinatario, cotacao)
        enviar_email(corpo_email, email_destinatario)