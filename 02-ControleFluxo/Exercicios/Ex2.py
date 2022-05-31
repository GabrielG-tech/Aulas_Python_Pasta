# Exercícios
# Criar um jogo em que o usuário 
# terá que acertar um número que 
# pode ser de 1 a 6 em 5 
# lançamentos de um dado.

# Dica
# random
import random
random.randint(0,10)

# para x em [1,5] faça
for x in range(5):
#  pegar um número do usuário
    aposta = int(input("Escolha um número de 1 a 6: "))
#  sortear um número aleatório de 1 a 6
    resultado = random.randint(1,6)
#  verificar se o número do usuário é igual ao número sorteado
    if aposta == resultado :
#    se sim, informar que o usuário ganhou um ponto
        print("Acertou!")
#    se não, informar que ele errou
    else: print(f"Errou! Resultado:\t {resultado}")

# fim do programa.
print("Fim do programa.")