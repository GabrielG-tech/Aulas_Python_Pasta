programa
 {

	// Vetor com as casas do tabuleiro do Jogo
	caracter casas[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
	// Indicador de Final de jogo: Quando o jogo deve acabar
	logico fimDoJogo = falso
	// Indicador do jogador do Turno
	logico ehAVezDoJogadorA = verdadeiro
	// Indicador da casa escolhida pelo Jogador
	inteiro casaEscolhida = 0
	// Quantidade de casas livres para finalizar o jogo
	inteiro casasLivres = 9
	// Indicador do marcador para a escolha do jogador
	caracter marcadorCasa = 'X'
	// Indicador do ganhador
	cadeia ganhador = "Velha"
		
	funcao inicio()
 {

		faca {
			// Exibe tabuleiro
			limpa()
			escreva("Jogador da Vez: ", marcadorCasa, "\n\n")
			imprimirTabuleiro()

			// Solicita uma jogada do usuário
			escreva("\n\n")
			escreva("Escolha uma casa válida ou 0 para sair: ")
			leia(casaEscolhida)

			// Escolheu sair do jogo
			se (casaEscolhida == 0) fimDoJogo = verdadeiro

			// Escolheu uma casa válida
			senao se (casaEscolhida >= 1 e casaEscolhida <= 9) {

				// Se a casa não está ocupada...
				se (nao (casas[casaEscolhida - 1] == 'X') e 
					nao (casas[casaEscolhida - 1] == 'O')){
						// Marcar a casa escolhida
						casas[casaEscolhida - 1] = marcadorCasa
						// Muda o jogador
						ehAVezDoJogadorA = nao ehAVezDoJogadorA
						// Decrementa o número de casas livres
						casasLivres--
						// Verifica se há ganhador
						se (verificarGanhador()){
								ganhador = "Jogador " + marcadorCasa
								casasLivres = 0
							}
						// Verificar se ainda há casa disponível
						se (casasLivres == 0) fimDoJogo = verdadeiro
						// Muda o marcador da casa
						se (ehAVezDoJogadorA) marcadorCasa = 'X'
						senao marcadorCasa = 'O'
					}
			}
		} enquanto (nao fimDoJogo)

		// Exibe a última configuração do tabuleiro
		limpa()
		escreva("Fim do Jogo!\n\n")
		escreva("Ganhador: ", ganhador, "\n\n")
		imprimirTabuleiro()
	}

	funcao imprimirTabuleiro(){
		escreva("| ")
		para (inteiro casa = 0; casa < 9; casa++){
			escreva(casas[casa], " | ")
			se (casa == 2 ou casa == 5)
				escreva("\n-------------\n| ")
		}
	}
	
	funcao logico verificarGanhador(){
		retorne   // Trilhas horizontais
				(casas[0] == casas[1] e casas[1] == casas[2]) ou 
				(casas[3] == casas[4] e casas[4] == casas[5]) ou 
				(casas[6] == casas[7] e casas[7] == casas[8]) ou
				// Trilhas verticais
				(casas[0] == casas[3] e casas[3] == casas[6]) ou 
				(casas[1] == casas[4] e casas[4] == casas[7]) ou 
				(casas[2] == casas[5] e casas[5] == casas[8]) ou
				// Trilhas diagonais
				(casas[0] == casas[4] e casas[4] == casas[8]) ou
				(casas[2] == casas[4] e casas[4] == casas[6])
	}
}