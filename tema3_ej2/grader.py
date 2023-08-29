__version__ = "1.0"
import analizador.util
import tema3_ej2.solucion
import math

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        x=1/math.sqrt(3)
        v1=self.modulo.Vector(x,x,x)
        v2=tema3_ej2.solucion.Vector(x,x,x)
        r=v1.norma()
        if r!=v2.norma():
            self.errores.append("El vector ({0},{1},{2}) es unitario, pero tu clase retorna {3}".format(x,x,x,r))

        v3=tema3_ej2.solucion.Vector(3,2,3)
        e=tema3_ej2.solucion.suma_vectores(v3,v3)

        v4=self.modulo.Vector(3,2,3)
        o=self.modulo.suma_vectores(v4,v4)

        if e.x!=o.x or e.y!=o.y or e.z!=o.z:
            self.errores.append("Al sumar (3,2,3)+(3,2,3) el resultado debiera ser (5,5,5), no ({0},{1},{2})".format(o.x,o.y,o.z))

        if len(self.errores)==0:
            self.score=2/3

        e=v3+v3
        o=v4+v4
        if e.x!=o.x or e.y!=o.y or e.z!=o.z:
            self.errores.append("Al sumar (3,2,3)+(3,2,3) con el operador + el resultado debiera ser (5,5,5), no ({0},{1},{2})".format(o.x,o.y,o.z))
