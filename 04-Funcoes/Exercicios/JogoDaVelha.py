from os import system, name

def clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')

# ----------------
# caracter casas[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
casas = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# logico fimDoJogo = falso
fim_do_jogo = False
# logico ehAVezDoJogadorA = verdadeiro
eh_a_vez_do_jogador_x = True
# inteiro casaEscolhida = 0

# inteiro casasLivres = 9
casas_livres = 9
# caracter marcadorCasa = 'X'
marcador_casa = 'X'
#cadeia ganhador = "Velha"
ganhador = 'Velha'
    
def clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')

def iniciar_jogo(): pass

def imprimir_tabuleiro(): pass

def verificar_ganhador(): pass

iniciar_jogo()