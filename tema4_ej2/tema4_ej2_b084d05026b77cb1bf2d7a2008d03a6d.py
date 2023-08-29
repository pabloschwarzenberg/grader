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
        restante = 0
        kilometros = velocidad*tiempo
        completo = False
        if kilometros <= self.autonomia():
            completo = True
            self.kilometraje += kilometros
            self.cuenta_kilometros += kilometros
            self.nivel_estanque = self.nivel_estanque - kilometros/(self.rendimiento)
        else:
            restante = kilometros - autonomia
            self.kilometraje += autonomia
            self.cuenta_kilometros += autonomia
            self.nivel_estanque = 0
        if completo:
            return 0
        else:
            return restante
            

    def autonomia(self):
        k = (self.rendimiento)*(self.nivel_estanque)
        return k

    def llenar_estanque(self, cantidad):
        llena = False
        max_cap = (self.capacidad_estanque - self.nivel_estanque)
        if cantidad <= max_cap:
            llena = True
            self.nivel_estanque += cantidad
        if llena:
            return tuple([self.nivel_estanque, llena])
        else:
            return tuple([max_cap, llena])
        

if __name__ == "__main__":
    auto=Auto(100,12)

         