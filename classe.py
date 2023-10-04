class Hotel:
    def __init__(self, nome, endereço, cnpj):
        self.nome = nome
        self.endereço = endereço
        self.cnpj = cnpj
        self.quartos = []
        self.clientes = {}
        self.reservas = []

    def cadastrarCliente(self, nome, email, cpf):
        self.clientes[nome] = {'CPF': cpf, 'Email': email}
        print("Cliente cadastrado com sucesso!")

    def listarClientes(self):
        for chave, valor in self.clientes.items():
            print(f"Nome: {chave}, CPF: {valor['CPF']}, Email: {valor['Email']}")

    def listarDisponiveis(self):
        disponivel = [quarto for quarto in self.quartos if not quarto.getOcupado()]
        return disponivel

    def fazerReserva(self, quarto, cliente):
        if quarto in self.listarDisponiveis():
            reserva = {"Ciente:", cliente, "Quarto:", quarto}
            quarto.setOcupado(True)
            self.reservas.append(reserva)


class Quarto:
    def __init__(self, valor, descrição):
        self.valor = valor
        self.descrição = descrição
        self.ocupado = False 

    def getOcupado(self):
        return self.ocupado
    
    def setOcupado(self, ocupado):
        self.ocupado = ocupado

    def getDescrição(self):
        return self.descrição
    
    def setDescrição(self, descrição):
        self.descrição = descrição

class MasterQuarto(Quarto):
    def __init__(self, valor):
        self.valor = valor
        self.descrição = "É um espaço projetado para oferecer conforto, privacidade e luxo aos hóspedes. É um espaço onde eles podem relaxar, recarregar as energias e desfrutar de comodidades adicionais. Contém: Banheiro privativo, closet, área de estar e varanda."

class DeluxeQuarto(Quarto):
     def __init__(self, valor):
        self.valor = valor
        self.descrição = "Um quarto deluxe é uma opção de acomodação que oferece um nível mais elevado de conforto, estilo e comodidades do que um quarto padrão. Contém: Banheiro privativo e área de estar"

class CasalQuarto(Quarto):
    def __init__(self, valor):
        self.valor = valor
        self.descrição = "Um quarto de casal é um espaço projetado para atender às necessidades e preferências de um casal, proporcionando um ambiente confortável e acolhedor para descansar, relaxar e desfrutar de momentos juntos. Contém: Baheiro privativo, cama de casal e uma pequena área de descanso."

class CasalQuartoDuplo(Quarto):
    def __init__(self, valor):
        self.valor = valor
        self.descrição = "Um quarto de casal é um espaço projetado para atender às necessidades e preferências de um casal, proporcionando um ambiente confortável e acolhedor para descansar, relaxar e desfrutar de momentos juntos. Contém: Baheiro privativo, duas camas de casal e uma pequena área de descanso."

class SolteiroQuarto(Quarto):
     def __init__(self, valor):
        self.valor = valor
        self.descrição = "É um espaço pessoal projetado para atender às necessidades e preferências de uma única pessoa. Contém: Banheiro privativo e uma cama de solteiro."

class SolteiroQuartoDuplo(Quarto):
    def __init__(self, valor):
        self.valor = valor
        self.descrição = "É um espaço pessoal projetado para atender às necessidades e preferências de duas pessoas. Contém: Banheiro privativo e duas camas de solteiro."

quarto = Quarto(100, "aa")