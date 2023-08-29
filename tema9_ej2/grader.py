__version__ = "1.0"
import analizador.util
import tema9_ej2.plantilla
import tema9_ej2.solucion

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        e1=tema9_ej2.solucion.Matriz([[1,2],[3,4]])
        e2=tema9_ej2.solucion.Matriz([[5,6],[7,8]])
        e=e1*e2

        o1=self.modulo.Matriz([[1,2],[3,4]])
        o2=self.modulo.Matriz([[5,6],[7,8]])
        o=o1*o2

        if e.celdas[0][0] != o.celdas[0][0] or e.celdas[0][1] != o.celdas[0][1] or\
                        e.celdas[1][0] != o.celdas[1][0] or e.celdas[1][1] != o.celdas[1][1]:
            self.errores.append("{0} * {1} debiera retornar {2}".format(e1.celdas,e2.celdas,e.celdas))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema9_ej2.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)