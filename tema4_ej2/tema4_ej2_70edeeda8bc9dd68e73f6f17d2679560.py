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
        litros_consumidos = distancia / self.rendimiento

        if litros_consumidos <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_consumidos
            return 0
        else:
            kilometros_faltantes = (litros_consumidos - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - kilometros_faltantes
            self.cuenta_kilometros += distancia - kilometros_faltantes
            self.nivel_estanque = 0
            return kilometros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        litros_permitidos = self.capacidad_estanque - self.nivel_estanque

        if cantidad_litros <= litros_permitidos:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            return litros_permitidos, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    # Simulación de un viaje
    auto.reiniciar_cuentakilometros()
    distancia_viaje = 500
    velocidad = 80
    tiempo = distancia_viaje / velocidad

    while True:
        faltante = auto.andar(velocidad, tiempo)
        if faltante == 0:
            break
        else:
            print("¡Se quedó sin combustible! Faltaron recorrer", round(faltante, 2), "kilómetros.")
            cantidad_litros = float(input("Ingrese la cantidad de litros para llenar el estanque: "))
            litros_disponibles, exito = auto.llenar_estanque(cantidad_litros)
            if not exito:
                print("No se puede llenar el estanque con esa cantidad. Se llenará con", litros_disponibles, "litros.")
            print("Estanque llenado. Se continuará el viaje.")

    print("El viaje ha finalizado. Total de kilómetros recorridos:", auto.kilometraje)
    print("Autonomía actual:", auto.autonomia())
