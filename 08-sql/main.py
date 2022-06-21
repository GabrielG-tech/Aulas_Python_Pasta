import sqlite3
banco_de_dados = '08-sql/database.db'

conn = sqlite3.connect(banco_de_dados)

# Criar tabela com SQL
com_criar_tabela_pessoa = '''
CREATE TABLE IF NOT EXISTS pessoas
    (nome TEXT, sobrenome TEXT, idade INTEGER)
'''

conn.execute(com_criar_tabela_pessoa)
conn.commit()

# Inserir dados com SQL
com_inserir_dados = '''
INSET INTO pessoas VALUES ('fulano', 'de tal', 90)
'''

# conn.execute(com_inserir_dados)
# conn.commit()

cursor = conn.cursor()
for pessoa in cursor.execute("SELECT * FROM pessoas"):
    print(pessoa)

conn.close()