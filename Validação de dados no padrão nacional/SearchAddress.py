import requests

class SearchAddress:

    def __init__(self, cep):
        cep = str(cep)
        if self.valid_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep()

    def valid_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def access_zip_code(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        result = requests.get(url)
        data = result.json()
        return (
            data['bairro'],
            data['localidade'],
            data['uf']
        )
