import sqlite3 as sq

conn = sq.connect('sistema_prod.db')

cursor = conn.cursor()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        quantidade INTEGER,
        preco REAL
    );
'''
cursor.execute(create_table_query)

conn.commit()


