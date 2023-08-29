__version__ = "1.0"
import analizador.util
import tema4_ej2.solucion
import tema4_ej2.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        referente=tema4_ej2.solucion.Auto(100,12)
        try:
            auto=self.modulo.Auto(100,12)
        except ValueError:
            self.errores.append("Recuerda definir el constructor en la clase Auto")
            return
        auto.llenar_estanque(60)
        referente.llenar_estanque(60)
        if auto.nivel_estanque!=60:
            self.errores.append("Cuando se crea el auto el estanque parte en 0, al agregarle 60 litros nivel_estanque debe ser 60")
        auto.llenar_estanque(60)
        referente.llenar_estanque(60)
        if auto.nivel_estanque!=60:
            self.errores.append("Si se crea un auto con 100 litros de capacidad no debe permitir llenarlo con 120 litros")

        if auto.autonomia() != referente.autonomia():
            self.errores.append("Un auto con 12 km/l de rendimiento y 60 litros tiene autonomía de {0}".format(referente.autonomia()))
        auto.andar(120,1)
        referente.andar(120,1)
        if auto.nivel_estanque != referente.nivel_estanque:
            self.errores.append("Después de viajar 1 hr a 120 km/h el estanque debiera quedar con {0} l, con rendimiento=12 km/l y estanque con 60 litros".format(referente.nivel_estanque))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema4_ej2.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)