class Auto():
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
        return

    def andar(self,velocidad,tiempo):
        kilometros = velocidad*tiempo
        litros_usados = self.rendimiento//kilometros
        self.nivel_estanque = self.nivel_estanque - litros_usados
        if self.nivel_estanque < 0:
            litros_que_faltan = abs(self.nivel_estanque)
            self.nivel_estanque = 0
            self.kilometraje = kilometros - (litros_que_faltan*self.rendimiento)
            self.cuenta_kilometros = kilometros - (litros_que_faltan*self.rendimiento)
            return litros_que_faltan*self.rendimiento

        elif self.nivel_estanque >= 0:
            self.kilometraje = kilometros
            self.cuenta_kilometros = kilometros
            self.nivel_estanque = 50
            return 0

    def autonomia(self):
        return self.nivel_estanque*self.rendimiento

    def llenar_estanque(self,litros):
        if self.nivel_estanque + litros > self.capacidad_estanque:
            tupla = (self.capacidad_estanque,False)
            return tupla
        elif self.nivel_estanque + litros <= self.capacidad_estanque:
            self.nivel_estanque = self.nivel_estanque + litros
            tupla = (self.nivel_estanque,True)
            return tupla

if __name__ == "__main__":
    auto=Auto(100,12)
    auto.llenar_estanque(120)