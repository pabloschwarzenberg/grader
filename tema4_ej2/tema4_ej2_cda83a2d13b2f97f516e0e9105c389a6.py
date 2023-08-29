class Auto :
    def __init__(self,capacidad,rendimiento) :
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self) :
        self.cuenta_kilometros = 0

    def andar(self,velocidad,tiempo) :
        nivel = self.nivel_estanque - ((velocidad*tiempo) / self.rendimiento)
        self.kilometraje += velocidad * tiempo
        self.cuenta_kilometros += velocidad * tiempo
        if nivel < 0 :
            return 0 - nivel
        else :
            self.nivel_estanque = nivel
            return 0

    def autonomia(self) :
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self,litros) :
        if litros > self.capacidad_estanque - self.nivel_estanque :
            return (self.capacidad_estanque - self.nivel_estanque,False)
        else :
            self.nivel_estanque += litros

if __name__ == "__main__":
    auto=Auto(100,12)
         