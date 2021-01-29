import random


def play():
    print("----------------------------------")
    print("Bem vindo ao jogo de adivinhação")
    print("----------------------------------")

    secret_number = random.randint(1, 100)
    max_attempts = 0
    score = 1000

    # while attempts > 0:
    #     guess = int(input("Qual a resposta de tudo? "))
    #
    #     if guess == secret_number:
    #         print("Você acertou :D")
    #         break
    #     else:
    #         if guess < secret_number:
    #             print("Dica: seu chute foi menor que a resposta")
    #
    #         elif guess > secret_number:
    #             print("Dica: seu chute foi maior que a resposta")
    #
    #         attempts -= 1
    #         print(f"Não foi dessa vez :(, lhe restam {attempts} tentativas")

    print("Qual o nivel de dificuldade do jogo?")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    level = int(input("Digite a dificuldade desejada: "))

    if level == 1:
        max_attempts = 20
    elif level == 2:
        max_attempts = 10
    else:
        max_attempts = 5

    for attempts in range(1, max_attempts + 1):
        guess = int(input("Qual a resposta de tudo? "))

        if guess < 1 or guess > 100:
            print("(Dica: É um número entre 1 e 100)")
            print(f"Lhe restam {max_attempts - attempts} tentativas")
            continue

        if guess == secret_number:
            print(f"Você acertou e obteve {score} pontos")
            break

        else:
            if guess < secret_number:
                print("(Dica: seu chute foi menor que a resposta)")

            elif guess > secret_number:
                print("(Dica: seu chute foi maior que a resposta)")

            score -= abs(secret_number - guess)
            print(f"Não foi dessa vez :(, lhe restam {max_attempts - attempts} tentativas")

    print("-----------------------")
    print(f"Resposta: {secret_number}")
    print("Fim de jogo")

if (__name__ == "__main__"):
    play()
