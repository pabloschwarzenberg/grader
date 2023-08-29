class Auto:
    
    def __init__(self,capacidad_estanque,rendimiento,kilometraje=0,cuenta_kilometros=0,nivel_estanque=0):
        self.kilometraje = kilometraje
        self.cuenta = cuenta_kilometros
        self.capacidad = capacidad_estanque
        self.nivel_estanque = nivel_estanque
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta=0

    def andar(self,velocidad,tiempo_viaje):
        litros_usados=velocidad*tiempo_viaje/self.rendimiento
        if self.nivel_estanque - litros_usados >= 0:
            self.kilometraje += self.kilometraje + velocidad*tiempo_viaje
            self.cuenta += self.cuenta + velocidad*tiempo_viaje
            self.nivel_estanque=self.nivel_estanque -litros_usados
            return 0
        else:
            self.nivel_estanque=0
            kilometros_faltan=(velocidad*tiempo_viaje)-(self.rendimiento*self.nivel_estanque)
            return kilometros_faltan
        
    def autonomia(self):
        hola=(self.rendimiento*self.nivel_estanque)
        return hola

    def llenar_estanque(self,cantidad_litros):
        if self.nivel_estanque+cantidad_litros>self.capacidad:
            s=self.capacidad-self.nivel_estanque
            return s,False
        else:
            s=self.nivel_estanque+cantidad_litros
            self.nivel_estanque += cantidad_litros
            return s,True

if __name__ == "__main__":
    auto=Auto(100,12)
    kilometros_recorrer=int(input("cuantos kilometros va a recorrer?"))
    contador=0
    while auto.cuenta<kilometros_recorrer:
        auto.llenar_estanque(100)
        auto.andar(100,12)
        contador += 1
    print(contador)