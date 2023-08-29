class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self,velocidad,tiempo):
        km = velocidad * tiempo
        self.cuenta_kilometros += km
        self.kilometraje += km
        self.nivel_estanque -= (km/self.rendimiento)

    def autonomia(self):
        A = self.rendimiento * self.nivel_estanque 
        return A
    def llenar_estanque(self,litros):
        act = litros + self.nivel_estanque
        if act > self.capacidad_estanque:
            cantmax = self.capacidad_estanque - self.nivel_estanque
            return cantmax,False
        elif act < self.capacidad_estanque:
            self.nivel_estanque = act
            return act,True
def paradas(auto, kilometros):
    kilometros_recorridos = auto.autonomia
    paradas = kilometros/auto.autonomia
    return paradas
            
if __name__ == "__main__":
    auto=Auto(100,12)
    viaje = int(input("cantidad de kilometros en el viaje: "))
    paradas(auto,viaje)
         