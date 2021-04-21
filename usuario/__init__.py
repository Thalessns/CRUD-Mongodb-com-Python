# Classe Usuário que vai cuidar do BackEnd e responder a UsuarioController
class Usuario:
    # Importando módulo essencial
    import uteis;
    # Função construtura que prepara as variaveis essenciais da classe
    def __init__(self, nome='', email='', senha=''):
        # Pegando valores
        if nome != '':
            self.nome = nome;
        if email != '':
            self.email = email;
        if senha != '':
            self.senha = senha;
        # Adicionando módulo de Conexao
        from conectar import conectar;
        # Efetuando conexao
        self.con    = conectar();
        # Pegando banco que será utilizado
        self.banco  = self.con['Teste'];
        # Pegando coleção que será utilizada
        self.colec  = self.banco['usuarios'];

    # Função que vai cadastrar dados
    def cadastrar(self):
        try:
            # Verificando se o email já está registrado
            if self.verEmail() != True:
                raise Exception('Email já foi registrado!');
            # Gerando novo código
            cod = self.novoCod();
            # Preparando dados
            dados = { 'codigo': str(cod),
                      'nome':   self.nome,
                      'email':  self.email,
                      'senha':  self.senha };
            # Cadastrando
            self.colec.insert_one(dados);
        except Exception as error:
            # Retornando mensagem de erro
            return f'Erro no cadastro: {error}';
        else:
            # Retornando sucesso
            return True;

    # Função que vai retornar todos os registros
    def consultaTodos(self):
        try:
            # Criando query
            query = self.colec.find();
            # Variavel que vai guardar os dados
            dados = [f'{"Código":<30} {"Nome":<33} {"Email":<30} {"Senha":>30}'];
            dados.append('');
            # Pegando registros
            for reg in query:
                dados.append(str(f'{reg["codigo"]}' + self.uteis.espaco(reg["codigo"]) + f'{reg["nome"]}' + self.uteis.espaco(reg["nome"]) + f'{reg["email"]}' + self.uteis.espaco(reg["email"]) + f'{reg["senha"]}'));
        except Exception as error:
            # Retornando mensagem de erro
            return f'Erro na consulta de dados: {error}';
        else:
            # Retornando a lista de dados
            return dados;
    
    # Função que vai alterar dados 
    def alterar(self, cod):
        try:
            # Verificando se o email é repetido
            result = self.verEmail(alt=True);
            # Verificando se é repetido
            if type(result) != bool:
                if result['codigo'] != cod:
                    raise Exception('Este email já está em uso!');
            # Preparando dados
            dados = {'codigo':  cod,
                     'nome':    self.nome,
                     'email':   self.email,
                     'senha':   self.senha };
            # Alterando
            self.colec.update_one({'codigo': cod}, {'$set': dados}, upsert=True);
        except Exception as error:
            return error;
        else:
            return True;

    # Função que vai excluir registros
    def excluir(self, cod):
        try:
            # Excluindo Registro
            self.colec.delete_one({'codigo': cod});
        except Exception as error:
            return error;
        else:
            return True;

    # Função que fará a função de login
    def login(self):
        try:
            # Verificando se existem registros no banco
            if self.novoCod() == 1:
                raise Exception('Você não tem registros no banco!');
            # Fazendo query
            query = self.colec.find({'email': self.email, 'senha': self.senha});
            # Verificando se o registro existe
            reg = {};
            for line in query:
                # Pegando o registro
                reg = line;
            # Verificando se o registro é válido
            if len(reg) == 0:
                raise Exception('Login/senha estão incorretos!');
        except Exception as error:
            return f'Erro no login: {error}';
        else:
            return reg;
                                 
    # Função que vai gerar um novo código para cadastro
    def novoCod(self):
        # Contador
        cont = 0;
        # Efetuando Query
        for reg in self.colec.find():
            if int(reg['codigo']) > cont:
                cont = int(reg['codigo']);
        # Verificando se existem registros
        if cont > 0:
            # Retornando Novo Código
            return cont + 1;
        else:
            # Retornando Primeiro Código
            return 1;

    # Função que verifica se um email já está registrado no banco
    def verEmail(self, alt=False):
        # Efetuando Query
        query = self.colec.find({'email': self.email});
        # Verificando se retornou registros
        for reg in query:
            if alt == True:
                return reg;
            # Email repetido, retornando falha se não for alteração
            return False;
        # Email não repetido, retornando sucesso
        return True;

    # Função que vai retornar o nome
    def retornaNome(self, cod):
        # Efetuando Query
        query = self.colec.find({'codigo': cod});
        # Registrando resultado caso registro não for encontrado
        result = False;
        # Verificando se existem registros
        for reg in query:
            # Guardando registro encotrado
            result = reg;
        # Retornando resultado
        return result;
