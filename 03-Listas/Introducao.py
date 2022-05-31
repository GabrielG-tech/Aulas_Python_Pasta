lista = [1, 2, 3, 4, 5]
estados = ['RJ', 'SP', 'MG', 'ES']

print(lista)
print(estados)
             #  0      1     2  3 
outra_lista = ['um', 'dois', 3, 4]
pessoa = ['Fulano', 'De Tal', 90, 2000.0]
print(outra_lista)

nome = pessoa[0]
salario = pessoa[3]
print(nome)
print("Salário: R$ ", salario)

quant = len(estados)
print(estados[quant-1])

for estado in estados:
    print("Estado: ", estado)

for estado in outra_lista:
    print("Estado: ", estado)


matriz = [
    [],
    []
]

matriz[0][0]