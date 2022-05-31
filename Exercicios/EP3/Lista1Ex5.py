# Um motorista deseja abastecer 
# um valor X em reais, de combustível. 
# Escreva um algoritmo para 
# ler o preço do litro do combustível 
# e o valor que o motorista deseja abastecer. 
# Em seguida, informe quantos litros 
# foram abastecidos.

valor_a_abastecer = float(input("Informe o valor (R$): "))
valor_da_gasolina = float(input("Informe o preço da Gasolina: "))


quant_litros = valor_a_abastecer / valor_da_gasolina
print(f"A quantidade foi de: {quant_litros:.6f}")