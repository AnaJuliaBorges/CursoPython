import adivinhacao
import forca


def chose():
    print("----------------------------------")
    print("Escolha seu jogo")
    print("----------------------------------")

    print("(1) Forca, (2) Adivinhação")

    game = int(input("Digite o jogo escolhido: "))
    test(game)


def test(game):
    if (game == 1):
        forca.play()
    elif (game == 2):
        adivinhacao.play()
    else:
        print("jogo inexistente")
        chose()


if (__name__ == "__main__"):
    chose()
