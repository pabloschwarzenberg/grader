import analizador.util
import io
import sys
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        numeros=list(range(21))
        elecciones=[]
        while len(elecciones)<5:
            n=random.choice(numeros)
            numeros.remove(n)
            elecciones.append(n)
        self.setup=[[10,15,5,12,2],elecciones]
        self.precondiciones=[self.setup_caso1,self.setup_caso2]
        self.revisiones=[self.caso1,self.caso2]

    def setup_caso(self,i):
        sys.stdin=io.StringIO()
        for dato in self.setup[i]:
            sys.stdin.write("{0}\n".format(dato))
        sys.stdin.seek(0)
        sys.stdout=io.StringIO()

    def revisar_caso(self,i):
        salida=sys.stdout.getvalue().strip().lower()
        salidas=salida.split("\n")
        secuencia=[]
        j=0
        respuesta=False
        for linea_original in salidas:
            if respuesta:
                self.errores.append("Tu programa no termina después de indicar el número secreto")
                break
            linea=linea_original.replace(" ","")
            if linea.find("menor")!=-1:
                if j>5:
                    self.errores.append("Tu programa dio {0} intentos no 5".format(j))
                    break
                secuencia.append("<")
                j+=1
            elif linea.find("mayor")!=-1:
                if j>5:
                    self.errores.append("Tu programa dio {0} intentos no 5".format(j))
                    break
                secuencia.append(">")
                j+=1
            elif linea.find("noadivinaste")!=-1:
                respuesta=True
                if j<4:
                    self.errores.append("Tu programa dio {0} intentos no 5".format(j))
                    break
                p=linea.find("era")
                if p==-1:
                    self.errores.append("Cuando no adivinan tu programa no dice \"mi numero era ...\"")
                    break
                else:
                    numero=linea[p+3:]
                    numero=numero.replace(":","")
                    try:
                        numero=int(numero)
                    except:
                        self.errores.append("Tu programa dice {0} y no termina el mensaje con el número".format(linea_original))
                    for intento in self.setup[i]:
                        if intento==numero:
                            self.errores.append("Con la secuencia {0} tu programa dice NO ADIVINADO y tu numero era {1}".format(self.setup[i],numero))
                            break
            elif linea.find("adivinaste")!=-1:
                respuesta=True
                p=linea.find("era")
                if p==-1:
                    self.errores.append("Cuando adivinan tu programa no dice \"mi numero era ...\"")
                    break
                else:
                    numero=linea[p+3:]
                    numero=numero.replace(":","")
                    try:
                        numero=int(numero)
                    except:
                        self.errores.append("Tu programa dice {0} y no termina el mensaje con el número".format(linea_original))
                    encontrado=False
                    for intento in self.setup[i]:
                        if intento==numero:
                            encontrado=True
                            break
                    if(not encontrado):
                        self.errores.append("Con la secuencia {0} tu programa dice ADIVINADO y tu numero era {1}".format(self.setup[i],numero))
        if j<5 and not respuesta:
            self.errores.append("Tu programa dio {0} intentos no 5".format(j))

    def setup_caso1(self):
        self.setup_caso(0)

    def caso1(self):
        self.revisar_caso(0)

    def setup_caso2(self):
        self.setup_caso(1)

    def caso2(self):
        self.revisar_caso(1)

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)