import os
from random import *
import time


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def criar_forca(palpites_errados):
    qtd_erros = len(palpites_errados)
    complete = 4

    forca = '    ________\n   |        |\n'

    if qtd_erros >= 1:
        forca += '   |        O\n'
        complete -= 1

    if qtd_erros == 2:
        forca += '   |        |\n'
        complete -= 1

    if qtd_erros == 3:
        forca += '   |       /|\n'

    if qtd_erros >= 4:
        forca += '   |       /|\ \n'

    if qtd_erros >= 5:
        forca += '   |        | \n'
        complete -= 1

    if qtd_erros == 6:
        forca += '   |       /\n'
        complete -= 1

    if qtd_erros == 7:
        forca += '   |       / \ \n'
        complete -= 1

    for x in range(0, complete):
        forca += '   |\n'

    forca += '__/|\__\n'

    return forca


def verifica_palpite(palpites, palpites_corretos, palpites_errados, lista_letra_palavra, letra):
    # Verifica se o palpite ja foi informado
    valido = False
    if letra in palpites:
        valido = True
    else:
        # verifica se os palpites é corretos ou incorretos e acrescenta na lista.
        if not letra in lista_letra_palavra:
            palpites_errados.append(letra)
        else:
            palpites_corretos.append(letra)

        palpites.append(letra)

    return [valido, palpites, palpites_corretos, palpites_errados]

# Imprimir os espaço da palavra


def casas_palavra(lista_letra_palavra, palpites_corretos):
    casas = ''
    acertos = 0
    for x in lista_letra_palavra:
        if x in palpites_corretos:
            casas += x + ' '
            acertos += 1
        else:
            casas += '_ '

    return ['A palavra é: ' + casas, acertos]


def op_jogo():
    print('Jogo da forca! Vamos jogar ?')
    print('1 - contra o computado')
    print('2 - contra um jogador')
    print('3 - voltar ao menu principal')

    valido = False
    while not valido:
        op = int(input('Qual o modo de jogo ? '))
        if op in [1, 2, 3]:
            valido = True
    return op


def start_jogo(palavra):
    lista_letra_palavra = list(palavra)
    palpites_errados = []
    palpites_corretos = []
    palpites = []

    cls()
    forca = criar_forca(palpites_errados)
    casas = casas_palavra(lista_letra_palavra, palpites_corretos)
    print(forca)
    print(casas[0])

    stop = False
    while not stop:

        letra = input('Digite uma letra: ').upper()

        palpite_valido = verifica_palpite(
            palpites, palpites_corretos, palpites_errados, lista_letra_palavra, letra)
        palpites = palpite_valido[1]
        palpites_corretos = palpite_valido[2]
        palpites_errados = palpite_valido[3]

        cls()

        forca = criar_forca(palpites_errados)
        casas = casas_palavra(lista_letra_palavra, palpites_corretos)
        print(forca)
        print(casas[0])

        if len(palpites_errados) != 0:
            print('Palpites errados: ', palpites_errados)

        if palpite_valido[0]:
            print('Palpite repetido!')

        if len(palpites_errados) >= 7:
            print(' \nVocê Perdeu :(\n')
            print('A palavra era:', palavra)
            time.sleep(3)
            stop = True

        if casas[1] == len(lista_letra_palavra):
            print('\nVocê venceu :)\n')
            stop = True
            time.sleep(3)
        

def main():
    cls()
    palavra = ''
    # palavras aleatorias
    animais = ['Abelha', 'Águia', 'Alce', 'Andorinha', 'Anta', 'Avestruz', 'Baleia',
               'Barata', 'Boi', 'Borboleta', 'Burro', 'Cabra', 'Camelo', 'Canguru', 'Cão',
               'Caracol', 'Caranguejo', 'Carneiro', 'Castor', 'Cavalo', 'Cisne', 'Cobra',
               'Coelho', 'Elefante', 'Esquilo', 'Falcão', 'Foca', 'Formiga', 'Furão']
    op = op_jogo()
    cls()

    if op == 1:
        selecione = randint(1, len(animais))
        palavra = animais[selecione].upper()
        start_jogo(palavra)
    elif op == 2:
        valido = False
        while not valido:
            palavra = input(
                'Digite a palavra a ser adivinhada: ').upper().strip()
            if palavra != '':
                valido = True
        start_jogo(palavra)
    else:
        print('Até mais!')
        time.sleep(2)


if __name__ == '__main__':
    main()
