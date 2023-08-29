__version__ = "1.0"
import analizador.util
import lab5.solucion
import lab5.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        self.casos=[
            "XXX,___,___",
            "X__,X__,X__",
            "X__,_X_,__X",
            "__X,_X_,X__",
            "OOO,___,___",
            "O__,O__,O__",
            "O__,_O_,__O",
            "__O,_O_,O__",
            "XOX,OXO,OXO"
        ]

    def generar_tablero(self,caso):
        tablero=[]
        filas=caso.split(",")
        for fila in filas:
            tablero.append(list(fila))
        return tablero

    def analizar(self):
        for caso in self.casos:
            tablero=self.generar_tablero(caso)
            ev=lab5.solucion.revisar_vertical(tablero,0)
            eh=lab5.solucion.revisar_horizontal(tablero,0)
            ed=lab5.solucion.revisar_diagonal_derecha(tablero)
            ei=lab5.solucion.revisar_diagonal_izquierda(tablero)

            try:
                ov=self.modulo.revisar_vertical(tablero,0)
                if ov!=ev:
                    self.errores.append("revisar_vertical en {0} debe retornar {1} no {2}".format(caso,ev,ov))
            except ValueError:
                self.errores.append("Recuerda definir la función revisar_vertical")

            try:
                oh = self.modulo.revisar_horizontal(tablero, 0)
                if oh!=eh:
                    self.errores.append("revisar_horizontal en {0} debe retornar {1} no {2}".format(caso,eh,oh))
            except ValueError:
                self.errores.append("Recuerda definir la función revisar_horizontal")

            try:
                od = self.modulo.revisar_diagonal_derecha(tablero)
                if od!=ed:
                    self.errores.append("revisar_diagonal_derecha en {0} debe retornar {1} no {2}".format(caso,ed,od))
            except ValueError:
                self.errores.append("Recuerda definir la función revisar_diagonal_derecha")

            try:
                oi = self.modulo.revisar_diagonal_izquierda(tablero)
                if oi!=ei:
                    self.errores.append("revisar_diagonal_izquierda en {0} debe retornar {1} no {2}".format(caso,ei,oi))
            except ValueError:
                self.errores.append("Recuerda definir la función revisar_diagonal_izquierda")

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=lab5.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)