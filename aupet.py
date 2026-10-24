class Pessoa:
    lista_clientes = []
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class Tutor(Pessoa):
    def __init__(self, nome, email, telefone, cpf, endereco):
        super().__init__(nome, email, telefone)
        self.cpf = cpf
        self.endereco = endereco

class Administrador(Pessoa):
    def __init__(self, nome, email, telefone, senha):
        super().__init__(nome, email, telefone)
        self.senha = senha

class Auxiliar(Pessoa):
    def __init__(self, nome, email, telefone, senha):
        super().__init__(nome, email, telefone)
        self.senha = senha

class Recepcionista(Pessoa):
    def __init__(self, nome, email, telefone, senha):
        super().__init__(nome, email, telefone)
        self.senha = senha

class Cachorro:
    def __init__(self, id_cachorro, nome, foto, pelagem, raca, data_nascimento, carteira_vacina, porte, alergia, castrado, tutor, data_matricula, tipo_mensalidade):
        self.id_cachorro = id_cachorro
        self.nome = nome
        self.foto = foto
        self.pelagem = pelagem
        self.raca = raca
        self.data_nascimento = data_nascimento
        self.carteira_vacina = carteira_vacina
        self.porte = porte
        self.alergia = alergia
        self.castrado = castrado
        self.tutor = tutor
        self.data_matricula = data_matricula
        self.tipoMensalidade = tipo_mensalidade

    def __repr__(self):
        return f"{self.id_cachorro} - {self.nome} - {self.foto} - {self.pelagem} - {self.raca} - {self.data_nascimento} - {self.carteira_vacina} - {self.porte} - {self.alergia} - {self.castrado} - {self.tutor.nome}"

class Medicacao:
    def __init__(self, id_cachorro, nome_medicacao, qtd, data_medicacao, horario_medicacao):
        self.id_cachorro = id_cachorro
        self.nome_medicacao = nome_medicacao
        self.qtd = qtd
        self.data_medicacao = data_medicacao
        self.horario_medicacao = horario_medicacao

    def registrar_medicacao(self):
        print(f'Medicação: ({self.nome_medicacao}) | Quantidade: ({self.qtd}) | Registrada para o Cachorro ({self.id_cachorro})\nÀs {self.horario_medicacao} de {self.data_medicacao}.')
    
class Estadia:
    def __init__(self, cpf, id_cachorro, periodo_hospedagem, status_pagamento='Pendente'):
        self.cpf = cpf
        self.id_cachorro = id_cachorro
        self.periodo_hospedagem = periodo_hospedagem
        self.status_pagamento = status_pagamento
        

    def registrar_pagamento(self):
        self.status_pagamento='Pago'
        print(f'CPF do Tutor ({self.cpf}) | ID do Cachorro ({self.id_cachorro})\nPeriodo da Hospedagem ({self.periodo_hospedagem})\nStatus do Pagamento ({self.status_pagamento}).')

class Frequencia:
    def __init__(self, id_cachorro, data, horario_entrada, horario_saida):
        self.id_cachorro = id_cachorro
        self.data = data
        self.horario_entrada = horario_entrada
        self.horario_saida = horario_saida

    def registrar_frequencia(self):
        print(f'ID Cachorro ({self.id_cachorro}) | Data ({self.data})\nHorários: Entrada ({self.horario_entrada}) | Saída ({self.horario_saida})')

class Pagamento:
    def __init__(self, cpf, id_cachorro, tipo_plano, valor, tipo_pagamento, data_pagamento, status='Pendente'):
        self.cpf = cpf
        self.id_cachorro = id_cachorro
        self.tipo_plano = tipo_plano
        self.valor = valor
        self.tipo_pagamento = tipo_pagamento
        self.data_pagamento = data_pagamento
        self.status = status

    def registrar_pagamento(self):
        self.status = 'Confirmado'

    def historico_pagamento(self):
        print(f'{self.status}!\nCPF: ({self.cpf}) | ID Cachorro ({self.id_cachorro})\nPlano ({self.tipo_plano}) | Valor: R${self.valor}\nMétodo de Pagamento: {self.tipo_pagamento} | Data ({self.data_pagamento}).')

t = Tutor('Giovana', 'giovana@nome', '19999999999', '12345677','rua')
c = Cachorro(1, 'Pandora', '', 'preto', 'vira-lata', '07-08-2020', '', 'pequeno', 'cenoura', True, t, '23/10/2026', 'Mensal')

remedio1 = Medicacao('1', 'Vermífugo','1 comprimido', '23/10/2026', '16:12','123')
remedio1.registrar_medicacao()

hospedagem1 = Estadia('123.456.789-00', 1, '23/10 a 28/10')
hospedagem1.registrar_pagamento()
pagamento1 = Pagamento('123.456.789-00', '1', 'Mensalidade Creche', 250.00, 'PIX', '23/10/2026')
print('Antes do Pagamento')
pagamento1.historico_pagamento()
print('\nDepois do Pagamento')
pagamento1.historico_pagamento()

print(c.tutor.nome)
