<h1 style='text-align: center;'>Sistema de Gerenciamento de Produtos</h1>
<p>
Este é um sistema de gerenciamento de produtos desenvolvido em Python utilizando a biblioteca ttkbootstrap para a interface gráfica. O sistema permite que os usuários façam login, registrem novos usuários e gerenciem produtos (cadastrar, atualizar, exibir e deletar).
</p>

<h2>Funcionalidades</h2>
<ul>
<li>Login: Tela de login para acessar o sistema.</li>
<li>Registro de Usuário: Permite o registro de novos usuários.</li>
<li>Menu Principal: Interface principal com opções para gerenciar produtos.</li>
<li>Cadastro de Produto: Tela para cadastrar novos produtos no sistema.</li>
<li>Exibir Produto: Tela para exibir detalhes de um produto específico.</li>
<li>Deletar Produto: Tela para deletar produtos do sistema.</li>
<li>Atualizar Produto: Tela para atualizar informações de produtos existentes.</li>
</ul>

<h2>Estrutura do Projeto</h2>
<p>O projeto é organizado da seguinte maneira:</p>


    
    ├── db
    └── sistema_prod.db     # Banco de dados SQLite
    ├── crud_user.py            # Módulo para operações CRUD de usuários
    ├── crud_prod.py            # Módulo para operações CRUD de produtos
    ├── main.py                 # Arquivo principal que contém a classe MyApp einicializa a aplicação
    └── README.md               # Este arquivo

<h2>Dependências</h2>
<p>Para executar este projeto, você precisa das seguintes bibliotecas Python:</p>
<ul>
<li>ttkbootstrap</li>
<li>tkinter</li>
</ul>

<h2>Uso:</h2>
<ol>
<li><h3>Login:</h3>
<ul>
<li>Insira seu nome de usuário e senha para acessar o sistema.</li>
<li>Certifique-se de que as senhas correspondam antes de enviar.</li>
</ul>
</li>

<li><h3>Registrar Usuário:</h3>
<ul>
<li>Preencha os campos de e-mail, nome de usuário e senha para criar uma nova conta.</li>
<li>Certifique-se de que as senhas correspondam antes de enviar.</li>
</ul>
</li>

<li><h3>Menu Principal:</h3>
<ul>
<li>Após fazer login, você será redirecionado para o menu principal.</li>
<li>Aqui você pode escolher entre as opções para cadastrar, atualizar, exibir ou deletar produtos.</li>
</ul>
</li>

<li><h3>Gerenciamento de Produtos:</h3>
<ul>
<li>Cadastrar Produto: Preencha os detalhes do produto e clique em "Cadastrar".</li>
<li>Exibir Produto: Insira o ID do produto que deseja exibir e clique em "Buscar Produto".</li>
<li>Deletar Produto: Insira o ID do produto que deseja deletar e clique em "Deletar".</li>
<li>Atualizar Produto: Insira o ID do produto que deseja atualizar, clique em "Procurar" para buscar os detalhes, faça as alterações necessárias e clique em "Atualizar".</li>

</ul>
</li>
</ol>

<h2>Contribuição</h2>
<p>Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, por favor, abra uma issue ou envie um pull request.</p>

<h2>Licença</h2>

<p>Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.</p>