from ValidDocument import Document

example_cpf = "15316264754"
cpf = Document.create_document(example_cpf)
print(cpf)

example_cnpj = "35379838000112"
cnpj = Document.create_document(example_cnpj)
print(cnpj)