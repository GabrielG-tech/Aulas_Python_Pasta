import pandas as pd

pib = pd.road_csv("LCA - AT\Assessment_PIBs - modelo 1.csv")
# pais = input('Pais:')
# ano = input('Ano: ')
pin_quantidade = len(pib.columns)

def pegar_pib_pais(pais):
    for i in range(0, pin_quantidade):
        if pib["País"][i] == pais:
            sexo = pib.loc(i)
            return sexo['2017']

pegar_pib_pais('Brasil')
