from extract_arguments_url import ExtractArgumentsURL

'''
url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar"

argumentsURL = ExtractArgumentsURL(url)
origin_currency, destiny_currency = argumentsURL.returns_currency()

print(origin_currency, destiny_currency)

'''

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
exchange = ExtractArgumentsURL(url)
origin_currency, destiny_currency = exchange.returns_currency()
value = exchange.return_value()
print(origin_currency, destiny_currency, value)
