class Auto:
    def __init__(self, capacidad, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = float(capacidad)
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo
        litros = distancia / self.rendimiento

        if litros <= self.nivel_estanque:
            self.nivel_estanque -= litros
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        
        else:
            l_falta = litros - self.nivel_estanque
            d_falta = self.rendimiento * l_falta
            self.nivel_estanque = 0 
            self.kilometraje += distancia - d_falta
            self.cuenta_kilometros += distancia - d_falta
            return d_falta
        
    def autonomia(self):
        return self.rendimiento * self.nivel_estanque
    
    def llenar_estanque(self, litros):
        if self.capacidad_estanque < litros + self.nivel_estanque:
            return [self.capacidad_estanque, False]
        else:
            self.nivel_estanque += litros
            return [self.nivel_estanque, True]