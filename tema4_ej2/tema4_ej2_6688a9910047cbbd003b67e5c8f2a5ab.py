class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
        self.cuenta_kilometros = 0
    def reiniciar_cuenta_kilometros(self):
        self.cuenta_kilometros = 0
    def andar(self,velocidad,tiempo_viaje):
        kilometros_recorridos = velocidad * tiempo_viaje
        litros_gastados = kilometros_recorridos / self.rendimiento
        if litros_gastados > self.nivel_estanque:
            distancia_maxima = self.rendimiento*self.nivel_estanque
            self.nivel_estanque = 0
            self.kilometraje += distancia_maxima
            self.cuenta_kilometros += distancia_maxima
            return kilometros_recorridos - distancia_maxima
        else:
            self.nivel_estanque = self.nivel_estanque - litros_gastados
            self.kilometraje += kilometros_recorridos
            self.cuenta_kilometros += kilometros_recorridos
            return 0
    def autonomia(self):
        kilometros_por_andar = self.rendimiento * self.nivel_estanque
        return kilometros_por_andar
    def llenar_estanque(self,cantidad):
        if self.nivel_estanque + cantidad > self.capacidad_estanque:
            return (self.capacidad_estanque,False)
        else:
            self.nivel_estanque = self.nivel_estanque + cantidad
            return (self.nivel_estanque,True)
        

if __name__ == "__main__":
    auto=Auto(100,12)
         