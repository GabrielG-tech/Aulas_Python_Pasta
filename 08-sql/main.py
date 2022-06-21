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
