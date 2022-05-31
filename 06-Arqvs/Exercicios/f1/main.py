def tratar_dados_do_arquivo(arquivo):
    file = open(arquivo)
    lista = file.read().splitlines()
    file.close()
    dados = []
    for item in lista:
        dados.append(item.split(','))
    return dados

drivers = tratar_dados_do_arquivo('06-Arqvs\Exercicios\\f1\\00drivers.csv')
races = tratar_dados_do_arquivo('06-Arqvs\Exercicios\\f1\\02races.csv')
results = tratar_dados_do_arquivo('06-Arqvs\Exercicios\\f1\\03results.csv')

# Retornar todas as corridas de uma temporada
def pegar_corridas_de_temporada(ano):
    corridas_temporada = []
    for race in races:
        if race[1] == str(ano):
            corridas_temporada.append(race)
    return corridas_temporada

# Retornar os resultados de um piloto em uma temporada
'''
def pegar_id_do_piloto(nome):
    pilotos = []
    for driver in drivers:
        if driver[4].strip("\"") == nome:
            pilotos.append(driver)
    if (len(pilotos) == 1): return pilotos[0][0]
    # não encontrou um piloto
    # ha mais do que um piloto
'''

def pegar_id_do_piloto(nome, sobrenome):
   for driver in drivers:
       tem_nome = driver[4].strip("\"") == nome
       tem_sobrenome = driver[5].strip("\"") == sobrenome
       if tem_nome and tem_sobrenome:
           return driver[0]

def pegar_ids_das_corridas_da_temporada(ano):
    ids_das_corridas = []
    lista_corridas_temporada = pegar_corridas_de_temporada(ano)
    for corrida in lista_corridas_temporada:
        ids_das_corridas.append(corrida[0])
    return ids_das_corridas

def pegar_resultados_do_piloto_na_temporada(nome, sobrenome, ano):
    resultados = []
    id_piloto = pegar_id_do_piloto(nome, sobrenome)         # id vazio
    ids_corridas = pegar_ids_das_corridas_da_temporada(ano) # lista vazia
    for resultado in results:
        if (resultado[1] in ids_corridas and resultado[2] == id_piloto):
            resultados.append(resultado)
    return resultados


# Retornar a pontuação total de um piloto em cada temporada

def app():
    # print(pegar_id_do_piloto('Jean', 'Alesi'))
    # print(pegar_id_do_piloto('Nelson', 'Piquet'))
    resultados = pegar_resultados_do_piloto_na_temporada('Nico', 'Rosberg', 2009)
    print("Posição\tPontos")
    for resultado in resultados:
        print(f"{resultado[6]}\t{resultado[9]}")

app()
