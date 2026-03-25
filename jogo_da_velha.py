# Jogo da velha

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)
def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True

    # Verificar colunas
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"É a vez do jogador {jogador_atual}.")
        linha = int(input("Digite a linha (0, 1 ou 2): "))
        coluna = int(input("Digite a coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            if verificar_vencedor(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Parabéns! O jogador {jogador_atual} venceu!")
                break
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Essa posição já está ocupada. Tente novamente.")

if __name__ == "__main__":
    jogar()