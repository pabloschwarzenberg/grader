__version__ = "1.0"
import analizador.util
import tema8_ej2.solucion
import tema8_ej2.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        lista_r=tema8_ej2.solucion.buscarTodas("tres tristes tigres","t")
        lista_i=self.modulo.buscarTodas("tres tristes tigres","t")
        if lista_r != lista_i:
            self.errores.append("Al buscar t en 'tres tristes tigres' el resultado debiera ser {0}".format(lista_r))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema8_ej2.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)