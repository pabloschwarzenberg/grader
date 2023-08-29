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
        # Calculamos la distancia recorrida
        distancia = velocidad * tiempo
        # Calculamos los litros de combustible consumidos
        litros_consumidos = distancia / self.rendimiento
        # Si no hay suficiente combustible, retornamos la cantidad de kilómetros faltantes
        if litros_consumidos > self.nivel_estanque:
            faltantes = (litros_consumidos - self.nivel_estanque) * self.rendimiento
            self.nivel_estanque = 0
            self.cuenta_kilometros += distancia
            self.kilometraje += distancia
            return faltantes
        # Si hay suficiente combustible, actualizamos los valores y retornamos 0
        else:
            self.nivel_estanque -= litros_consumidos
            self.cuenta_kilometros += distancia
            self.kilometraje += distancia
            return 0
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, litros):
        if litros > self.capacidad_estanque:
            return (self.capacidad_estanque, False)
        else:
            self.nivel_estanque = litros
            return (self.nivel_estanque, True)
