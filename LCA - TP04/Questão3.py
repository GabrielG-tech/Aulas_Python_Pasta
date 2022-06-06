from os import system, name
def clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')
clear()

nota_vencedor = 0
vencedor = ''
for participante in range(5):
    p = str(input(f'Informe nome do {participante + 1}º participante: '))
    n = float(input(f'Informe nota do {participante + 1}º participante: '))
    # verificar se a nota da pessoa é >= 0 and <= 10.
    if n >= 0 and n <= 10:
        if n > nota_vencedor:
            nota_vencedor = n
            vencedor = p
    else:
        print('\033[1;31mError\033[m')
        break

print(f'O(a) vencedor(a) foi \033[1;33m{vencedor}\033[m com nota \033[1;32m{nota_vencedor}\033[m!')
