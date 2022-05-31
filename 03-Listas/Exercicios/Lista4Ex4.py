# Crie um algoritmo que 
# remova duplicatas de 
# uma lista.

lista = [1,5,6,4,6,2,5,3,1,5,1,2,3,4,5,6,1,2,3,4,5]
lista_limpa = []

for item in lista:
    if item not in lista_limpa:
        lista_limpa.append(item)

lista_limpa.sort()
print(lista_limpa)

# Crie um algoritmo que analise duas listas 
# e informe quantos e quais elementos 
# elas possuem em comum.

listaA = [1,6,9,30]
listaB = [2,6,8,30]
listaC = []

# for num in listaA and listaB:
#    print(num)

for num in listaA and listaB: 
    if num in listaA:
        listaC.append(num)

print(len(listaC))
print(listaC)

# Jogo da velha

