# Insira um conteúdo no formato 
# CSV (comma separated values), 
# considerando cada linha 
# como o registro de uma entidade 
# de um domínio qualquer e, 
# cada valor, um atributo deste registro.
# Exemplo: nome, marca, valor, quantidade
# DICAS: 	
#   splitlines() -> String -> 
#       retorna uma lista com as linhas
#	split(‘,’)	 -> String -> 
#        retorna uma lista com cada elementos separado por ','

nome_arquivo = "06-Arqvs/Exercicios/bancodedados.db"
mode_de_abertura = 'r'

# arquivo = open(nome_arquivo, mode_de_abertura)
# conteudo = arquivo.read()
# Lista de Strings
# itens = conteudo.splitlines()

with open(nome_arquivo, mode_de_abertura) as arquivo:
    print("Nome\tMarca\t\tPreço\tQuant.")
    for item in arquivo:
        item = item.split(',')
        print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}", end="")

print("\nFim do programa.")

# arquivo.close()