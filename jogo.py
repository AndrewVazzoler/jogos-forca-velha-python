import os 
import forca
import velha

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('Vamos jogar ?')
    print('1 - jogo da velha')
    print('2 - jogo da forca')
    print('3 - para sair')

    valido = False
    while not valido:
        op = int(input('Sua escolha: '))
        if op in [1, 2, 3]:
            return op


def main():
    
    continua = True

    while continua:
        opcao = menu()

        if opcao == 1:
            velha.main()
        elif opcao == 2:
            forca.main()
        elif opcao == 3 :
            continua = False
        cls()    

if __name__ == '__main__':
    main()
