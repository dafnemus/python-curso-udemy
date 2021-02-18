# pylint: disable=missing-docstring

# Conocer el valor de Bitcoin.
# api = Coindesk
import requests

API_URL_BITCOIN = 'https://api.coindesk.com/v1/bpi/currentprice.json'

result = requests.get(API_URL_BITCOIN)

if result.status_code != requests.codes.OK:  # pylint: disable=no-member
    print('Algo ha pasado')
print('Todo está OK')

print()
bitcoin_data = dict(result.json())

# imprimir la clave y sus valoes usando items

for key, elemento in bitcoin_data.items():
    print(f'clave: {key}')
    print(elemento)

print()
# bitcoin en USD:
usd = bitcoin_data['bpi']['USD']
print(f'bitcoin in USD: {usd}')

usd_value = bitcoin_data['bpi']['USD']['rate']
valor_bit_usd = float(usd_value.replace(',', ''))
print(f'USD: {valor_bit_usd}')
