# retorno_print = print()
# retorno_input = input()
# nome_funcao()

#   rotulo(lista de tipos parâmetros) <- assinatura da função
def nome_funcao(parm1, parm2):
    print("Parâmetro 1:", parm1)
    print("Parâmetro 2:", parm2)
    print("Função nova.") # desenha no console
    return "Fim da função." # devolve para quem a chamou

# def nome_funcao():
#    print("Outra Função nova.")
#    return "Fim da função."

# print(parm1)
retorno_funcao = nome_funcao("Parm1", "Parm2")
print(retorno_funcao, "\n", "Fim do programa.")


def calcular_reajuste(salario):
    return salario + 1000.0

reajuste = calcular_reajuste(2000.0)

# rejuste...



def soma(numA, numB):
    # print(numA + numB)
    return numA + numB

retorno_soma = soma(10.0, 8.6)
media = retorno_soma/ 2