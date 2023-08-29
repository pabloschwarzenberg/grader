class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        kilometros_a_andar = velocidad*tiempo
        recorrido = self.rendimiento*self.nivel_estanque - kilometros_a_andar
        if recorrido >= 0:
            self.nivel_estanque = 0 + recorrido/self.rendimiento
            self.kilometraje += kilometros_a_andar
            self.cuenta_kilometros += kilometros_a_andar
            return 0
        else:
            self.nivel_estanque = 0
            self.kilometraje += kilometros_a_andar + recorrido
            self.cuenta_kilometros += kilometros_a_andar + recorrido
            return abs(recorrido)      
        
    def autonomia(self):
        self.autonomia = self.rendimiento*self.nivel_estanque
        return self.autonomia

    def llenar_estanque(self, cantidad_de_litros):
        if self.nivel_estanque + cantidad_de_litros > self.capacidad_estanque:
            return [self.capacidad_estanque, False]
        else:
            self.nivel_estanque += cantidad_de_litros
            return [self.nivel_estanque + cantidad_de_litros, True]

if __name__ == "__main__":
    auto=Auto(100,12)
         