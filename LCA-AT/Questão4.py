# A. Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, como entrada,
# um montante financeiro inicial, um percentual de rendimento por período,
# um valor de aporte para cada período e uma quantidade de períodos.

# B. Crie uma função que exiba um gráfico da evolução do valor acumulado,
# tendo como eixo das abscissas (horizontal) o número de períodos e,
# no eixo das ordenadas (vertical), o valor acumulado, em reais.

import matplotlib.pyplot as plt

def calcular_juros_compostos(valor_inicial, quant_aporte, juros_mensais, periodos):
    valor_total = valor_inicial
    valor_total_grafico = []
    valor_total_periodo = []
    for item in range(periodos):
        valor_total += (valor_total * juros_mensais)/100
        valor_total += quant_aporte 
        valor_total_grafico.append(round(valor_total))
        valor_total_periodo.append(item)
        print(f'Após {item} períodos(s), o montante será de R${round(valor_total, 2)}.')
    plt.plot(valor_total_periodo, valor_total_grafico)
    plt.show()

def aplicar_juros_dados_usuario():
    valor_inicial = float(input("Valor inicial: R$ "))
    rendimento_periodo = float(input("Rendimento por período (%): "))
    quant_aporte =  float(input("Aporte a cada período: R$ "))
    periodos = int(input("Quantidade total de períodos: "))
    calcular_juros_compostos(valor_inicial, quant_aporte, rendimento_periodo, periodos)
aplicar_juros_dados_usuario()