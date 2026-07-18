from Veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, modelo, consumo, tanque_atual, portas):
        super().__init__(modelo, consumo, tanque_atual)
        self.__portas = portas

    def get_portas(self):
        return self.__portas

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}Portas: {self.get_portas()}\nSituação: {super().get_situacao()}"