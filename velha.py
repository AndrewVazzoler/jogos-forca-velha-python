import os
import time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print("|=======================================|")
    print("|             JOGO DA VELHA             |")
    print("|=======================================|")


def velha(m):
    print("|          +-----+-----+-----+          |")
    print("|          |  {}  |  {}  |  {}  |          |".format(
        m[0][0], m[0][1], m[0][2]))
    print("|          +-----+-----+-----+          |")
    print("|          |  {}  |  {}  |  {}  |          |".format(
        m[1][0], m[1][1], m[1][2]))
    print("|          +-----+-----+-----+          |")
    print("|          |  {}  |  {}  |  {}  |          |".format(
        m[2][0], m[2][1], m[2][2]))
    print("|          +-----+-----+-----+          |")
    print("|=======================================|")


def valida_jogada(jogada, jogador, matriz):
    valida = False
    if(jogada):
        for x in range(3):
            for z in range(3):
                if int(jogada) == matriz[x][z]:
                    
                    matriz[x][z] = jogador
                    valida = True
    return [valida, matriz]


def fazer_jogada(jogador, matriz):
    valida = False
    while not valida:
        jogada = input("Informe sua jogada, jogador {}: ".format(jogador))
        validaJogada = valida_jogada(jogada, jogador, matriz)
        
        if(validaJogada[0]):
            return validaJogada[1]
        else:
            print("Jogada invalida!")


def tem_ganhador(matriz):
    for jogador in ['X', 'O']:
        # horizontal
        for h in range(3):
            if matriz[h][0] == matriz[h][1] == matriz[h][2] == jogador:
                return jogador
        # vertical
        for v in range(3):
            if matriz[0][v] == matriz[1][v] == matriz[2][v] == jogador:
                return jogador
        # diagonal
        if matriz[0][0] == matriz[1][1] == matriz[2][2] == jogador:
            return jogador
        if matriz[0][2] == matriz[1][1] == matriz[2][0] == jogador:
            return jogador
    return False


def main():
    cls()
    matriz = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    jogadas = 0

    cabecalho()
    velha(matriz)

    continuar = True
    while continuar:
        jogador = 'X' if jogadas % 2 == 0 else 'O'
        matriz = fazer_jogada(jogador, matriz)
        ganhador = tem_ganhador(matriz)
        jogadas += 1
        cls()

        cabecalho()
        velha(matriz)

        if(ganhador):
            print("\nParabens jogador {} \n".format(ganhador))
            continuar = False
            time.sleep(3)

        if(jogadas == 9 and not ganhador):
            print("\nDeu velha!!!\n")
            continuar = False
            time.sleep(3)


if __name__ == '__main__':
    main()
