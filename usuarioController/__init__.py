# Classe Controller, Vai Exigir as informações
class UsuarioController:
    
    # importando módulos essenciais
    import PySimpleGUI as tl;
    from usuario import Usuario;
    import uteis;

    # Executa quando inicia
    def __init__(self):
        # Adicionando Tema
        self.tl.theme('DarkAmber');
    
    # Função que abre uma tela para mensagem
    def popUp(self,msg):
        # Tudo que vai aparecer na janela
        popLayout = [ [self.tl.Text(msg, size=(400, 0), justification='center')],
                      [self.tl.Text()], 
                      [self.tl.Text(' ', size=(21, 0)), self.tl.Button('OK')] ];
        # Criando janela
        pop = self.tl.Window('Alerta !', popLayout, size=(400, 100));
        # Loop
        while True:
            # Eventos
            evento, valores = pop.read();
            # Saindo
            if evento == 'OK' or evento == self.tl.WIN_CLOSED:
                # Fechando a janela
                pop.close();
                break;

    # Função que abre uma tela de confirmação
    def confirma(self,msg):
        # Tudo que vai aparecer na janela
        confirmaLayout = [ [self.tl.Text(msg, size=(250, 0), justification='center')],
                           [self.tl.Text()], 
                           [self.tl.Text('', size=(15, 0)), self.tl.Button('Sim'), self.tl.Button('Cancelar')] ];
        # Criando janela
        confirma = self.tl.Window('Alerta !', confirmaLayout, size=(400, 100));
        # Loop
        while True:
            # Eventos
            evento, valores = confirma.read();
            # Saindo
            if evento == 'Sim':
                # Fechando janela
                confirma.close();
                # Retornando SIM
                return True;
            else:
                # Fechando janela
                confirma.close();
                # Retornando NÂO
                return False;

    # Função para cadastro
    def cadastrar(self):
        # Tudo que vai ficar dentro da janela
        cadLayout = [   [self.tl.Text('Cadastrando Usuário', size=(415, 0), justification='center')],
                        [self.tl.Text(f'-' * 100, justification='center', size=(410,0))],
                        [self.tl.Text(f'{"Nome:":<15}', size=(15,0)), self.tl.InputText()], 
                        [self.tl.Text(f'{"Email:":<15}', size=(15,0)), self.tl.InputText()],
                        [self.tl.Text(f'{"Senha:":<15}', size=(15,0)), self.tl.InputText(password_char='*')],
                        [self.tl.Text(f'{"Confirmar Senha:":<15}', size=(15,0)), self.tl.InputText(password_char='*')],
                        [self.tl.Text(f'-' * 100, justification='center', size=(410,0))],
                        [self.tl.Text(' ', size=(13, 0)), self.tl.Button('Confirmar') ,self.tl.Button('Voltar')] ];
        # Criando janela
        janela = self.tl.Window('Cadastrar', cadLayout, size=(415, 210));
        # Loop que vai processar os 'eventos' e pegar os 'valores' das inputs
        while True:
            # Eventos 
            evento, valores = janela.read();
            # Verificando valores e escolhas do usuário
            if evento == 'Confirmar':
                if valores[0] != '' and valores[1] != '' and valores[2] != '' and valores[3] != '':
                    try:
                        # Verificando se o nome é válido
                        verNome = self.trataNome(valores[0]);
                        if verNome != True:
                            raise Exception(verNome);
                        # Verificando se o email é válido
                        verEmail = self.trataEmail(valores[1]);
                        if verEmail != True:
                            raise Exception(verEmail);
                        # Verificando se a senha é válida
                        verSenha = self.trataSenha(valores[2], valores[3]);
                        if verSenha != True:
                            raise Exception(verSenha);
                        # Criptografando senha
                        cripto = self.cripto(valores[2]);
                    except Exception as error:
                        # Mostrando Mensagem de erro
                        self.popUp(error);
                    else:
                        try:
                            # Criando classe
                            user = self.Usuario(nome=valores[0], email=valores[1], senha=cripto);
                            # Pegando resultado
                            result = user.cadastrar();
                            # Verificando resultado
                            if result != True:
                                raise Exception(result);
                        except Exception as error:
                            self.popUp(error);
                        else:
                            self.popUp('Cadastro Realizado com Sucesso!');
                            # Fechando Janela
                            janela.close();
                            return;
                else:
                    # Mostrando Mensagem de Erro
                    self.popUp('Por favor, preencha todos os campos!');
            if evento == self.tl.WINDOW_CLOSED or evento == 'Voltar':
                # Fechando Janela
                janela.close();
                break;
    
    # Função que vai consultar os dados
    def consultar(self):
        # Definindo Classe
        user = self.Usuario();
        # Fazendo COnsulta
        dados = user.consultaTodos();
        # Coisas que vão aparecer na tela
        consultLayout = [ [self.tl.Text('Consultando Registros', size=(800, 0), justification='center')],
                          [self.tl.Listbox(values=dados, enable_events=True, auto_size_text=True, size=(110, 12))],
                          [self.tl.Text(' ', size=(36, 0)), self.tl.Button('Alterar'), self.tl.Button('Excluir'), self.tl.Button('Voltar')] ];
        # Criando a Janela
        consulta = self.tl.Window('Consulta', consultLayout, size=(800, 260));
        # Criando Loop da Janela
        while True:__init__
            # Variaveis que vão armazenar ações e valores
            evento, valores = consulta.read();
            # Saindo do programa
            if evento == 'Voltar' or evento == self.tl.WIN_CLOSED:
                # Fechando Janela
                consulta.close();
                break;
            # Verificando se há registros selecionados
            if valores[0] != [] and valores[0][0] != '':
                # Excluindo registro
                if evento == 'Excluir':
                    try:
                        # Verificando se o código é valido
                        int(valores[0][0][0]);
                        # Pegando o código
                        cod = valores[0][0][0];
                        if cod == '1':
                            raise Exception(self.uteis.texto('excluir'));
                        # Pedindo confirmação se exclusão
                        if self.confirma(f'Deseja mesmo excluir o registro {cod}? ') == False:
                            raise Exception('Exclusão cancelada!');
                        # Preparando classe
                        user = self.Usuario();
                        # Excluindo registro
                        result = user.excluir(cod);
                        # Verificando resultado
                        if result != True:
                            raise Exception(result);
                    except ValueError:
                        # Mostrando mensagem de erro
                        self.popUp(f'Erro na seleção: Selecione uma opção válida!');
                    except Exception as error:
                        # Montrando mensagem de erro
                        self.popUp(f'Erro na exclusão: {error}');
                    else:
                        # Fechando a janela
                        consulta.close();
                        # Mostrando mensagem de sucesso
                        self.popUp('Registro excluído com sucesso!');
                        # Saindo da tela
                        break;
                # Alterando Registro
                elif evento == 'Alterar':
                    try:
                        # Verificando se existem registros selecionados

                        # Verificando se o código é valido
                        int(valores[0][0][0]);
                        # Pegando o código
                        cod = valores[0][0][0];
                        # Pedindo confirmação se exclusão
                        if self.confirma(f'Deseja mesmo alterar o registro {cod}? ') == False:
                            raise Exception('Alteração cancelada!');
                        # Preparando classe
                        user = self.Usuario();
                        # Alterando Registro
                        result = self.telaAlterar(cod);
                        if result != True:
                            raise Exception(result);
                    except ValueError:
                        # Mostrando mensagem de erro
                        self.popUp(f'Erro na seleção: Selecione uma opção válida!');
                    except Exception as error:
                        # Montrando mensagem de erro
                        self.popUp(f'Erro na alteração: {error}');
                    else:
                        # Fechando a janela
                        consulta.close();
                        # Mostrando mensagem de sucesso
                        self.popUp('Registro alterado com sucesso!');
                        # Saindo da Tela
                        break;
            else:
                # Mostrando mensagem
                self.popUp('Selecione algum registro!');
        # Saindo da Função
        return;

    # Função que cuida da tela de alteração
    def telaAlterar(self, cod):
        # Layout da tela
        alteraLayout = [ [self.tl.Text('Alterar Dados', size=(415, 0), justification='center')],
                         [self.tl.Text(f'-' * 100, justification='center', size=(410,0))],
                         [self.tl.Text('Nome:', size=(15, 0)), self.tl.InputText()], 
                         [self.tl.Text('Email:', size=(15, 0)), self.tl.InputText()],
                         [self.tl.Text('Senha:', size=(15, 0)), self.tl.InputText(password_char='*')],
                         [self.tl.Text('Confirma Senha:', size=(15, 0)), self.tl.InputText(password_char='*')],
                         [self.tl.Text(f'-' * 100, justification='center', size=(410,0))],
                         [self.tl.Text('', size=(15, 0)), self.tl.Button('Alterar'), self.tl.Button('Voltar')]];
        # Criando a tela
        altera = self.tl.Window('Alterar Dados', alteraLayout, size=(415, 210));
        # Cirando Loop da tela
        while True:
            # Variaveis
            evento, valores = altera.read();
            # Verificando ações
            if evento == 'Alterar':
                if valores[0] != '' and valores[1] != '' and valores[2] != '' and valores[3] != '':
                    try:
                        # Verificando se o nome é válido
                        verNome = self.trataNome(valores[0]);
                        if verNome != True:
                            raise Exception(verNome);
                        # Verificando se o email é válido
                        verEmail = self.trataEmail(valores[1]);
                        if verEmail != True:
                            raise Exception(verEmail);
                        # Verificando se a senha é válida
                        verSenha = self.trataSenha(valores[2], valores[3]);
                        if verSenha != True:
                            raise Exception(verSenha);
                        # Criptografando senha
                        cripto = self.cripto(valores[2]);
                        # Alterando
                        alt = self.Usuario(nome=valores[0], email=valores[1], senha=cripto);
                        # Pegando resultado
                        result = alt.alterar(cod);
                        # Verificando resultado
                        if result != True:
                            raise Exception(result);
                    except Exception as error:
                        # Mostrando mensagem de erro
                        self.popUp(f'Erro na alteração: {error}');
                    else:
                        # Fechando janela
                        altera.close();
                        # Retornando sucesso
                        return True;
                else:
                    self.popUp('Por favor, preencha todos os campos!');
            else:
                # Saindo
                altera.close();
                return 'Alteração cancelada!';

    # Função que vai cuidar do login do usuário
    def login(self):
        # Criando Layout da Tela
        loginLayout = [ [self.tl.Text('Login', size=(415,0), justification='center')],
                        [self.tl.Text(f'-' * 100, justification='center', size=(410,0))], 
                        [self.tl.Text('Email:', size=(7,0)), self.tl.InputText()],
                        [self.tl.Text('Senha:', size=(7,0)), self.tl.InputText(password_char='*')],
                        [self.tl.Text(f'-' * 100, justification='center', size=(410,0))],
                        [self.tl.Text(' ', size=(16,0)), self.tl.Button('Logar'), self.tl.Button('Voltar')] ];
        # Criando tela
        telaLogin = self.tl.Window('Login', loginLayout, size=(415, 170));
        # Loop da tela
        while True:
            # Variaveis
            evento, valores = telaLogin.read();
            # Verificano ação do usuário
            if evento == 'Logar':
                if valores[0] == '' or valores[1] == '':
                    self.popUp('Por favor, preencha todos os campos!');
                else:
                    try:
                        # Criptografando a senha
                        senha = self.cripto(valores[1]);
                        # Pegando email
                        email = valores[0];
                        # Preparando classe
                        user = self.Usuario(email=email, senha=senha);
                        # Pegando resultado
                        result = user.login();
                        # Verificando resultado
                        if type(result) == str:
                            # Retornando Mensagem de erro
                            raise Exception(result);
                    except Exception as error:
                        # Mostrando mensagem de erro
                        self.popUp(result);
                    else:
                        self.popUp('Login efetuado com sucesso!');
                        # Fechando a janela
                        telaLogin.close();
                        return result;
            elif evento == 'Voltar' or evento == self.tl.WIN_CLOSED:
                # Fechando janela
                telaLogin.close();
                # Retornando usuário não logado
                return False;

    # Função que vai verificar irregularidades no nome
    def trataNome(self, nome):
        try:
            # Definindo caracteres que não serão aceitos
            especiais = '!@#$%&*()[]}{+_=-1234567890/?°®ŧ←↓→øþþæßðđŋħł»\«»©µ─·<>.,;:/~^`´';
            # Verificando se há esses caracteres no nome
            for char in especiais:
                if char in nome:
                    # Mandando mensagem de erro
                    raise Exception('Erro: Caracteres especiais não serão aceitos no nome!');
            # Verificando se o nome é vazio
            if nome.strip() == '' or nome.strip() == ' ':
                raise Exception('Erro: O nome não pode estar vazio!');
            # Verificando quantos caracteres o nome tem
            if len(nome) < 3:
                raise Exception('Erro: O nome não pode ter menos de 3 caracteres!');
            if len(nome) > 20:
                raise Exception('Erro: O nome não pode ter mais de 20 caracteres!');
        except Exception as error:
            # Retornando Mensagem de erro
            return error;
        else:
            # Retornando sucesso
            return True;

    # Função que vai verificar irregularidades no email
    def trataEmail(self, email):
        try:
            # Verificando se o email é válido
            if len(email) < 3 or '@' not in email or ' ' in email:
                raise Exception('Erro: Email inválido!');
        except Exception as error:
            # Retornando mensagem de erro
            return error;
        else:
            return True;

    # Função que vai verificar irregularidades na senha
    def trataSenha(self, senha, confirma):
        try:
            # Verificando se a senha é válida
            if len(senha) < 6 or ' ' in senha or len(senha) > 20:
                raise Exception('Erro: A senha deve ter entre 6 e 20 caracteres, e também não deve conter espaços!');
            # Verificando se as senhas são iguais
            if senha != confirma:
                raise Exception('Erro: As senhas não correspondem!');
        except Exception as error:
            # Retornando mensagem de erro
            return error;
        else:
            return True;

    # Função que criptografa uma string
    def cripto(self, txt):
        # Importando biblioteca 
        import hashlib;
        # Criptografando Texto
        cripto = hashlib.sha1(txt.encode()).hexdigest();
        # Retornando texto criptografado
        return cripto;

    # Função que vai pegar o nome do usuário
    def pegaNome(self, cod):
        # Preparando classe
        user = self.Usuario();
        # Tentando pegar o nome
        result = user.retornaNome(cod);
        # Verificando resultado
        if type(result) != bool:
            # Retornando registro
            return result;
        else:
            # Retornando string caso o registro não for encontrado
            return 'Convidado';
