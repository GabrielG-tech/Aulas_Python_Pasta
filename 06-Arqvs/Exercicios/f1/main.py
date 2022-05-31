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

def pegar_corridas_de_temporada(ano):
    corridas_temporada = []
    for race in races:
        if race[1] == str(ano):
            corridas_temporada.append(race)
    return corridas_temporada

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
    ids_corridas = pegar_ids_das_corridas_da_temporada(ano) # lista 
    # print(id_piloto)
    # print(ids_corridas)
    for resultado in results:
        if (resultado[1] in ids_corridas and resultado[2] == id_piloto):
            resultados.append(resultado)
    return resultados

def exibir_pontuacao_piloto_na_temporada(nome, sobrenome, ano):
    total_pontos = 0
    resultados = pegar_resultados_do_piloto_na_temporada(nome, sobrenome, ano)
    for resultado in resultados:
        total_pontos += float(resultado[9])
    return f"{nome} {sobrenome} \t Temporada {ano}: \t {total_pontos}"

def pegar_todas_temporadas():
    temporadas = []
    for corrida in races:
        ano = corrida[1]
        if not ano in temporadas:
            temporadas.append(ano)
    return temporadas

def exibir_pontuacoes_do_piloto(nome, sobrenome):
    for ano in pegar_todas_temporadas():
        print(exibir_pontuacao_piloto_na_temporada(nome, sobrenome, ano))

# Menu de interação
def app():
    exibir_pontuacoes_do_piloto('Nico', 'Rosberg')
    # Retornar todas as corridas de uma temporada
    # Retornar os resultados de um piloto em uma temporada
    # Retornar a pontuação total de um piloto em cada temporada
    # Itens extras
    # Buscar informações de um piloto buscando pelo seu nome ou sobrenome
    # Buscar informações de um circuito pelo seu país

app()