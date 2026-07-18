from Veiculo import Veiculo


class Caminhao(Veiculo):
    def __init__(self, modelo, consumo, tanque_atual, carga_maxima):
        super().__init__(modelo, consumo, tanque_atual)
        self.__carga_maxima = carga_maxima

    def get_carga_maxima(self):
        return self.__carga_maxima

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}Carga Máxima: {self.get_carga_maxima()}\nSituação: {super().get_situacao()}"