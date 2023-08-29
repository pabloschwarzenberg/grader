import analizador.util
import tema8_ej5.solucion
import tema8_ej5.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        esperado=tema8_ej5.solucion.FechaHora()
        observado=self.modulo.FechaHora()

        esperado.fijarFechaHora("30-09-2015 17:45:00")
        observado.fijarFechaHora("30-09-2015 17:45:00")
        if str(esperado)!=str(observado):
            self.errores.append("Al fijar 30-09-2015 17:45:00 el resultado debiera ser {0}".format(str(esperado)))

        esperado.cambiar("mm=10")
        observado.cambiar("mm=10")
        if str(esperado)!=str(observado):
            self.errores.append("Al cambiar mm=10 el resultado debiera ser {0}".format(str(esperado)))

        esperado.fijarHora("18:00:00")
        esperado.cambiar("aaaa = 2016")
        observado.fijarHora("18:00:00")
        observado.cambiar("aaaa = 2016")
        if str(esperado)!=str(observado):
            self.errores.append("Al fijar hora 18:00:00 y cambiar aaaa = 2016 el resultado debiera ser {0}".format(str(esperado)))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema8_ej5.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)
