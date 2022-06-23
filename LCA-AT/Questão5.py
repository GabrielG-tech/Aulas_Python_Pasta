import pandas as pd

pib = pd.read_csv("LCA-AT/Assessment_PIBs - modelo 1.csv")
pib_quantidade = len(pib.columns)

def pegar_pib_pais(pais, ano):
    for i in range(0, pib_quantidade):
        if pib["País"][i] == pais:
            ano_encontrado = pib.loc(i)
            return ano_encontrado[ano]

def perguntar_dados_usuario():
    pais = input('País: ')
    ano = str(input("Ano: "))
    pib_pais = pegar_pib_pais(pais, ano)
    return print(f'PIB do {pais}: US${pib_pais} trilhões')

perguntar_dados_usuario()
