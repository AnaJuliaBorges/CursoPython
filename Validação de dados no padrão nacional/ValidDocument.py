from validate_docbr import CPF, CNPJ

class Document:

    @staticmethod
    def create_document(document):
        if len(document) == 11:
            return DocCPF(document)
        elif len(document) == 14:
            return DocCNPJ(document)
        else:
            raise ValueError("Quantidade de dígitos incorretos")


class DocCPF:
    def __init__(self, document):
        document = str(document)
        if self.valid(document):
            self.cpf = document
        else:
            raise ValueError("CPF inválido!")

    def valid(self, document):
        return CPF().validate(document)

    def format(self):
        return CPF().mask(self.cpf)

    def __str__(self):
        return self.format()


class DocCNPJ:
    def __init__(self, document):
        document = str(document)
        if self.valid(document):
            self.cnpj = document
        else:
            raise ValueError("CPF inválido!")

    def valid(self, document):
        return CNPJ().validate(document)

    def format(self):
        return CNPJ().mask(self.cnpj)

    def __str__(self):
        return self.format()


