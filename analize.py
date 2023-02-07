import time

import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define o símbolo da criptomoeda que você quer analisar
symbol = "GALAUSDT"

# URL da API da Binance
url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1d"

while True:
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        # Converte os dados retornados em um DataFrame
        df = pd.DataFrame(data, columns=["Open time", "Open", "High", "Low", "Close", "Volume", "Close time",
                                         "Quote asset volume", "Number of trades", "Taker buy base asset volume",
                                         "Taker buy quote asset volume", "Ignore"])

        # Converte as colunas para o tipo float
        df[["Open", "High", "Low", "Close", "Volume"]] = df[["Open", "High", "Low", "Close", "Volume"]].astype(float)

        # Adiciona uma coluna com a variação do preço entre o fechamento e o abertura
        df["Price variation"] = df["Close"] - df["Open"]

        # Verifica se a variação de preço é positiva ou negativa
        if df["Price variation"].iloc[-1] > 0:
            print("Recomenda-se comprar")
        else:
            print("Recomenda-se vender")

        plt.plot(df["Close time"], df["Close"])
        plt.xlabel("Tempo")
        plt.ylabel("Preço de fechamento")
        plt.show()
    else:
        print("Erro ao buscar dados da API da Binance:", response.status_code)
    time.sleep(2)