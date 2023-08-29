class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
    def andar(self,velocidad,tiempo_de_viaje):
        self.nivel_estanque = capacidad_estanque
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        for t in range(tiempo_de_viaje):
            self.cuenta_kilometros = velocidad*t
            kilometraje += self.cuenta_kilometros
            self.nivel_estanque = self.capacidad_estanque - cuenta_kilometros/self.rendimiento
            if self.nivel_estanque == 0:
                print("Faltaron ",velocidad*tiempo_de_viaje - cuenta_kilometros," kilómetros")
    def autonomia(self):
        return nivel_estanque*self.rendimiento
    def llenar_estanque(self,recarga):
        if recarga < self.capacidad_estanque:
            nivel_estanque = recarga
        else:
            return (capacidad_estanque, False)
    #    nivel_estanque = capacidad_estanque


if __name__ == "__main__":
    auto=Auto(100,12)
         