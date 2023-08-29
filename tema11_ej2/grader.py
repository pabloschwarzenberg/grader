import analizador.util
import tema11_ej2.solucion
import tema11_ej2.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        expresiones=["2+3","2-3","2++","--2","2-"]
        for expresion in expresiones:
            e=tema11_ej2.solucion.validar_expresion(expresion)
            o=self.modulo.validar_expresion(expresion)
            if e!=o:
                self.errores.append("Al validar {0} el resultado debe ser {1}".format(expresion,e))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema11_ej2.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)
