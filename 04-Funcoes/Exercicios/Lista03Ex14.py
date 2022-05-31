# Crie um função que detecta se uma string é 
# ou não um palíndromo.

# Um palíndromo é uma sequência de 
# caracteres que lida igualmente da esquerda 
# para a direita ou da direita para a esquerda.

# Exemplos: “ABBA”, “RACECAR”, “AMOR A ROMA”, 
# “ SUBI NO ÔNIBUS”(sem contar os espaços e 
# caracteres especiais…)

# Obs: Em python, o conceito de x[::-1] 
# a listas e strings resolve o problema de maneira imediata, 
# mas não é solução ótima.

def eh_palindromo(texto):
    texto_inverso = texto[::-1]
    eh_pali = texto_inverso == texto
    # print(eh_pali)
    return eh_pali

entrada = input("Informe um texto: ")
retorno = eh_palindromo(entrada)
print("É Palindromo:\t", retorno)

# JogoDaVelhaFull.por
