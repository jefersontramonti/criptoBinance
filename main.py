import requests
import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Define o símbolo da criptomoeda que você quer analisar
symbol = "GALAUSDT"

# URL da API da Binance
url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1d"

# Faz a chamada à API e recebe a resposta
response = requests.get(url)

# Verifica se a resposta foi recebida com sucesso
if response.status_code == 200:
    # Carrega o conteúdo da resposta em um dicionário
    data = json.loads(response.content)

    # Converte os dados retornados em um DataFrame
    df = pd.DataFrame(data, columns=["Open time", "Open", "High", "Low", "Close", "Volume", "Close time",
                                     "Quote asset volume", "Number of trades", "Taker buy base asset volume",
                                     "Taker buy quote asset volume", "Ignore"])

    # Converte as colunas para o tipo float
    df[["Open", "High", "Low", "Close", "Volume"]] = df[["Open", "High", "Low", "Close", "Volume"]].astype(float)

    # Adiciona uma coluna com a variação do preço entre o fechamento e o abertura
    df["Price variation"] = df["Close"] - df["Open"]

    # Divide os dados em treinamento e teste
    X = df.drop("Price variation", axis=1)
    y = df["Price variation"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


    # Treina um modelo de regressão linear
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Faz previsões para os dados de teste
    y_pred = model.predict(X_test)

    # Calcula o erro médio absoluto (MAE)
    mae = np.mean(np.abs(y_pred - y_test))
    print("MAE:", mae)

    plt.plot(df["Close time"], df["Close"])
    plt.xlabel("Tempo")
    plt.ylabel("Preço de fechamento")
    plt.show()
else:
    # Imprime uma mensagem de erro caso a resposta não tenha sido recebida com sucesso
    print("Erro ao buscar dados da API da Binance:", response.status_code)
