class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
        pass
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
    
    def andar(self, velocidad, tiempo):
        litros_necesarios = velocidad * tiempo / self.rendimiento
    
        if litros_necesarios <= self.nivel_estanque:
            self.kilometraje += velocidad * tiempo
            self.cuenta_kilometros += velocidad * tiempo
            self.nivel_estanque -= litros_necesarios
            return 0
        else:
            km_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += (velocidad * tiempo) - km_faltantes
            self.cuenta_kilometros += (velocidad * tiempo) - km_faltantes
            self.nivel_estanque = 0
            return km_faltantes
            
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if self.nivel_estanque + litros <= self.capacidad_estanque:
            self.nivel_estanque += litros
            return (self.nivel_estanque, True)
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return (max_litros, False)

if __name__ == "__main__":
    auto=Auto(100,12)
         