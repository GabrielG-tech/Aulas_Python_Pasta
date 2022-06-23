# Crie um programa contendo uma função que, dados um valor de renda mensal total,
# gastos totais com moradia, gastos totais com educação e gastos totais com transporte,
# faça um diagnóstico da saúde financeira do usuário, com base nos valores percentuais acima expostos,
# informando qual é o percentual da renda mensal total comprometido por cada custo. 

renda_mensal_total = float(input('Renda mensal total: '))
gasto_moradia = float(input('Gasto com moradia: '))
gastos_totais_educacao = float(input('Gasto com educação: '))
gastos_totais_transporte = float(input('Gasto com transporte: '))

# Se o gasto estiver dentro do percentual recomendado, informe ainda que:
# "Seus gastos estão dentro da margem recomendada."

# Caso contrário, informe:
# "Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_max}"
valor_max_moradia = renda_mensal_total * 0.3
valor_max_educacao = renda_mensal_total * 0.2
valor_max_transporte = renda_mensal_total * 0.15

print('valor_max_moradia = {}, valor_max_educacao = {}, valor_max_transporte = {}'.format(valor_max_moradia, valor_max_educacao, valor_max_transporte))


#def diagnostico_financeira_usuario():
#    if gasto_moradia/renda_mensal_total <= 0.3 and gastos_totais_educacao/renda_mensal_total <= 0.2 and gastos_totais_transporte/renda_mensal_total <= 0.15:
#        print("Seus gastos estão dentro da margem recomendada.")
#    elif :
#        print(f"Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_max}")

# Onde "tipo" deve ser moradia, educação ou transportes e "valor_max"
# deve ser o valor equivalente ao percentual máximo de gasto com esse tipo de custo.

# Exemplo de saída do programa:

# Renda mensal total: R$ 5000
# Gastos totais com moradia: R$ 1760
# Gastos totais com educação: R$ 800
# Gastos totais com transporte: R$ 300

# Diagnóstico:
# Seus gastos totais com moradia comprometem 35.2% de sua renda total.
# O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ 1500.

# Seus gastos totais com educação comprometem 16% de sua renda total.
# O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.

# Seus gastos totais com transporte comprometem 6% de sua renda total.
# O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.
