import sqlite3 as sq


class Produtos:
    def __init__(self,banco):
        self.banco = banco#Conexão com banco
    
    '''Função para inserit produtos'''
    def insert_prod(self,id,nome,categoria,quantidade,preco):
        
        conn = sq.connect(self.banco)
        cursor = conn.cursor()
        
        query = '''
            SELECT * FROM produtos
            WHERE id = ?;'''
            
        cursor.execute(query,(id,))
        result = cursor.fetchone()
        '''
        Tratamento de erros
        '''
        try: 
            id = int(id)
            nome = str(nome).capitalize()
            categoria = str(categoria).capitalize()
            quantidade = int(quantidade)
            preco = float(preco)
            
            insert_dados ='''
            INSERT INTO produtos (id,nome,categoria,quantidade,preco)
            VALUES (?,?,?,?,?)
            '''
            if not result:
                dados = (id,nome,categoria,quantidade,preco)
                cursor.execute(insert_dados,dados)
                conn.commit()
                return True
            else:
                return False
            
        except sq.Error as e:
            return f'Erro de conexão com o bando de dados: {e}'
            
        finally:
            conn.close()

    #Função para atualizar dados
    def update_prod(self,id,nome,categoria,quantidade,preco):
        
        conn = sq.connect(banco)
        cursor = conn.cursor()
        try:
            dados_update = (nome,categoria,quantidade,preco,id)
            
            update_query = '''
            UPDATE produtos
            SET  nome = ?, categoria = ?, quantidade = ?, preco = ?
            WHERE id = ?
            '''
            
            cursor.execute(update_query,dados_update)
            conn.commit()
            
            return True
        
        except sq.Error as e:
            return f'Erro de conexão com o banco: {e}'

    #Buscando informações
    def buscando_prod(self,id):
        
        conn = sq.connect(self.banco)
        cursor = conn.cursor()
        
        try:
            query = '''
                SELECT *
                FROM produtos
                WHERE id = ?;
            '''
            
            cursor.execute(query,(id,))
            resultado = cursor.fetchall()
            
            infor_produto = {}
            
            for produto in resultado:
                
                infor_produto = {
                    'id':produto[0],
                    'nome':produto[1],
                    'categoria':produto[2],
                    'quantidade':produto[3],
                    'preco':produto[4]
                }
                
            return infor_produto
        
        except sq.Error as e:
            return f'Erro de conexão com o banco: {e}'

        finally:
            conn.close()


    def deletar_produto(self,id):
        
        conn = sq.connect(self.banco)
        cursor = conn.cursor()
        
        try:
            query = '''
                DELETE FROM produtos
                WHERE id = ?
            '''
            
            cursor.execute(query,(id,))
            
            conn.commit()
            
            
        except sq.Error as e:
            return f'Erro de conexão com o banco: {e}'

        finally:
            conn.close()
            
banco = './db/sistema_prod.db'
acesso = Produtos(banco)




