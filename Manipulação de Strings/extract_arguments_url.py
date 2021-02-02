class ExtractArgumentsURL:
    def __init__(self, url):
        if self.str_is_valid(url):
            self.url = url
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

        begin_substring_destiny = self.find_index_begin_substring(destiny_currency_search)

        destiny_currency = self.url[begin_substring_destiny:]

        return origin_currency, destiny_currency

    def find_index_begin_substring(self, value):
        return self.url.find(value) + len(value) + 1
