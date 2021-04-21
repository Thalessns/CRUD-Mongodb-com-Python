# Importando Módulos essenciais
import PySimpleGUI as tl;
from usuarioController import UsuarioController;
from usuario import Usuario;
from conectar import conectar;
import uteis;

# Gerando Classe
user = UsuarioController();

# Variavel que guarda informações do usuário logado
logado = False;

# Nome de usuário sem estar logado
username = 'Convidado';

# Loop do programa
while True:
    # Verifica se o usuário está logado
    if logado != False:
        # Pegando nome do usuário logado
        username = user.pegaNome(logado['codigo'])['nome'];
    # Adicionando Tema
    tl.theme('DarkAmber');
    # Tudo que vai ficar dentro da janela
    layout = [ [tl.Text(f'Bem-vindo(a), {username}!', justification='center', size=(410, 0))],
               [tl.Text('Escolha uma opção: ', justification='center', size=(410, 0))],
               [tl.Text(f'-' * 100, justification='center', size=(410,0))],
               [tl.Button('Login'), tl.Button('Cadastrar'), tl.Button('Consultar'), tl.Button('Logout'), tl.Button('Sair')] ];
    # Criando janela
    janela = tl.Window('Menu de Opções', layout, size=(415, 120));
    # Variavel que vai guardar a escolha
    escolha = '';
    # Loop que vai processar os 'eventos' e pegar os 'valores' das inputs
    while True:
        # Eventos 
        evento, valores = janela.read();
        # Veriicando escolha do usuário
        escolha = evento;
        break;
    # Fechando Janela
    janela.close();
    # Saindo programa
    if escolha == 'Sair' or escolha == tl.WIN_CLOSED:
        if user.confirma(f'{username}, tem certeza que deseja sair?') == True:
            break;
    # Rodando Função de Login
    if escolha == 'Login':
        result = user.login();
        logado = result;
    # Rodando Função de Cadastro
    if escolha == 'Cadastrar':
        user.cadastrar();
    # Rodando Função de Consulta
    elif escolha == 'Consultar':
        user.consultar();
    # Fazendo logout de usuário
    elif escolha == 'Logout':
        if logado != False:
            # Removendo usuário logado
            logado = False;
            # Mostrando mensagem
            if user.confirma(f'Deseja mesmo fazer Logout, {username}?') == True:
                # Efettuando logout
                user.popUp('Logout efetuado com sucesso!');
                username = 'Convidado';
                logado = False;
        else:
            # Mostrando mensagem
            user.popUp('Você não está logado!');