__version__ = "1.0"
import analizador.util
import tema8_ej3.solucion
import tema8_ej3.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        estadisticas_r=tema8_ej3.solucion.estadisticas_frase(tema8_ej3.solucion.hombre_imaginario)
        estadisticas_i=self.modulo.estadisticas_frase(tema8_ej3.solucion.hombre_imaginario)
        if estadisticas_r!=estadisticas_i:
            self.errores.append("Al usar como frase el extracto del hombre imaginario las estadísticas debieran ser: {0}".format(
                estadisticas_r))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema8_ej3.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)