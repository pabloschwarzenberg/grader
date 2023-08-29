class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad = capacidad_estanque   #capacidad de bencina que puede guardar el auto
        self.rendimiento = rendimiento        #Kilometros/Litro
        self.kilometraje = 0                       #Kilometros que tiene el auto
        self.cuenta_kilometros = 0                 #Kilometros del auto, se puede reiniciar
        self.nivel_estanque = 0                    #nivel actual de bencina. es <= capacidad

    def reiniciar_cuentakilometros(self):
        cuenta_kilometros = 0

    def andar(self,velocidad,tiempo):
        self.nivel_estanque = self.nivel_estanque - (velocidad*tiempo)/self.rendimiento
        kilometros_faltantes = velocidad*tiempo - self.rendimiento*self.capacidad
        if self.nivel_estanque <= 0:
            self.kilometraje += self.rendimiento*self.capacidad
            self.cuenta_kilometros += self.rendimiento*self.capacidad
            self.nivel_estanque = 0
            return velocidad*tiempo - self.rendimiento*self.capacidad
        else:
            self.kilometraje += velocidad*tiempo
            self.cuenta_kilometros += velocidad*tiempo
            return 0

    def autonomia(self):
        autonomia = self.nivel_estanque*self.rendimiento
        return autonomia

    def llenar_estanque(self,litros):
        if self.nivel_estanque+litros > self.capacidad:
            return [[self.capacidad,False]]
        else:
            self.nivel_estanque += litros
            return [[self.nivel_estanque+litros,True]]