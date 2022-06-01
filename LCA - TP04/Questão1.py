from os import system, name

def clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')
clear()

valor_total = float(input('Informe o valor total do consumo: R$'))
num_pessoas = input('Informe o total de pessoas: ')
perc_serv = float(input('Informe o percentual do serviço, entre 0 e 100: '))

def verificação():
    while num_pessoas >= 0 or num_pessoas != int:
        num_pessoas = input('Valor inválido\nPorfavor insira outro valor: ')
    while valor_total >= 0:
        valor_total = input('Valor inválido\nPorfavor insira outro valor: ')
    while 0 < perc_serv < 100:
        valor_total = input('Valor inválido\nPorfavor insira outro valor: ')
        
#def dividir_conta(): 
#    valor_dividido = valor_final / num_pessoas


valor_final = valor_total + (valor_total * perc_serv)


valor_final = str(valor_final)     # Converte o valor para uma string
valor_final.replace('.', ',')      # Substitui pontos por vírgulas

# O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
# Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro
# “Valor inválido” e o programa deve ser interrompido.

print(f'O valor total da conta, com a taxa de serviço, será de R${valor_dividido}')
print(f'Dividindo a conta por {num_pessoas} pessoa(s), cada pessoa deverá pagar R${valor_final}.')
