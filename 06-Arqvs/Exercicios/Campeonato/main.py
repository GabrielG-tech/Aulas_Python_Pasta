# Ler o arquivo e exibir uma tabela
# Funcao -> Todos os jogos de um time informado pelo usuário
# A funcao informe quantos pontos o time ganhou.
# 3 pontos caso vencedor
# 1 ponto caso empate
# 0 ponto caso derrota
nome_arquivo = '06-Arqvs\Exercicios\Campeonato\campeonato-brasileiro-full.csv'
arquivo = open(nome_arquivo) #, 'rb')
lista_partidas = arquivo.read().splitlines()
arquivo.close()

# print("Mandante\tVisitante\tVencedor")
# for partida in lista_partidas:
#    partida = partida.split(',')
#    print(partida[5],"\t", partida[6],"\t", partida[11])

def buscar_jogos_por_time(time):
    lista_de_jogos = []
    for partida in lista_partidas:
        partida = partida.split(',')
        if (partida[5] == time or partida[6] == time):
            lista_de_jogos.append(partida)
    return lista_de_jogos

def calcular_pontos_do_time(time):
    pontuacao = 0
    resultado_partidas = buscar_jogos_por_time(time)
    for partida in resultado_partidas:
        if (partida[11] == time): pontuacao += 3
        elif (partida[11] == "-"): pontuacao += 1
    return pontuacao

time = input("Informe o time: ")
pontos = calcular_pontos_do_time(time)
print(f"{time} fez {pontos} pontos!")
print("Fim do programa!")
