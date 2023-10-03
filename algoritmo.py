from classe import *
import os

hotel = Hotel("Hotel", "Av.Qualquer, 123", "12345678901234")

quartoMaster = MasterQuarto(300)
quartoDeluxe = DeluxeQuarto(200)
quartoCasal = CasalQuarto(120)
quartoCasal2 = CasalQuartoDuplo(150)
quartoSolteiro = SolteiroQuarto(80)
quartoSolteiro2 = SolteiroQuartoDuplo(100)

hotel.quartos.extend([quartoMaster, quartoDeluxe, quartoCasal, quartoCasal2, quartoSolteiro, quartoSolteiro2])

def main():
    a = True
    while a == 1:
        try:
            print("Bem vindo ao Hotel")
            print("--- MENU ---")
            print("01 - Cadastrar Cliente")
            print("02 - Visualizar quartos disponiveis")
            print("03 - Fazer reserva")
            print("04 - Sair")

            menu = int(input("Qual opção você deseja? \n -"))
            os.system("pause")
            os.system("cls")


            match menu:
                case 1:
                    nome = input("Qual o nome do cliente: ") 
                    email = input("Qual o email do cliente: ")
                    cpf = int(input("Qual o cpf do cliente: "))
                    hotel.cadastrarCliente(nome, email, cpf)

                case 2:
                    disponiveis = hotel.listarDisponiveis()
                    for quarto in disponiveis:
                        print(f"Quarto disponível: {quarto.getDescricao()} - Valor: R${quarto.valor}")

                case 3:
                    quarto = input("Informe o quarto que será reservado: ")
                    cliente = input("Informe o cliente que o reservará: ")
                    hotel.fazerReserva(quarto, cliente)

                case 4:
                    break

                case _:
                    print("Valor invalido")
        
        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)                    