from collections import defaultdict, Counter

my_text = "Olá meu nome é ana Júlia e quase me chamei maria júlia " \
          "gosto de gosto doce e meu doce favorito é doce de coco".lower()

word_appered = Counter(my_text.split())

for word, value in word_appered.items():
    print(word,"apareceu", value, "x")

print("\n")

class Account:
    def __init__(self):
        print("Criando Conta...")

accounts = defaultdict(Account)
accounts[26]
accounts[34]
accounts[15]
accounts[34]