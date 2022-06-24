def diagnostico_financeiro_usuario():
    # Coleta de dados
    renda_mensal_total = float(input('Renda mensal total: '))
    moradia = float(input('Gasto com moradia: '))
    educacao = float(input('Gasto com educação: '))
    transporte = float(input('Gasto com transporte: '))

    # Calculo de valor_max
    valor_max_moradia = renda_mensal_total * 0.3
    valor_max_educacao = renda_mensal_total * 0.2
    valor_max_transporte = renda_mensal_total * 0.15

    # Transformar em % e arredondar
    perc_moradia = moradia/renda_mensal_total * 100
    perc_educacao = educacao/renda_mensal_total * 100
    perc_transporte = transporte/renda_mensal_total * 100
    perc_moradia = round(perc_moradia, 1)
    perc_educacao = round(perc_educacao, 1)
    perc_transporte = round(perc_transporte, 1)

    print('Diáginostico: ')
    if perc_moradia <= 30:
        print(f'Seus gastos totais com moradia comprometem {perc_moradia}% de sua renda total. O máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada.')
    else:
        print(f'Seus gastos totais com moradia comprometem {perc_moradia}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${valor_max_moradia}')
    if perc_educacao <= 20:
        print(f'Seus gastos totais com moradia comprometem {perc_educacao}% de sua renda total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.')
    else:
        print(f'Seus gastos totais com moradia comprometem {perc_educacao}% de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com educacao deveria ser de R${valor_max_educacao}')
    if perc_transporte <= 15:
        print(f'Seus gastos totais com moradia comprometem {perc_transporte}% de sua renda total. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.')
    else:
        print(f'Seus gastos totais com moradia comprometem {perc_transporte}% de sua renda total. O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R${valor_max_transporte}')
diagnostico_financeiro_usuario()
