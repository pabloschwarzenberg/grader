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
        distancia = velocidad * tiempo
        litros_necesarios = distancia / self.rendimiento
        
        if litros_necesarios <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_necesarios
            return 0
        else:
            km_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += km_faltantes
            self.cuenta_kilometros += km_faltantes
            self.nivel_estanque = 0
            return km_faltantes
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    viaje = [(100, 2), (90, 3), (120, 1), (80, 4)] 
    
    detenciones = 0
    
    for tramo in viaje:
        velocidad, tiempo = tramo
        resultado = auto.andar(velocidad, tiempo)
        
        if resultado > 0:
            detenciones += 1
            max_litros, _ = auto.llenar_estanque(resultado)
            print("Detenerse a cargar combustible. Máxima cantidad de litros:", max_litros)
    
    print("Cantidad de detenciones necesarias:", detenciones)
