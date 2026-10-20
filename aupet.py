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


t = Tutor('Giovana', 'giovana@nome', '19999999999', '12345677','rua')
c = Cachorro(1, 'Pandora', '', 'preto', 'vira-lata', '07-08-2020', '', 'pequeno', 'cenoura', True, t)

print(c.tutor.nome)
