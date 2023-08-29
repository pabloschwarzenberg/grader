class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta = 0
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.nivel_estanque = 0
    def reiniciar_cuentakilometros(self):
        self.cuenta = 0

    def autonomia(self):
        return self.rendimiento*self.nivel_estanque

    def andar(self,velocidad,tiempo):
        quiere_andar = velocidad*tiempo
        new_nivel = self.nivel_estanque - quiere_andar / self.rendimiento
        if new_nivel < 0:
            excedente = abs(new_nivel)
        else:
            excedente = 0
            self.kilometraje += quiere_andar
            self.cuenta += quiere_andar
            self.nivel_estanque = new_nivel
        return excedente
    def llenar_estanque(self,litros):
        llenado = litros + self.nivel_estanque
        if llenado > self.capacidad_estanque:
            return tuple([self.capacidad_estanque,False])
        else:
            self.nivel_estanque = llenado
            return tuple([self.nivel_estanque, True])

if __name__ == "__main__":
    auto = Auto(100, 12)
