class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def autonomia(self):
        return self.rendimiento * self.nivel_estanque

    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo

        rendir = self.capacidad_estanque * self.rendimiento
        if rendir >= distancia:
            self.kilometraje = self.kilometraje + distancia
            self.cuenta_kilometros = self.cuenta_kilometros + distancia
            self.nivel_estanque -= distancia / self.rendimiento
            return 0
        else:
            recorrido = distancia - rendir
            self.kilometraje = self.kilometraje + recorrido
            self.cuenta_kilometros = self.cuenta_kilometros + recorrido
            self.nivel_estanque -= recorrido / self.rendimiento
            return recorrido

    def llenar_estanque(self, litros_nuevos):
        nuevos_litros = self.nivel_estanque + litros_nuevos
        if litros_nuevos > self.capacidad_estanque or nuevos_litros > self.capacidad_estanque:
            return (self.capacidad_estanque == False)
        else:
            self.nivel_estanque = nuevos_litros
            return (self.nivel_estanque == True)

        
        
            
if __name__ == "__main__":
    auto=Auto(100,12)





if __name__ == "__main__":
 a1=Auto("60","12")
 a2=Auto("40","8")
 print(a1)
         