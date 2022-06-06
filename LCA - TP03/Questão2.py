from os import system, name
def clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')
clear()

# Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:
idade = int(input('Informe sua idade: '))

# Fluxo de exceção: 
# Verificar se a idade da pessoa é maior do que zero.
if idade > 0:
    # Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
    if idade >= 18 and idade < 70:
        print('\033[33mEleitor obrigatório\033[m')

    # Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
    elif idade >= 16 and idade < 18 or idade >= 70:
        print('\033[33mEleitor facultativo\033[m')

    # Não tem direito a voto (menor de 16 anos).
    elif idade < 16:
        print('\033[31mNão tem direito a voto\033[m')

else:
    print('\033[31mValor inválido\033[m')
