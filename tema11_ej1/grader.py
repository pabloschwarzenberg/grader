__version__ = "1.0"
import analizador.util
import tema11_ej1.solucion
import tema11_ej1.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        e=tema11_ej1.solucion.palindromo("oso")
        o=self.modulo.palindromo("oso")
        if e!=o:
            self.errores.append("La palabra oso es un palíndromo")
        e=tema11_ej1.solucion.palindromo("dinosaurio")
        o=self.modulo.palindromo("dinosaurio")
        if e!=o:
            self.errores.append("La palabra dinosaurio no es un palíndromo")

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema11_ej1.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)