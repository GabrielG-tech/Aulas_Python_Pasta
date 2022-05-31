# Crie um algoritmo que 
# calcule o novo valor de 
# um salário a partir 
# de um valor percentual 
# de reajuste. 
# O valor atual do salário e 
# o valor percentual do reajuste 
# devem ser informados pelo usuário 
# como, por exemplo, 7,3%.

salario = float(input("Salário: "))
reajuste = float(input("Reajuste: "))

salario = salario * (1 + reajuste)

print(f"Novo Salário: {salario}")