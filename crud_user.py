import sqlite3 as sq

class Users:
    def __init__(self, banco):
        self.banco = banco
        
    # Consultando no banco:
    def query(self, email):
        conn = sq.connect(self.banco)
        cursor = conn.cursor()
        
        query = '''
            SELECT * FROM usuarios;
        '''
        
        try:
            cursor.execute(query)
            resultados = cursor.fetchall()
            
            for res in resultados:
                if res[0] == email:
                    return True
        
        except sq.Error as e:
            return f'Erro ao conectar ao banco: {e}'
        
        finally:
            cursor.close()
            conn.close()
        
        return False
        
    # Cadastrar usuario
    def cadastrar_user(self, email, user, senha):
        if self.query(email):
            return 'Email já cadastrado'
        
        if email == '' or user == '' or senha == '':
            return 'Todos os campos devem ser preenchidos!'
        
        conn = sq.connect(self.banco)
        cursor = conn.cursor()
        
        insert = '''
            INSERT INTO usuarios (email, nome, senha)
            VALUES (?, ?, ?)
        '''
        
        dados_user = (email, user, senha)
        
        try:
            cursor.execute(insert, dados_user)
            conn.commit()
            return True
        
        except sq.Error as e:
            return f'Erro ao inserir usuário: {e}'
        
        
        finally:
            cursor.close()
            conn.close()
            
    #Acesso ao menu
    def acesso(self, user, senha):
        conn = sq.connect(self.banco)
        cursor = conn.cursor()
        
        query = '''
            SELECT * FROM usuarios 
            WHERE nome = ? AND senha = ?
        '''
        
        try:
            cursor.execute(query, (user, senha))
            resultado = cursor.fetchone()  
            dados_user = {}
            
            if resultado:
                dados_user = {
                    'nome':resultado[1]
                }
                    
                return dados_user
            else:
                return False
            
        except sq.Error as e:
            return f'Erro ao conectar ao banco: {e}'
        
        finally:
            conn.close()

banco = './db/sistema_prod.db'       
users = Users(banco)

