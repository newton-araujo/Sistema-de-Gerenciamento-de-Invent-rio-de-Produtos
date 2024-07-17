import sqlite3 as sq

conn = sq.connect('sistema_prod.db')

cursor = conn.cursor()

create_user = '''
    CREATE TABLE IF NOT EXISTS usuarios (
        email TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL
    )
'''

cursor.execute(create_user)

conn.commit()
cursor.close()
conn.close()