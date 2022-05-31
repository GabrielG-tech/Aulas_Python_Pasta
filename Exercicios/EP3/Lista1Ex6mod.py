# Crie um algoritmo para 
# calcular a média de duas notas digitadas pelo usuário, 
# sendo que a segunda nota tem peso dois.
# E informe se ele passou ou não (nota maior que 7.0) 

nota_1 = float(input("Informe a primeira nota: "))
nota_2 = float(input("Informe a segunda nota: "))

media = (nota_1 + nota_2 * 2) / 3
passou = media >= 7

print(f"Média do aluno: {media:.2f}")
print(f"Aprovado: {passou}")