class militaresBehavior:
    def ataque(self):
        pass

    def movimiento(self):
        pass

class soldadosBehavior(militaresBehavior):
    def ataque(self):
        print("Soldado atacando")

    def movimiento(self):
        print("Soldado moviendose")

class arquerosBehavior(militaresBehavior):
    def ataque(self):
        print("Arquero disparando")

    def movimiento(self):
        print("Arquero moviendose")

class caballerosBehavior(militaresBehavior):
    def ataque(self):
        print("Caballero andando")

    def movimiento(self):
        print("Caballero andando")

class militares:
    def __init__(self, behavior):
        self.behavior=behavior

    def perform_ataque(self):
        self.behavior.ataque()

    def perform_movimiento(self):
        self.behavior.movimiento()

if __name__=="__main__":
    soldados=militares(soldadosBehavior())
    arqueros=militares(arquerosBehavior())
    caballeros=militares(caballerosBehavior())

    soldados.perform_ataque()
    soldados.perform_movimiento()

    arqueros.perform_ataque()
    arqueros.perform_movimiento()

    caballeros.perform_ataque()
    caballeros.perform_movimiento()
