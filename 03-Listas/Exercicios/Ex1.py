# Calcule a média em uma lista de notas.
notas = [6.0, 8.0]
somatorio = 0

for nota in notas:
    somatorio = somatorio + nota

quant_notas = len(notas)
media = somatorio / quant_notas

print("A média foi de: ", media)

