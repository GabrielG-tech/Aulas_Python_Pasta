from os import system, name 

def clear(): 
    if name == 'nt': _ = system('cls') 
    else: _ = system('clear') 

# caracter casas[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
casa = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# logico fimDoJogo = falso
fim_do_jogo = False
# logico ehAVezDoJogadorA = verdadeiro
eh_a_vez_do_jogador_x = True
# inteiro casaEscolhida = 0 --> não precisa

# inteiro casasLivres = 9
casas_livres = 9
# caracter marcadorCasa = 'X'
marcadorCasa = 'X'
# cadeia ganhador = "Velha"
ganhador = "Velha"

def iniciar_jogo():
    # Exibe tabuleiro
    clear()
    print('Jogador da vez: ', marcadorCasa, '\n\n')
    imprimir_tabuleiro()
    
    # Solicita uma jogada do usuário
    print('\n\n')
    input('Escolha uma casa válida ou 0 para sair: ')
    
def imprimir_tabuleiro(): pass
    
    
def verificar_ganhador(): pass
