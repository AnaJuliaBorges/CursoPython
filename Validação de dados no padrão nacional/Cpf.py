from validate_docbr import CPF

class Cpf:
    def __init__(self, document):
        document = str(document)
        if self.cpf_eh_Valido(document):
            self.cpf = document
        else:
            raise ValueError("CPF inválido!")

    def cpf_eh_Valido(self, cpf):
        if len(cpf) == 11:
            return CPF().validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.format_cpf()


