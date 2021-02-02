class ExtractArgumentsURL:
    def __init__(self, url):
        if self.str_is_valid(url):
            self.url = url.lower()
        else:
            raise LookupError("URL inválida !!")

    def str_is_valid(self, url):
        if url:
            return True
        else:
            return False


    def returns_currency(self):
        origin_currency_search = "moedaorigem"
        destiny_currency_search = "moedadestino"

        begin_substring_origin = self.find_index_begin_substring(origin_currency_search)
        end_substring_origin = self.url.find("&")
        origin_currency = self.url[begin_substring_origin: end_substring_origin]

        if (origin_currency == 'moedadestino'):
            origin_currency = self.verify_currency_origin(origin_currency_search)

        begin_substring_destiny = self.find_index_begin_substring(destiny_currency_search)
        end_substring_destiny = self.url.find("&valor")

        destiny_currency = self.url[begin_substring_destiny:end_substring_destiny]

        return origin_currency, destiny_currency

    def find_index_begin_substring(self, value):
        return self.url.find(value) + len(value) + 1

    def verify_currency_origin(self, search_origin_currency):
        self.url = self.url.replace("moedadestino", "real", 1)
        begin_substring_origin = self.find_index_begin_substring(search_origin_currency)

        end_substring_origin = self.url.find("&")
        return self.url[begin_substring_origin:end_substring_origin]

    def return_value(self):
        search_value = "valor"
        begin_substring_value = self.find_index_begin_substring(search_value)
        value = self.url[begin_substring_value:]
        return value

    def __str__(self):
        origin_currency, destiny_currency = self.returns_currency()
        str_representation = f"Valor: {self.return_value()}\n" \
                             f"Moeda Origem: {origin_currency} \n" \
                             f"Moeda Destino: {destiny_currency}"
        return str_representation

    def __len__(self):
        return len(self.url)

    def __eq__(self, other):
        return self.url == other.url
