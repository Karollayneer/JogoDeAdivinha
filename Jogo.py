import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhaçao!")
    print("Estou pensando em um numero entre 1 e 100.")

    # Escolher um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)

    tentativas = 0

    while True:
        # Pedir ao jogador para fazer uma tentativa
        tentativa = int(input("Faça sua tentativa: "))
        tentativas += 1

        # Verificar se a tentativa está correta
        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif tentativa < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

if __name__ == "__main__":
    jogo_adivinhacao()
