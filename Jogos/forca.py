import random


def play():
    print_opening_message()
    secret_word = loading_secret_word()

    correct_letters = ["_" for letter in secret_word]

    attempts = 7

    hang = False
    correct = False

    print(f"A palavra é: {correct_letters}")

    while (not hang and not correct):
        guess = input("Qual a Letra? ").strip().upper()

        if guess in secret_word:
            mark_right_letters(guess, correct_letters, secret_word)
        else:
            attempts -= 1
            print_gallows(guess, attempts)

        hang = attempts == 0
        correct = "_" not in correct_letters

        print(correct_letters)

    if correct:
        print_victory_message()
    else:
        print_gameover_message(secret_word)

    print("\n_____ FIM DE JOGO ____________-")


def print_opening_message():
    print("----------------------------------")
    print("Bem vindo ao jogo da forca")
    print("----------------------------------")


def loading_secret_word(arquivo="palavras.txt"):
    archive = open(arquivo)
    possible_words = [line.strip().upper() for line in archive]
    archive.close()

    return possible_words[random.randrange(0, len(possible_words))]


def mark_right_letters(guess, correct_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            correct_letters[index] = letter
        index += 1


def print_victory_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_gameover_message(secret_word):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def print_gallows(guess, attempts):
    print(f"Ops, não tem a letra {guess}, você possui mais {attempts} tentativas")

    print("  _______     ")
    print(" |/      |    ")

    if (attempts == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (attempts == 5):
        print(" |      (_)   ")
        print(" |       |     ")
        print(" |            ")
        print(" |            ")

    if (attempts == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (attempts == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (attempts == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (attempts == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (attempts == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    play()
