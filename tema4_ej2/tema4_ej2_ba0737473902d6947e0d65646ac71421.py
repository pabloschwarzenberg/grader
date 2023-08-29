class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje =0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=int(rendimiento)

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo_viaje):
        kilometros=int(velocidad)*int(tiempo_viaje)
        litros_consumidos=kilometros/self.rendimiento
        if litros_consumidos<=self.nivel_estanque:
            self.kilometraje=self.kilometraje+kilometros
            self.cuenta_kilometros=self.cuenta_kilometros+kilometros
            self.nivel_estanque=self.nivel_estanque-litros_consumidos
            return 0
        else:
            kilometros_recorridos=self.nivel_estanque*self.rendimiento
            self.kilometraje=self.kilometraje+kilometros_recorridos
            self.cuenta_kilometros=self.cuenta_kilometros+kilometros_recorridos
            self.nivel_estanque=0
            return (kilometros-kilometros_recorridos)
        
    def autonomia(self):
        kilometros=self.nivel_estanque*self.rendimiento
        return kilometros
    
    def llenar_estanque(self,litros):
        if self.nivel_estanque+int(litros)>self.capacidad_estanque:
            return ((self.capacidad_estanque-self.nivel_estanque),False)
        else:
            self.nivel_estanque=self.nivel_estanque+int(litros)
            return (self.nivel_estanque,True)


if __name__ == "__main__":
    auto = Auto(100, 12)
     