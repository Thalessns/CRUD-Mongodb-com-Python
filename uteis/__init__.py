# Função de Mensagens
def msg(txt):
    return f'{txt:^100}';

# Função Espacamento
def espaco(var):
    return f'.' * (30 - len(str(var.strip())));
