# Importando módulos essenciais
from pymongo import MongoClient;
from urllib import parse;

# Função que vai conectar com o banco
def conectar():
    try:
        # Definindo usuário do banco
        user        = parse.quote_plus('convidado');
        # Senha de usuário
        password    = parse.quote_plus('hEWJSbT7BDNLTt2Q');
        # Conectando
        conexao     = MongoClient(f'mongodb+srv://{user}:{password}@cluster0.ij7sq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority');
    except Exception as error:
        # Mostrando mensagem de erro
        print(f'Erro na conexão com o banco: {error}');
    else:
        # Retornando conexao com o banco
        return conexao;
