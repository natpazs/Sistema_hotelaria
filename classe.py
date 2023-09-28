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

class MasterQuarto(Quarto):
    pass

class DeluxeQuarto(Quarto):
    pass

class CasalQuarto(Quarto):
    pass

class CasalQuartoDuplo(Quarto):
    pass

class SolteiroQuarto(Quarto):
    pass

class SolteiroQuartoDuplo(Quarto):
    pass