import coinmarketcapapi


API_KEY = '78aad556-a89a-4bf1-89ac-d3235f27afa9'


print('Currency to exchange(symbols):')
cur_currency = input()
print('Currency you need(symbols):')
needed_currency = input()
print("Amount:")
amount = float(input())


cmc = coinmarketcapapi.CoinMarketCapAPI(API_KEY)
tool = cmc.tools_priceconversion(amount=amount, symbol=cur_currency, convert=needed_currency).data
print(tool['quote'][needed_currency.upper()]['price'])
input()
