class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
        return
    def andar(self,velocidad,tiempo):
        distancia = velocidad*tiempo
        litros = (distancia/self.rendimiento)
        self.kilometraje += distancia
        self.cuenta_kilometros += distancia
        if litros > self.nivel_estanque:
            return ((litros - self.nivel_estanque)* self.rendimiento)
        else:
            self.nivel_estanque -= litros
            return 0
    def autonomia(self):
        return (self.rendimiento*self.nivel_estanque)
    def llenar_estanque(self,litros):
        if (self.nivel_estanque + litros) > self.capacidad_estanque:
            return ((self.capacidad_estanque - self.nivel_estanque),False)
        else:
            self.nivel_estanque += litros
            return ((self.nivel_estanque),True)

if __name__ == "__main__":
    auto=Auto(100,12)
         