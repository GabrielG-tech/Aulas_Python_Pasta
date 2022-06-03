#
# Altere o código para usar Estruturas (Classes)
#

# Define uma estrutura (classe)
from ast import Set


class Corrida: pass

class Resultado: pass

def tratar_dados_do_arquivo(arquivo, tipo):
    file = open(arquivo)
    lista = file.read().splitlines()
    file.close()
    dados = []
    # Pega os atributos na primeira linha do arquivo
    atributos = lista.pop(0).split(',')
    for item in lista:
        dados_dic = {}
        dados_tratar = item.split(',')
        for i in range(len(atributos)):
            dados_dic[atributos[i]] = dados_tratar[i]
            # piloto[atributo[0]] = "valor"
            # piloto.moto = ""
        dados.append(dados_dic)
    return dados

drivers = tratar_dados_do_arquivo('06-Arqvs\Exercicios\\f1\\00drivers.csv')
races = tratar_dados_do_arquivo('06-Arqvs\Exercicios\\f1\\02races.csv')
results = tratar_dados_do_arquivo('06-Arqvs\Exercicios\\f1\\03results.csv')
'''
# print(drivers)
# print(races)
# print(results)

def pegar_corridas_de_temporada(ano):
    corridas_temporada = []
    for race in races:
        if race['year'] == str(ano):
            corridas_temporada.append(race)
    return corridas_temporada

# print(pegar_corridas_de_temporada(2009))
'''

'''
def pegar_id_do_piloto(nome):
    pilotos = []
    for driver in drivers:
        if driver['forename'].strip("\"") == nome:
            pilotos.append(driver)
    if (len(pilotos) == 1): return pilotos[0][0]
    # não encontrou um piloto
    # ha mais do que um piloto
'''

'''
def pegar_id_do_piloto(nome, sobrenome):
   for driver in drivers:
       tem_nome = driver['forename'].strip("\"") == nome
       tem_sobrenome = driver['surname'].strip("\"") == sobrenome
       if tem_nome and tem_sobrenome:
           return driver['driverId']

# print(pegar_id_do_piloto("Nico", "Rosberg"))

def pegar_ids_das_corridas_da_temporada(ano):
    ids_das_corridas = []
    lista_corridas_temporada = pegar_corridas_de_temporada(ano)
    for corrida in lista_corridas_temporada:
        ids_das_corridas.append(corrida['raceId'])
    return ids_das_corridas

# print(pegar_ids_das_corridas_da_temporada(2009))


def pegar_resultados_do_piloto_na_temporada(nome, sobrenome, ano):
    resultados = []
    id_piloto = pegar_id_do_piloto(nome, sobrenome)         # id vazio
    ids_corridas = pegar_ids_das_corridas_da_temporada(ano) # lista 
    # print(id_piloto)
    # print(ids_corridas)
    for resultado in results:
        tem_corrida = resultado['raceId'] in ids_corridas
        tem_piloto = resultado['driverId'] == id_piloto
        if (tem_corrida and tem_piloto):
            resultados.append(resultado)
    return resultados

# print(pegar_resultados_do_piloto_na_temporada("Nico", "Rosberg", 2009))

def exibir_pontuacao_piloto_na_temporada(nome, sobrenome, ano):
    total_pontos = 0
    resultados = pegar_resultados_do_piloto_na_temporada(nome, sobrenome, ano)
    if (len(resultados) > 0):
        for resultado in resultados:
            total_pontos += float(resultado['points'])
        return f"{nome} {sobrenome} \t Temporada {ano}: \t {total_pontos}"
    # else: return None

# print(exibir_pontuacao_piloto_na_temporada("Nico", "Rosberg", 2009))

def pegar_todas_temporadas():
    temporadas = []
    for corrida in races:
        ano = corrida['year']
        if not ano in temporadas:
            temporadas.append(ano)
    return temporadas

# print(pegar_todas_temporadas())

def exibir_pontuacoes_do_piloto(nome, sobrenome):
    for ano in pegar_todas_temporadas():
        resultado_temp = exibir_pontuacao_piloto_na_temporada(nome, sobrenome, ano)
        if resultado_temp != None:
            print(resultado_temp)

# Menu de interação
def app():
    exibir_pontuacoes_do_piloto('Nico', 'Rosberg')
    # Retornar todas as corridas de uma temporada
    # Retornar os resultados de um piloto em uma temporada
    # Retornar a pontuação total de um piloto em cada temporada
    # Itens extras
    # Buscar informações de um piloto buscando pelo seu nome ou sobrenome
    # Buscar informações de um circuito pelo seu país

# app()
'''