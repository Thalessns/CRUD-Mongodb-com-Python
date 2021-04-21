# Importando módulos essenciais
from pymongo import MongoClient;
from urllib import parse;

# Função que vai conectar com o banco
def conectar():
    try:
        # Definindo usuário do banco
        user        = parse.quote_plus('usuario_do_banco');
        # Senha de usuário
        password    = parse.quote_plus('senha_do_usuario');
        # Nome do cluster
        cluster     = parse.quote_plus('nome_do_cluster');
        # Conectando
        conexao     = MongoClient(f'mongodb+srv://{user}:{password}@{cluster}.ij7sq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority');
    except Exception as error:
        # Mostrando mensagem de erro
        print(f'Erro na conexão com o banco: {error}');
    else:
        # Retornando conexao com o banco
        return conexao;
