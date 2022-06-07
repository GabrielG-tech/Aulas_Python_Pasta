#
# Altere o código para usar Estruturas (Classes)
#

# Define uma estrutura (classe)
class Driver:
    def __init__(self, driverId, forename, surname, nationality):
        self.driverId = driverId            # 0
        self.forename = forename            # 4
        self.surname = surname              # 5
        self.nationality = nationality      # 7

    def __str__(self):
        return f"#{self.driverId} {self.forename} {self.surname} ({self.nationality})"

class Race: 
    def __init__(self, id, y, n):
        self.raceId = id
        self.year = y
        self.name = n

    def __str__(self) -> str:
        return f"#{self.raceId} {self.year} ({self.name})"

class Result:
    def __init__(self, resultId, raceId, driverId, points):
        self.resultId = resultId
        self.raceId = raceId
        self.driverId = driverId
        self.points = points

    def __str__(self) -> str:
        return f"#{self.resultId} {self.raceId} {self.driverId} - {self.points}"

'''
def tratar_dados_do_arquivo(arquivo):
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
'''

def pegar_conteudo_arquivo(arquivo):
    file = open(arquivo)
    conteudo = file.read().splitlines()
    file.close()
    return conteudo

def tratar_dados_dos_races():
    dados = []
    for item in pegar_conteudo_arquivo('06-Arqvs\Exercicios\\f1\\02races.csv'):
        race = item.split(',')
        corridaId = race[0].strip("\"")
        ano = race[1].strip("\"")
        nome = race[4].strip("\"")
        dados.append(Race(corridaId, ano, nome))
    return dados

def tratar_dados_dos_drivers():
    dados = []
    for item in pegar_conteudo_arquivo('06-Arqvs\Exercicios\\f1\\00drivers.csv'):
        driver = item.split(',')
        driverId = driver[0].strip("\"")
        forename = driver[4].strip("\"")
        surname = driver[5].strip("\"")
        nationality = driver[7].strip("\"")
        dados.append(Driver(driverId, forename, surname, nationality))
    return dados

def tratar_dados_dos_results():
    dados = []
    for item in pegar_conteudo_arquivo('06-Arqvs\Exercicios\\f1\\03results.csv'):
        result = item.split(',')
        resultId = result[0].strip("\"")
        raceId = result[1].strip("\"")
        driverId = result[2].strip("\"")
        points = result[9].strip("\"")
        dados.append(Result(resultId, raceId, driverId, points))
    return dados

drivers = tratar_dados_dos_drivers()
races = tratar_dados_dos_races()
result = tratar_dados_dos_results()
for resultado in result:
    print(resultado)

'''# print(races)
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