## exemplo de como organizar os arquivos do jogo

## Este é o arquivo principal

# Importa os arquivos de cada jogo, eles devem estar todos na mesma pasta.
import forca, velha

# Este arquivo pode ter mais funções além da main(),
# para imprimir o menu, por exemplo. 

def main():
    <bloco de código para perguntar em um laço qual o jogo,
    com menu, opções para escolher o jogo e sair.>
    <opção 1 --> jogo da velha, chamar --> velha.main()>
    <opção 2 --> jogo da forca, chamar --> forca.main()>
    <opção 3 --> sair --> finaliza o laço e encerra o programa>

    # Esta função não tem parâmetros nem return. As outras funções, definidas
    # acima, deverão ter ou não parâmetro e returns conforme o necessário
    # para cada uma, de acordo com a forma que vocês organizaram o código.
    #
    # NÃO É PERMITIDO O USO DE VARIÁVEIS GLOBAIS! PROGRAMAS QUE FIZEREM USO
    # DE VARIÁVEIS GLOBAIS TERÃO NOTA MÁXIMA IGUAL A 5

# Mantenham esse if no final do código.
# A explicação está no vídeo da última aula de LP1.
if __name__ == '__main__':
    main()
