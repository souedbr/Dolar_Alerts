    #Adicionar os imports
import requests
import smtplib
import email.message
    #Pegar a informação desejada
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dicionario = requisicao.json()
dolar_alerts = float (requisicao_dicionario ['USDBRL']['bid'])
print(dolar_alerts)

