__version__ = "1.0"
import analizador.util

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        r1=self.modulo.es_primo(1)
        if r1!=False:
            self.errores.append("El 1 no es primo y tu función retorna {0}".format(r1))

        r1=self.modulo.es_primo(24)
        if r1!=False:
            self.errores.append("El 24 no es primo y tu función retorna {0}".format(r1))

        r1=self.modulo.es_primo(3)
        if r1!=True:
            self.errores.append("El 3 es primo y tu función retorna {0}".format(r1))

        r1=self.modulo.es_primo(11)
        if r1!=True:
            self.errores.append("El 11 es primo y tu función retorna {0}".format(r1))
