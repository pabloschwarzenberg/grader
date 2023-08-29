class FechaHora:
    def __init__(self):

        self.segundo=0
        self.minuto=0
        self.hora=0
        self.dia=0
        self.mes=0
        self.año=0

    def __str__(self):

        return str(self.año)+"/"+str(self.mes)+"/"+str(self.dia)+" "+str(self.hora)+":"+str(self.minuto)+":"+str(self.segundo)

    def fijarFecha(self,fecha):

        if ("/"in fecha)==True:

            f=fecha.split("/")

        elif ("-" in fecha)==True:

            f=fecha.split("-")

        self.año=str(f[2])

        self.mes=str(f[1])

        self.dia=str(f[0])
        


    def fijarHora(self,hora):
        h=hora.split(":")

        self.hora=str(h[0])
        self.minuto=str(h[1])
        self.segundo=str(h[2])

    def fijarFechaHora(self,fechahora):
        lista=fechahora.split()

        fecha=lista[0]

        if ("/" in fecha)==True:

            l_fecha=fecha.split("/")

        elif("-" in fecha)==True:

            l_fecha=fecha.split("-")

        lista[0]=l_fecha

        hora=lista[1]

        l_hora=hora.split(":")

        lista[1]=l_hora

        self.segundo=str(lista[1][2])
        self.minuto=str(lista[1][1])
        self.hora=str(lista[1][0])
        self.dia=str(lista[0][0])
        self.mes=str(lista[0][1])
        self.año=str(lista[0][2])

        

    def cambiar(self,parte):

        s=""

        parte=parte.split("=")

        palabra=parte[0]

        while (" " in palabra)==True:

            palabra=palabra.strip(" ")

        s=palabra

        numero1=parte[1]

        while (" " in numero1)==True:

            numero1=numero1.strip(" ")

        numero=int(numero1)


        if s=="aaaa":

            if numero>0:

                self.año=numero1

            else:

                print("Numero fuera de rango")

        elif s=="mm":

            if numero>=1 and numero<=12:

                self.mes=numero1

            else:

                print("Numero fuera de rango")

        elif s=="dd":

            if numero>=1 and numero<=31:

                self.dia=numero1

            else:

                print("Numero fuera de rango")

        elif s=="HH":

            if numero>=1 and numero<=24:

                self.hora=numero1

            else:

                print("Numero fuera de rango")

        elif s=="MM":

            if numero>=0 and numero<=59:

                self.minuto=numero1

            else:

                print("Numero fuera de rango")

        elif s=="SS":

            if numero>=1 and numero<=59:

                self.segundo=numero1

            else:

                print("Numero fuera de rango")

        
                    

                    



        
        

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)

           