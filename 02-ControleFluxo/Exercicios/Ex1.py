# Carteira de Habilitação
# A: Motos e Triciclos
# B: Carros de Passeio
# C: Acima de 3,5 ton
# D: + de 8 passageiros
# E: Unidades acopladas + 6
# Escrever uma função que receba a
#  categoria do motorista e informe 
# quais veículos ele pode dirigir

categoria = input("Informe a sua categoria: ")

if (categoria == "a"):
    print("Motos e Triciclos")
elif categoria == "b":
    print("Carros de passeio")
elif categoria == "c":
    print("Acima de 3.5 ton")
elif categoria == "d":
    print("+ de 8 passageiros")
elif categoria == "e":
    print("Unidades acopladas")
else:
    print("Categoria desconhecida.")

print("Fim do programa.")