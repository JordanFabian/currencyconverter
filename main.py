import requests

usd = float(input("Quantidade em dolar: "))

try:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    if response.status_code != 200:
        raise Exception("Falha")

    data = response.json()
    exchange_rate = data["rates"]["BRL"]
    euro = usd * exchange_rate

    print("{:.2f} dolares serão {:.2f} Reais".format(usd, euro))
except Exception as e:
    print("Exceção: {}".format(e))