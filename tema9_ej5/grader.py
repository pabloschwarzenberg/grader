__version__ = "1.0"
import analizador.util
import tema9_ej5.solucion
import tema9_ej5.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        esperado=tema9_ej5.solucion.JuegoDelGato()
        esperado.cargar_tablero([[-1,-1,0],[0,1,0],[1,1,0]])
        esperado.jugarRaton()

        observado=self.modulo.JuegoDelGato()
        observado.cargar_tablero([[-1,-1,0],[0,1,0],[1,1,0]])
        observado.jugarRaton()
        try:
            o=observado.mostrar_tablero()
        except ValueError:
            self.errores.append("El método mostrar_tablero no existe en tu clase")
        if not isinstance(o,list):
            self.errores.append("El método mostrar_tablero no retorna una lista de números")

        if o[0][2]!=-1:
            self.errores.append("Con el tablero [O,O, ],[ ,X, ],[X,X, ] el ratón debiera jugar en 0,2")

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema9_ej5.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)