# Jogo da forca

import random

def escolher_palavra():
    palavras = ["cachorro", "gato", "elefante", "girafa", "leão", "tigre", "urso", "coelho", "macaco", "panda", "zebra", "hipopótamo", "rinoceronte", "cavalo", "ovelha", "vaca", "porco", "galinha", "pato", "galo", "peixe", "tartaruga", "cobra", "jacaré", "sapo", "rato", "camelo", "lobo", "raposa", "coruja", "falcão", "águia", "urso polar", "leopardo", "pantera", "guepardo", "antílope", "bode", "cabra", "ovelha", "cavalo-marinho", "golfinho", "baleia", "tubarão", "polvo", "lula"]
    return random.choice(palavras)
print("Bem-vindo ao Jogo da Forca!")
print("Tente adivinhar a palavra antes de ser enforcado!")
print("Dica: A palavra é um animal.")

def exibir_forca(erros):
    forca = [
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |"
    ]
    if erros >= 1:
        forca[2] = "  O   |"
    if erros >= 2:
        forca[3] = "  |   |"
    if erros >= 3:
        forca[3] = " /|   |"
    if erros >= 4:
        forca[3] = " /|\\  |"
    if erros >= 5:
        forca[4] = " /    |"
    if erros >= 6:
        forca[4] = " / \\  |"

    for linha in forca:
        print(linha)

def jogar():
    palavra = escolher_palavra()
    letras_certas = []
    letras_erradas = []
    erros = 0

    while True:
        print("\nPalavra:", end=" ")
        for letra in palavra:
            if letra in letras_certas:
                print(letra, end=" ")
            else:
                print("_", end=" ")

        print(f"\nLetras erradas: {', '.join(letras_erradas)}")
        exibir_forca(erros)

        if erros == 6:
            print("Você perdeu!")
            break

        letra = input("\nDigite uma letra: ").lower()

        if letra in letras_certas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            letras_certas.append(letra)
            if all(letra in letras_certas for letra in palavra):
                print("Parabéns! Você acertou a palavra!, a resposta era:", palavra)
                break
        else:
            letras_erradas.append(letra)
            erros += 1

if __name__ == "__main__":

    jogar()