from collections import defaultdict

my_text = "Olá meu nome é ana Júlia e quase me chamei maria júlia " \
          "gosto de gosto doce e meu doce favorito é doce de coco".lower()

word_appered = defaultdict(int)
for word in my_text.split():
    until_now = word_appered[word]
    word_appered[word] = until_now + 1

for word, value in word_appered.items():
    print(word, value)
