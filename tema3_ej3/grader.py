__version__ = "1.0"
import analizador.util
import tema3_ej3.solucion

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        cuenta_1=self.modulo.Cuenta("12864303-6",10000)
        cuenta_2=tema3_ej3.solucion.Cuenta("12864303-6",10000)
        obtenido=cuenta_1.girar(3000)
        esperado=cuenta_2.girar(3000)
        if cuenta_1.saldo != cuenta_2.saldo:
            self.errores.append("La cuenta tenía un saldo inicial"
                                " de 10000, al girar 3000 debían quedar {0}".format(cuenta_2.saldo))
        cuenta_1.saldo=10000
        cuenta_2.saldo=10000
        obtenido=cuenta_1.girar(11000)
        esperado=cuenta_2.girar(11000)
        if obtenido!=esperado:
            self.errores.append("Un retiro de 11000 no se puede realizar,"
                                " por lo que girar debe retorna {0}".format(esperado))

if __name__ == "__main__":
    analizador=Analizador()
    analizador.modulo=tema3_ej3.solucion
    analizador.analizar()

