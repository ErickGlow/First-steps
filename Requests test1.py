import requests


s = requests.get('https://revenuebot.io',  timeout=5)
x = s.status_code
if x == 200:
    print('RB is working')
else:
    print('RB has an error')
print(s.status_code)

s = requests.get('https://poloniex.com/',  timeout=5)
x = s.status_code
if x == 200:
    print('Poloniex is working')
else:
    print('Poloniex has an error')
print(s.status_code)

s = requests.get('https://www.binance.com',  timeout=5)
x = s.status_code
if x == 200:
    print('Binance is working')
else:
    print('Binance has an error')
print(s.status_code)

s = requests.get('https://exmo.me/',  timeout=5)
x = s.status_code
if x == 200:
    print('Exmo is working')
else:
    print('Exmo has an error')
print(s.status_code)

#s = requests.get('https://www.bybit.com',  timeout=5)
#x = s.status_code
#if x == 200:
#    print('Bybit is working')
#else:
#    print('Bybit has an error')
#print(s.status_code)

s = requests.get('https://www.bitget.com',  timeout=5)
x = s.status_code
if x == 200:
    print('Bitget is working')
else:
    print('Bitget has an error')
print(s.status_code)

s = requests.get('https://www.bitfinex.com/',  timeout=5)
x = s.status_code
if x == 200:
    print('Bitfinex is working')
else:
    print('Bitfinex has an error')
print(s.status_code)

s = requests.get('https://global.bittrex.com/',  timeout=5)
x = s.status_code
if x == 200:
    print('Bittrex is working')
else:
    print('Bittrex has an error')
print(s.status_code)

s = requests.get('https://www.gate.io',  timeout=5)
x = s.status_code
if x == 200:
    print('Gate is working')
else:
    print('Gate has an error')
print(s.status_code)

s = requests.get('https://www.huobi.com',  timeout=5)
x = s.status_code
if x == 200:
    print('Huobi is working')
else:
    print('Huobi has an error')
print(s.status_code)

s = requests.get('https://cex.io/',  timeout=5)
x = s.status_code
if x == 200:
    print('Cex is working')
else:
    print('Cex has an error')
print(s.status_code)

#s = requests.get('https://ftx.com',  timeout=5)
#x = s.status_code
#if x == 200:
#    print('FTX is working')
#else:
#    print('FTX has an error')
#print(s.status_code)

s = requests.get('https://hitbtc.com/',  timeout=5)
x = s.status_code
if x == 200:
    print('HitBTC is working')
else:
    print('HitBTC has an error')
print(s.status_code)

s = requests.get('https://www.kraken.com',  timeout=5)
x = s.status_code
if x == 200:
    print('Kraken is working')
else:
    print('Kraken has an error')
print(s.status_code)

s = requests.get('https://www.kucoin.com',  timeout=5)
x = s.status_code
if x == 200:
    print('Kucoin is working')
else:
    print('Kucoin has an error')
print(s.status_code)

s = requests.get('https://www.okx.com',  timeout=5)
x = s.status_code
if x == 200:
    print('OKX is working')
else:
    print('OKX has an error')
print(s.status_code)

