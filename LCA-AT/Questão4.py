# A. Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, como entrada,
# um montante financeiro inicial, um percentual de rendimento por período,
# um valor de aporte para cada período e uma quantidade de períodos.

# B. Crie uma função que exiba um gráfico da evolução do valor acumulado,
# tendo como eixo das abscissas (horizontal) o número de períodos e,
# no eixo das ordenadas (vertical), o valor acumulado, em reais.


















# ========= Dagoberto ============

# import matplotlib.pyplot as plt

# def pegar_dados ():
#     dados = []  # 0 Valor inicial /  1 Redimento p/periodo / 2 Aporte / 3 Total de periodos
#     dados.append(float(input("Valor inicial: R$ ")))
#     dados.append(float(input("Aporte a cada período: R$ ")))
#     dados.append(float(input("Rendimento por período em %: ")))
#     dados.append(int(input("Quantidade de períodos: ")))
#     return dados

# def juros (dados) :
#      global valor_grafico
#      global valor_periodo
#      valor = dados[0]
#      valor_grafico = []
#      valor_periodo = []
#      for i in range(dados[3]):
#          valor += (valor * dados[1]) / 100
#          valor += dados[2]
#          print("Após {} períodos(s), o montante será de R${}".format(i+1, round(valor, 2)))
#          valor_grafico.append(round(valor))
#          valor_periodo.append(i)
#      plt.plot(valor_periodo, valor_grafico)
#      plt.show()


# dados = pegar_dados()
# juros(dados)
