import requests
import time

# Define o símbolo da criptomoeda que você quer monitorar
symbol = "GALAUSDT"

# URL da API da Binance
url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"

# Define o limite de compra
buy_limit = 0.0005

# Define o limite de venda
sell_limit = 0.0007

# Laço infinito para monitorar o preço da criptomoeda
while True:
    # Faz a chamada à API e recebe a resposta
    response = requests.get(url)

    # Verifica se a resposta foi recebida com sucesso
    if response.status_code == 200:
        # Carrega o conteúdo da resposta em um dicionário
        data = response.json()

        # Recupera o preço atual da criptomoeda
        price = float(data["price"])

        # Verifica se o preço atingiu o limite de compra
        if price <= buy_limit:
            # Envia uma notificação de compra
            print("Compre agora! Preço:", price)

        # Verifica se o preço atingiu o limite de venda
        if price >= sell_limit:
            # Envia uma notificação de venda
            print("Venda agora! Preço:", price)

        # Espera 10 segundos antes de verificar o preço novamente
        time.sleep(10)
    else:
        # Imprime uma mensagem de erro caso a resposta não tenha sido recebida com sucesso
        print("Erro ao buscar dados da API da Binance:", response.status_code)
