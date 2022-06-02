from os import system, name

def clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')
clear()

valor_total = float(input('Informe o valor total do consumo: R$'))
num_pessoas = int(input('Informe o total de pessoas: '))
perc_serv = float(input('Informe o percentual do serviço, entre 0 e 100: '))
perc_serv = perc_serv/100


valor_final = valor_total + (valor_total * perc_serv)
valor_dividido = valor_final / num_pessoas

valor_final = str(valor_final)     # Converte o valor para uma string
valor_final.replace('.', ',')      # Substitui pontos por vírgulas

# O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
# Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro
# “Valor inválido” e o programa deve ser interrompido.

print(f'O valor total da conta, com a taxa de serviço, será de R${valor_dividido}')
print(f'Dividindo a conta por {num_pessoas} pessoa(s), cada pessoa deverá pagar R${valor_final}.')

# O programa deve verificar se o número total de pessoas é maior do que zero.
# O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
# Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e o programa deve ser interrompido.