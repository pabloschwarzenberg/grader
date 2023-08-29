class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
    def set_c_kilometros(self,cuenta_kilometros):
        self.cuenta_kilometros=cuenta_kilometros
    def set_kilometraje(self,kilometraje):
        self.kilometraje=kilometraje
    def set_nivel_estanque(self,nivel_estanque):
        self.nivel_estanque=nivel_estanque
    def get_kilometraje(self):
        return self.kilometraje
    def get_nivel_estanque(self):
        return self.nivel_estanque
    def get_cuenta_kilometros(self):
        return self.cuenta_kilometros
    def llenar_estanque(self,cantidad_litros):
        cantidad_litros_max = self.capacidad_estanque - self.nivel_estanque
        if cantidad_litros <= cantidad_litros_max:
            self.nivel_estanque = self.nivel_estanque + cantidad_litros
            return self.nivel_estanque, True
        else:
            return cantidad_litros_max, False
    def autonomia(self):
        kilometros_recorrer= self.nivel_estanque * self.rendimiento
        return kilometros_recorrer
    def andar(self,velocidad,tiempo_viaje):
        self.nivel_estanque = self.nivel_estanque - ((velocidad*tiempo_viaje)/self.rendimiento)
        self.kilometraje = self.kilometraje + (velocidad*tiempo_viaje)
        self.cuenta_kilometros = self.cuenta_kilometros + (velocidad*tiempo_viaje)
        if self.nivel_estanque > 0:
            return 0
        else:
            km_faltantes = (velocidad*tiempo_viaje) - (velocidad*tiempo_viaje*self.rendimiento)
            return km_faltantes
if __name__ == "__main__":
    auto=Auto(100,12)
         