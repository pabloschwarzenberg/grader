class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo_viaje):
        kilometros = velocidad * tiempo_viaje
        print(kilometros)
        kilometros_recorridos = 0
        ronda = 1
        while kilometros_recorridos != kilometros and self.nivel_estanque != 0:
            kilometros_recorridos += 1
            print(kilometros_recorridos)
            self.kilometraje += 1
            self.cuenta_kilometros += 1
            if kilometros_recorridos/ronda == self.rendimiento:
                ronda += 1
                self.nivel_estanque -= 1
        kilometros_faltantes = kilometros - kilometros_recorridos
        return kilometros_faltantes

    def autonomia(self):
        kilometros_recorribles = self.nivel_estanque * self.rendimiento
        return kilometros_recorribles

    def llenar_estanque(self, litros):
        if self.capacidad_estanque < self.nivel_estanque + litros:
            validar = False
            cantidad_maxima = self.capacidad_estanque - self.nivel_estanque
        else:
            validar = True
            cantidad_maxima = self.nivel_estanque + litros
            self.nivel_estanque = self.nivel_estanque + litros
        tupla = (cantidad_maxima, validar)
        return tupla

if __name__ == "__main__":
    auto=Auto(100,12)
         