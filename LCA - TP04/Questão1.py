from os import system, name

def clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')
clear()

valor_total = float(input('Informe o valor total do consumo: R$'))
num_pessoas = int(input('Informe o total de pessoas: '))
if num_pessoas <= 0:
    print('\033[1;31m'+'Valor inválido'+ '\033[m')
    exit()

perc_serv = float(input('Informe o percentual do serviço, entre 0 e 100: '))
if perc_serv < 0 or perc_serv > 100:
    print('\033[1;31m'+'Valor inválido'+ '\033[m')
    exit()
perc_serv = perc_serv/100

# Verifica se o % do serviço entre 0 a 100 e se o núm total de pes é +0
# e calcula o preço totale o preço por pessoa

valor_final = valor_total + (valor_total * perc_serv)
valor_dividido = valor_final / num_pessoas
valor_final = str(valor_final).replace('.', ',')        # Converte o valor para uma string e Substitui pontos por vírgulas
valor_dividido = str(valor_dividido).replace('.', ',')  # Converte o valor para uma string e Substitui pontos por vírgulas
num_pessoas =str(num_pessoas)

print('O valor total da conta, com a taxa de serviço, será de ' + '\033[1mR$' + valor_final + '\033[m.')
print('Dividindo a conta por ' + '\033[1m' + num_pessoas + ' pessoa(s)\033[m, cada pessoa deverá pagar ' + '\033[1mR$' + valor_dividido + '\033[m.')
