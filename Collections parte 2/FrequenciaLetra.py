from collections import Counter

text1 = "Para começar a fazer vendas online, uma empresa que fabrica adesivos criou uma página para " \
        "pré cadastro de cartão de crédito que contém campos como nome, idade, endereço, CPF entre outros."

text2 = "Fora isso, o tipo de conteúdo pode ser o mesmo do marketing de conteúdo B2C. Passando desde textos " \
        "sobre novidades, inovações e dicas na área, até infográficos com dados de pesquisas, vídeos, áudios de " \
        "podcast, imagens e publicações nas redes sociais. Também, para conteúdo B2B, é muito comum encontrar " \
        "whitepapers, grupos de usuários, meetups, cases de sucesso, trial gratuito, e até mesmo vídeos ou campanhas " \
        "e posts de marketing com influenciadores."

def analyzes_letter_frequency(text):
    appeared = Counter(text.lower())
    total_characters = sum(appeared.values())

    for characters, proportion in appeared.most_common(10):
        proportion = proportion/total_characters
        #print("{} => {:.2f}%".format(characters, proportion * 100))
        print(f"{characters} => {proportion * 100:.2f}%")

analyzes_letter_frequency(text1)
print("\n", "texto 2")
analyzes_letter_frequency(text2)