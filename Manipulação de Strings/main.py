from extract_arguments_url import ExtractArgumentsURL

url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar"

argumentsURL = ExtractArgumentsURL(url)
origin_currency, destiny_currency = argumentsURL.returns_currency()

print(origin_currency, destiny_currency)

