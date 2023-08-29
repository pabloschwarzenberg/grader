__version__ = "1.0"
import analizador.util
import tema9_ej3.plantilla
import tema9_ej3.solucion

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        esperado=tema9_ej3.solucion.decodificar("01101000,01101111,01101100,01100001")
        observado=self.modulo.decodificar("01101000,01101111,01101100,01100001")
        if esperado!=observado:
            self.errores.append("Al decodificar 01101000,01101111,01101100,01100001 el resultado debiera ser {0}"
                                .format(esperado))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema9_ej3.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)