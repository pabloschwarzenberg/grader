__version__ = "1.0"
import analizador.util
import tema3_ej4.solucion
import tema3_ej4.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        fe1=tema3_ej4.solucion.Fraccion(1,2)
        fe2=tema3_ej4.solucion.Fraccion(3,4)
        re1=fe1+fe2
        re2=fe1-fe2
        re3=fe1*fe2
        re4=fe1/fe2

        f1=self.modulo.Fraccion(1,2)
        f2=self.modulo.Fraccion(3,4)
        ro1=f1+f2
        ro2=f1-f2
        ro3=f1*f2
        ro4=f1/f2

        if re1.a_numero() != ro1.a_numero():
            self.errores.append("El resultado de 1/2 + 3/4 es incorrecto, debe equivaler a {0}".format(re1.a_numero()))
        if re2.a_numero() != ro2.a_numero():
            self.errores.append("El resultado de 1/2 - 3/4 es incorrecto, debe equivaler a {0}".format(re2.a_numero()))
        if re3.a_numero() != ro3.a_numero():
            self.errores.append("El resultado de 1/2 * 3/4 es incorrecto, debe equivaler a {0}".format(re3.a_numero()))
        if re4.a_numero() != ro4.a_numero():
            self.errores.append("El resultado de 1/2 / 3/4 es incorrecto, debe equivaler a {0}".format(re4.a_numero()))

if __name__ == "__main__":
    analizador=Analizador()
    analizador.modulo=tema3_ej4.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)