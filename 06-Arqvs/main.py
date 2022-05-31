# Leitura e escrita em Arquivos

# open('end/nome.arqv') -> 
#   objeto de manipulação do arquivo

def escrever_arquivo():
    arqv = open('06-Arqvs/dados.txt', mode = 'a') # Modo escrita
    arqv.write("Novo Conteudo do arquivo: 08:29.\n")
    print("Conteudo com print", file=arqv)
    arqv.close()

def ler_arquivo():
    # mode = 'w', modo escrita - sobreescrever
    # mode = 'r', modo leitura - padrão
    # mode = 'a', modo escrita - no final do arquivo
    arqv = open('06-Arqvs/dados.txt', mode = 'r') # Modo escrita

    # Ler o arquivo todo
    conteudo = arqv.read() # String

    # Imprimir o conteudo no terminal
    print(conteudo)
    # operações

    arqv.close()

escrever_arquivo()
ler_arquivo()