# Modelando un Auto

class Auto:
    
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento   # Km/L
        self.nivel_estanque = 0
        self.kilometraje = 0
        self.cuenta_kilometros = 0
    
    def __repr__(self):
        return str(self.rendimiento)+" Km/L"+ "   "+str(self.capacidad_estanque)+" litros por estanque"
    
    def cuenta_kilometros(self):
        return self.cuenta_kilometros

    def nivel_estanque(self):
        return self.nivel_estanque
    
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, travel_time):  # La unidad de travel_time son las horas
        if self.nivel_estanque<=0:
            return "El estanque esta en 0 L, para andar debe llenar el estanque"
        else:
            Km_recorridos = velocidad*travel_time            
            self.nivel_estanque -= (Km_recorridos/self.rendimiento)
            if self.nivel_estanque<0:
                Km_pendientes = self.nivel_estanque*(-1)*self.rendimiento
                self.kilometraje += Km_recorridos - Km_pendientes
                self.cuenta_kilometros += Km_recorridos - Km_pendientes
                nivel_estanque = 0
                print("Te has quedado sin gasolina y te quedan por recorrer: ", Km_pendientes, "Kms.")
                return Km_pendientes
            else:
                self.kilometraje += Km_recorridos
                self.cuenta_kilometros += Km_recorridos
                return 0        

    def llenar_estanque(self, x):
        self.nivel_estanque += x
        if self.nivel_estanque>self.capacidad_estanque:
            self.nivel_estanque -= x
            return self.capacidad_estanque, False
        else:
            return self.nivel_estanque, True

    def autonomia(self):
        autonomia = self.nivel_estanque*self.rendimiento
        return autonomia

if __name__ == "__main__":
    
    mazda2 = Auto(42, 12)
    auto=Auto(100,12)
