from Carro import Carro
from Caminhao import Caminhao



class Gerenciador:
    def __init__(self):
        self.carro = Carro("Argo", 14, 60, 4)
        self.caminhao = Caminhao("Mercedes", 9, 200, 5000)

    def simula_viagem(self):
        while True:
            print("\nDados dos veiculos na viagem:")
            print(self.carro.exibir_detalhes())
            print(self.caminhao.exibir_detalhes())

            input("Aperte Enter para prosseguir...")
            escolha = input("Escolha o veiculo (1 - Carro  |  2 - Caminhao : ")

            if escolha == '1':
                if self.carro.get_tanque_atual() > 0:
                    distancia = input("\nQual a distancia em km da viagem: ")
                    self.carro.viagem(distancia)
                else:
                    print(f"{self.carro.get_modelo()} está sem combustível! Não pode mais viajar\n")
                    print(self.carro.exibir_detalhes())

            elif escolha == '2':
                if self.caminhao.get_tanque_atual() > 0:
                    distancia = input("\nQual a distancia em km da viagem: ")
                    self.caminhao.viagem(distancia)
                else:
                    print(f"{self.caminhao.get_modelo()} está sem combustível! Não pode mais viajar\n")
                    print(self.caminhao.exibir_detalhes())

            else:
                print("\nEscolha inválida! escolha novamente...")

            if self.caminhao.get_tanque_atual() == 0 and self.carro.get_tanque_atual() == 0:
                print("\nDados dos veiculos na viagem:")
                print(self.carro.exibir_detalhes())
                print(self.caminhao.exibir_detalhes())
                break
