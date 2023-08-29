__version__ = "1.0"
import analizador.util
import tema4_ej1.solucion
import tema4_ej1.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        palabra=self.modulo.ocultar_letras("lepidoptero",4)
        if palabra.count("_")!=4:
            self.errores.append("Si ocultas 4 letras en lepidoptero tu funcion retorna {0}".format(palabra))
        palabra=self.modulo.revisar_letra("lepidoptero","le_i_opter_","o")
        if palabra!="le_i_optero":
            self.errores.append("Al probar o en le_i_opter_ tu funcion retorna {0}".format(palabra))

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion2.py")
    for error in analizador.errores:
        print(error)