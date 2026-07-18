
class Veiculo:
    def __init__(self, modelo, consumo, tanque_atual):
        self.__modelo = modelo
        self.__consumo = float(consumo)
        self.__tanque_atual = float(tanque_atual)
        self.__situacao = ''

    def get_modelo(self):
        return self.__modelo

    def get_consumo(self):
        return self.__consumo

    def get_tanque_atual(self):
        return self.__tanque_atual

    def get_situacao(self):
        return self.__situacao

    def get_autonomia_atual(self):
        autonomia_atual = self.get_tanque_atual() * self.get_consumo()
        return autonomia_atual

    def viagem(self, distancia):
        litros = float(distancia) / self.get_consumo()
        if float(distancia) <= self.get_autonomia_atual():
            self.__tanque_atual -= litros
        elif float(distancia) >= self.get_autonomia_atual():
            msg = (f"Combustível acabou aos {int(self.get_autonomia_atual())} Kms dos {distancia} Kms pretendido\n")
            self.__situacao = msg
            self.__tanque_atual = 0

    def exibir_detalhes(self, situacao="Ok"):
        return (f"\nModelo: {self.get_modelo()}\n"
                 f"Consumo: {self.get_consumo()} Km/litro\n"
            f"Tanque Atual: {self.get_tanque_atual():.2f}\n"
         f"Autonomia atual: {self.get_autonomia_atual():.2f}\n")
