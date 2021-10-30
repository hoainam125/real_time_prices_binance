import ccxt
import time
from datetime import datetime
import json
import matplotlib.pyplot as plt

binance = ccxt.binance({
    'apiKey': str(input("apiKey: ")),
    'secret': str(input("secretKey: "))
})
binance.set_sandbox_mode(int(input("Sanbox_mode: 1 if true , 0 if false")))


def getPrices(a=[], b=[]):
    priceOrigin = binance.fetch_ohlcv('BNB/USDT', timeframe='1d', limit=1000)
    prices = {}
    for i in priceOrigin:
        for j in range(len(i) - 1):
            prices = {
                'Time:': datetime.fromtimestamp(i[0] / 1000).isoformat("#", "seconds"),
                'Open:': i[1],
                'High:': i[2],
                'Low:': i[3],
                'Close:': i[4],
                'Volume:': i[5]
            }
        a.append(i[4])
        time = datetime.fromtimestamp(i[0] / 1000).isoformat("#", "seconds")
        time = time.split("#", 1)
        b.append(time[0])



def view_prices():
    # print(fullBalance['total']['BNB'])
    y_axist = []
    x_axist = []
    i = 0
    while True:
        getPrices(y_axist, x_axist)
        print(x_axist[i], y_axist[i])
        i += 1
        plt.plot(x_axist, y_axist)
        plt.pause(1)
        time.sleep(59)
def get_balance():
    fullBalance = binance.fetch_balance()
    print(type(fullBalance))