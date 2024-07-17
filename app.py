import ttkbootstrap as ttk
from tkinter import IntVar,StringVar,DoubleVar
from ttkbootstrap.constants import *
from tkinter import Toplevel, messagebox
from crud_user import Users  # Assuming you have a Users class defined for user management
from crud_prod import Produtos


banco = './db/sistema_prod.db'
request = Users(banco)
request_prod = Produtos(banco)

class Myapp:
    def __init__(self, root):
        self.root = root
        
        # Login - TELA DE LOGIN
        self.login_frame = ttk.Frame(self.root, padding=20)
        self.login_frame.pack(fill='both', expand=False)
        
        self.title_login = ttk.Label(self.login_frame, text='Login', font=('Helvetica', 20))  # Titulo do login
        self.title_login.grid(row=0, column=1, columnspan=2, padx=10, sticky='NSEW')
        
        self.label_user = ttk.Label(self.login_frame, text="Username:")  # Username
        self.label_user.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.user = ttk.Entry(self.login_frame, width=30)
        self.user.grid(row=1, column=1, padx=10, pady=10)
        
        self.label_password = ttk.Label(self.login_frame, text='Password:')  # Password
        self.label_password.grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.password = ttk.Entry(self.login_frame, width=30, show='*')
        self.password.grid(row=2, column=1, padx=10, pady=10)
        
        self.button_submit = ttk.Button(self.login_frame, text="Acessar", bootstyle="SUCCESS",command=self.login_sistema)  # Botão Acessar
        self.button_submit.grid(row=3, column=1, columnspan=1, padx=5, pady=5, sticky="NSEW")
        
        self.button_registrar = ttk.Button(self.login_frame, text='Registrar', bootstyle="INFO", command=self.register)  # Registrar
        self.button_registrar.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky="NSEW")
    
        #Variaveis dos produtos.
        self.id = IntVar()
        self.nome_prod = StringVar()
        self.categoria_prod = StringVar()
        self.quantidade_prod = IntVar()
        self.preco_prod = DoubleVar()
        
    
    # Registro - REGISTRAR USUÁRIO
    def register(self):
        self.registrar_window = Toplevel(self.root)
        self.registrar_window.title('Registrar novo usuário')
        
        self.registro_frame = ttk.Frame(self.registrar_window, padding=20)
        self.registro_frame.pack(fill='both', expand=False)
        
        self.title = ttk.Label(self.registro_frame, text="Novo usuário", font=('Helvetica', 20))  # Titulo da página
        self.title.grid(row=0, column=1, columnspan=2, pady=10, sticky='NSEW')
        
        self.l_email = ttk.Label(self.registro_frame, text='Email:')  # Email
        self.l_email.grid(row=1, column=0, padx=10, pady=10)
        self.email = ttk.Entry(self.registro_frame, width=30)
        self.email.grid(row=1, column=1, padx=10, pady=10)
        
        self.l_user = ttk.Label(self.registro_frame, text="Novo Usuário:")  # Novo usuário
        self.l_user.grid(row=2, column=0, padx=10, pady=10)
        self.new_user = ttk.Entry(self.registro_frame, width=30)
        self.new_user.grid(row=2, column=1, padx=10, pady=10)
        
        self.l_password = ttk.Label(self.registro_frame, text="Senha:")  # Senha
        self.l_password.grid(row=3, column=0, padx=10, pady=10)
        self.new_password = ttk.Entry(self.registro_frame, width=30, show='*')
        self.new_password.grid(row=3, column=1, padx=10, pady=10)
        
        self.l_repeat_password = ttk.Label(self.registro_frame, text='Confirma Senha:')  # Confirma senha
        self.l_repeat_password.grid(row=4, column=0, padx=10, pady=10)
        self.repeat_password = ttk.Entry(self.registro_frame, width=30, show='*')
        self.repeat_password.grid(row=4, column=1, padx=10, pady=10)
        
        self.b_cadastrar = ttk.Button(self.registro_frame, text='Cadastrar Usuário', command=self.cadastrar_newUser)  # Botão cadastrar usuário
        self.b_cadastrar.grid(row=5, column=1, padx=10, pady=10, sticky='NSEW')
    
    
    
    
    #Menu de botões:
    def menu_botoes(self):
        
        self.menu_window = Toplevel(self.root)
        self.menu_window.title('Menu')

               
        self.menu_frame = ttk.Frame(self.menu_window, padding=20)
        self.menu_frame.pack(fill='both',expand=False)
    
        
        self.title_menu = ttk.Label(self.menu_frame,text='Menu do Sistema',font=('Helvetica', 20))
        self.title_menu.grid(row=0,column=1,padx=10,pady=10)

        self.cad_prod = ttk.Button(self.menu_frame, text='Cadastrar produto', bootstyle="SUCCESS",command=self.menu_cadastro)
        self.cad_prod.grid(row=1,column=1,padx=10,pady=10,sticky='NSEW')
        
        self.delete_prod = ttk.Button(self.menu_frame, text='Deletar produto', bootstyle=DANGER,command=self.deletar_produto)
        self.delete_prod.grid(row=2,column=1,padx=10,pady=10,sticky='NSEW')
        
        self.exibir_prod = ttk.Button(self.menu_frame,text='Exibir produto', bootstyle=INFO,command=self.exibir_produto)
        self.exibir_prod.grid(row=3,column=1,padx=10,pady=10,sticky='NSEW')
        
        self.atualizar_prod = ttk.Button(self.menu_frame,text="Atualizar produto", bootstyle=WARNING,command=self.atualizar_produto)
        self.atualizar_prod.grid(row=4,column=1,padx=10,pady=10,sticky="NSEW")
        
        
        
        
    # Cadastro de Produtos - MENU
    def menu_cadastro(self):
        
        self.menu_cadastro_window = Toplevel(self.root)
        self.menu_cadastro_window.title('Cadastro de produto')
        
        # Tela de cadastro de produtos
        self.main_frame = ttk.Frame(self.menu_cadastro_window, padding=20)
        
        self.main_frame.pack(fill='both', expand=False)
        
        #Titulo da pagina
        self.title_cad = ttk.Label(self.main_frame,text='Cadastro de Produto',font=('Helvetica', 20))
        self.title_cad.grid(row=0,column=1,padx=10,pady=10)
        
        self.id_label = ttk.Label(self.main_frame, text='ID PRODUTO:')  # ID produto
        self.id_label.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        self.id_entry = ttk.Entry(self.main_frame,textvariable=self.id, width=30)
        self.id_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.nome_label = ttk.Label(self.main_frame, text='Nome do Produto:')  # Nome do produto
        self.nome_label.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        self.nome_entry = ttk.Entry(self.main_frame,textvariable=self.nome_prod, width=30)
        self.nome_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.categoria = ttk.Label(self.main_frame, text='Categoria:')  # Categoria
        self.categoria.grid(row=3, column=0, padx=10, pady=10, sticky="W")
        self.categoria_entry = ttk.Entry(self.main_frame,textvariable=self.categoria_prod, width=30)
        self.categoria_entry.grid(row=3, column=1, padx=10, pady=10)
        
        self.quantidade = ttk.Label(self.main_frame, text='Quantidade:')  # Quantidade
        self.quantidade.grid(row=4, column=0, padx=10, pady=10, sticky="W")
        self.quantidade_entry = ttk.Entry(self.main_frame,textvariable=self.quantidade_prod, width=30)
        self.quantidade_entry.grid(row=4, column=1, padx=10, pady=10)
        
        self.preco = ttk.Label(self.main_frame, text='Preço:')  # Preço
        self.preco.grid(row=5, column=0, padx=10, pady=10, sticky="W")
        self.preco_entry = ttk.Entry(self.main_frame,textvariable=self.preco_prod, width=30)
        self.preco_entry.grid(row=5, column=1, padx=10, pady=10)
        
        self.submit = ttk.Button(self.main_frame, text='Cadastrar', width=30, bootstyle='SUCCESS',command=self.cadastrar_produtos)  # Botão Cadastrar Produto
        self.submit.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    #Tela - Exibir produto
    
    def exibir_produto(self):
        self.exibir_window = Toplevel(self.root)
        self.exibir_window.title("Exibir produto")
        
        self.exibir_frame = ttk.Frame(self.exibir_window,padding=20)
        self.exibir_frame.pack(fill='both',expand=False)
        
        self.busc_prod_title = ttk.Label(self.exibir_frame,text='Exibir produto',font=('Helvetica', 20))
        self.busc_prod_title.grid(row=0,column=1,padx=10,pady=10)
        
        self.label_buscar_prod = ttk.Label(self.exibir_frame,text='ID PRODUTO: ')
        self.label_buscar_prod.grid(row=1,column=0,padx=10,pady=10)
        self.id_buscar = ttk.Entry(self.exibir_frame,width=30)
        self.id_buscar.grid(row=1,column=1,padx=10,pady=10)
        
        self.btn_buscar = ttk.Button(self.exibir_frame,text='Buscando Produto',bootstyle=PRIMARY,command=self.exibir)
        self.btn_buscar.grid(row=3,column=1,padx=5,pady=5,sticky='NSEW')
        
    #Tela - Delatar produto
    def deletar_produto(self):
        self.delete_window = Toplevel(self.root)
        self.delete_window.title("Deletar Produto")
        
        self.delete_frame = ttk.Frame(self.delete_window,padding=10)
        self.delete_frame.pack(fill='both',expand=False)
        
        self.title_delete = ttk.Label(self.delete_frame,text="Deletar Produto",font=('Helvetica', 20))
        self.title_delete.grid(row=0,column=1,padx=10,pady=10)
        
        self.delete_id_label = ttk.Label(self.delete_frame,text="ID PRODUTO:")
        self.delete_id_label.grid(row=3,column=0,padx=10,pady=10)
        self.delete_id = ttk.Entry(self.delete_frame,textvariable=self.id,width=30)
        self.delete_id.grid(row=3,column=1,padx=10,pady=10)
        
        self.btn_delete = ttk.Button(self.delete_frame,text='Deletar', bootstyle=DANGER,command=self.delete_produto)
        self.btn_delete.grid(row=5,column=1,padx=10,pady=5,sticky='NSEW')
    
    #Tela - Atualizar produto.
    def atualizar_produto(self):
        
        self.update_window = Toplevel(self.root)
        self.update_window.title("Atualizar Produto")
        
        # Tela de update de produtos
        self.update_frame = ttk.Frame(self.update_window, padding=20)
        self.update_frame.pack(fill='both',expand=False)
        
        self.titulo_update = ttk.Label(self.update_frame,text='Atualizar produto',font=('Helvetica', 20))    
        self.titulo_update.grid(row=0,column=1,padx=10,pady=10)
    
        self.id_update = ttk.Label(self.update_frame,text='ID PRODUTO:')
        self.id_update.grid(row=1,column=0,padx=10,pady=10)
        self.id_update_entry = ttk.Entry(self.update_frame,width=30,textvariable=self.id)
        self.id_update_entry.grid(row=1,column=1,padx=10,pady=10)
    
        self.label_prod_up = ttk.Label(self.update_frame,text='Produto:')
        self.label_prod_up.grid(row=2,column=0,padx=10,pady=10)
        self.nome_prod_up = ttk.Entry(self.update_frame,width=30,state="disabled",textvariable=self.nome_prod) #Desabilitado self.nome_prod_up
        self.nome_prod_up.grid(row=2,column=1,padx=10,pady=10)
    
        self.label_cat_up = ttk.Label(self.update_frame, text="Categoria: ")
        self.label_cat_up.grid(row=3,column=0,padx=10,pady=10)
        self.categoria_up = ttk.Entry(self.update_frame,width=30,state='disabled',textvariable=self.categoria_prod) #Desabilitado self.categoria_up
        self.categoria_up.grid(row=3,column=1,padx=10,pady=10)
        
        self.label_quantidade = ttk.Label(self.update_frame,text='Quantidade: ')
        self.label_quantidade.grid(row=4,column=0,padx=10,pady=10)
        self.quantidade_up = ttk.Entry(self.update_frame,width=30, state='disabled',textvariable=self.quantidade_prod) #Desabilitado self.quantidade_up
        self.quantidade_up.grid(row=4,column=1,padx=10,pady=10)
        
        self.label_preco_up = ttk.Label(self.update_frame,text="Preço: ")
        self.label_preco_up.grid(row=5,column=0,padx=10,pady=10)
        self.preco_up = ttk.Entry(self.update_frame,width=30,state='disabled',textvariable=self.preco_prod) #Desabilitado self.preco_up
        self.preco_up.grid(row=5,column=1,padx=10,pady=10)
        
        self.search = ttk.Button(self.update_frame,text='Procurar',bootstyle=PRIMARY, command=self.search_id) #Botão procurar
        self.search.grid(row=6,column=1,columnspan=2,padx=10,pady=10,sticky='NSEW')
        
        self.update = ttk.Button(self.update_frame,text="Atualizar",bootstyle=SUCCESS,command=self.update_produto) #Botão atualizar
        self.update.grid(row=7,column=1,columnspan=2,padx=10,pady=10,sticky='NSEW')
        

    '''Metodos usados no sistema'''
    #Cadastrar novo usuário
    def cadastrar_newUser(self):
        email = self.email.get()
        nome = self.new_user.get()
        senha = self.new_password.get()
        r_senha = self.repeat_password.get()
        
        if senha != r_senha:
            messagebox.showinfo('As senhas não conferem', 'As senhas precisam ser iguais.')
    
        cad_user = request.cadastrar_user(email, nome, senha)
        if cad_user == True:
            messagebox.showinfo('Usuário cadastrado com sucesso!','Usuário cadastrado com sucesso!')
            self.registrar_window.destroy()  # Fechar a janela de registro após sucesso
        else:
            messagebox.showinfo('Email já cadastrado','Email já cadastrado')
            self.registrar_window.destroy()
                
    #Login - Validação de login
    def login_sistema(self):
        
        user = self.user.get()
        senha = self.password.get()
        
        if request.acesso(user,senha):
            
            messagebox.showinfo('Acesso liberado','Acesso liberado')
            self.login_frame.destroy()
            self.menu_botoes()
        
        else:
            messagebox.showinfo('Usuário ou Senha inválidos','Usuário ou Senha inválidos')

    #Cadastro de produtos
    def cadastrar_produtos(self):
        id = self.id.get()
        nome_prod =  self.nome_prod.get()
        categoria = self.categoria_prod.get()
        quantidade = self.quantidade_prod.get()
        preco = self.preco_prod.get()
        
        try:
            cad_prod = request_prod.insert_prod(id,nome_prod,categoria,quantidade,preco)

            print(cad_prod)
            
            if cad_prod:
                messagebox.showinfo('Atenção','Produto Cadastrado com sucesso!')
                
                self.id.set(0)
                self.nome_prod.set('')
                self.categoria_prod.set('')
                self.quantidade_prod.set(0)
                self.preco_prod.set(0.0)
            else:
                messagebox.showinfo('Atenção',f'O id:{id}, já está cadastrado!')
                
            
        except ValueError as erro:
            messagebox.showerror(f'Erro: {erro}')
    
    #Buscando produto        
    def search_id(self):
        
        id = self.id.get()
        
        produto = request_prod.buscando_prod(id)
        
        try:
        
            if produto:
                nome = produto['nome']
                categoria = produto['categoria']
                quantidade = produto['quantidade']
                preco = produto['preco']
                
                self.id_update.configure(state='normal')
                self.nome_prod_up.configure(state='normal')
                self.categoria_up.configure(state='normal')
                self.quantidade_up.configure(state='normal')
                self.preco_up.configure(state='normal')
        
                self.nome_prod.set(nome)
                self.categoria_prod.set(categoria)
                self.quantidade_prod.set(quantidade)
                self.preco_prod.set(preco)
            
            else:
                messagebox.showerror('Atenção','Produto não cadastrado!')
                
        except ValueError as Erro:
            messagebox.showinfo("Erro",f"Erro ao realizar busca do produto: {Erro}")
    
    #Atualizando produto
    def update_produto(self):
        
        id = self.id.get()
        nome =self.nome_prod.get()
        categoria = self.categoria_prod.get()
        quantidade = self.quantidade_prod.get()
        preco = self.preco_prod.get()

        try:
            update = request_prod.update_prod(id,nome,categoria,quantidade,preco)
            
            if update:
                messagebox.showinfo('Atualização',f'PRODUTO ID:{id} atualizado com sucesso!')
                self.id.set(0)
                self.nome_prod.set('')
                self.categoria_prod.set('')
                self.quantidade_prod.set(0)
                self.preco_prod.set(0.0)
                
                #Desabilitando novamento:
                self.nome_prod_up.configure(state='disabled')
                self.categoria_up.configure(state='disabled')
                self.quantidade_up.configure(state='disabled')
                self.preco_up.configure(state='disabled')
                
                self.update_window.destroy()
            
        except ValueError as erro:
            messagebox.showinfo('ERRO',f'Erro de sistema: {erro}')
    
    #Função da tela Delatar - PROCURANDO O ID  
    def delete_produto(self):
        
        id = self.id.get()
        print(id)
        confirma = messagebox.askyesno('Alerta',f"Deseja deletar o ID: {id}? ")
        
        try:
            
            if confirma:
                request_prod.deletar_produto(id)
                messagebox.showinfo('Aviso','Produto excluido com sucesso!')
                self.delete_window.destroy()
                
        except ValueError as e:
                messagebox.showerror('Erro', f'Erro do sistema! : {e}')
                
                
        print(confirma)
    
    def exibir(self):
        
        id_exibir = self.id_buscar.get()
        
        try:
            query = request_prod.buscando_prod(id_exibir)
            
            if query:
                id_e = query['id']
                nome_e = query['nome']
                categoria_e = query['categoria']
                quantidade_e = query['quantidade']
                preco_e = query['preco']

                self.id_e = ttk.Label(self.exibir_frame, text='ID PRODUTO:', font=('Helvetica', 13,'bold'))
                self.id_e.grid(row=5,column=0,padx=10,pady=10)
                self.id_r = ttk.Label(self.exibir_frame,text=f'{id_e}',font=('Helvetica', 13,'bold'))
                self.id_r.grid(row=5,column=1,padx=10,pady=10)

                self.nome_l = ttk.Label(self.exibir_frame,text='Produto: ', font=('Helvetica', 13,'bold'))
                self.nome_l.grid(row=6,column=0,padx=10,pady=10)
                self.nome_e = ttk.Label(self.exibir_frame, text=f'{nome_e}', font=('Helvetica', 13,'bold'))
                self.nome_e.grid(row=6,column=1,padx=10,pady=10)
                
                self.categoria_l = ttk.Label(self.exibir_frame,text='Categoria: ', font=('Helvetica', 13,'bold'))
                self.categoria_l.grid(row=7,column=0,padx=10,pady=10)
                self.categoria_e = ttk.Label(self.exibir_frame,text=f'{categoria_e}', font=('Helvetica', 13,'bold'))
                self.categoria_e.grid(row=7,column=1,padx=10,pady=10)
                
                self.quantidade_l = ttk.Label(self.exibir_frame,text='Quantidade: ', font=('Helvetica', 13,'bold'))
                self.quantidade_l.grid(row=8,column=0,padx=10, pady=10)
                self.quantidade_e = ttk.Label(self.exibir_frame,text=f'{quantidade_e}', font=('Helvetica', 13,'bold'))
                self.quantidade_e.grid(row=8,column=1,padx=10,pady=10)
                
                self.preco_l = ttk.Label(self.exibir_frame,text='Preço: ', font=('Helvetica', 13,'bold'))
                self.preco_l.grid(row=9,column=0,padx=10,pady=10)
                self.preco_e = ttk.Label(self.exibir_frame,text=f'R$ {preco_e:.2f}', font=('Helvetica', 13,'bold'))
                self.preco_e.grid(row=9,column=1,padx=10,pady=10)
                
        except ValueError as erro:
            messagebox.showerror('ERRO', f'Erro de requisição: {erro}')
        
  
       
           
#Inicializando sistema
if __name__ == "__main__":
    root = ttk.Window(themename='morph')
    app = Myapp(root)
    root.mainloop()
