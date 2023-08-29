#Se debe poder cambiar cualquier parámetro (día, hora, etc.) con un método
#cambiar que reciba como argumento un string que especifica el tipo de
#parámetro y su valor, el cual se debe validar. Por ejemplo, si quiero cambiar
#el día a 2, debería usar como parámetro ’dd=2’, sin importar los espacios, y
#deberíaa aparecer un mensaje cuando, por ejemplo, quiera cambiar el día a 40.
#Un objeto de la clase FechaHora se debe poder mostrar mediante print con la
#fecha en formato aaaa/mm/dd HH:MM:SS.
class FechaHora:
    def __init__(self):
        self.fecha=""
        self.hora=""
        self.fechahora= [self.fecha,self.fecha]

    def __str__(self):
        return "{0} {1}".format(self.fechahora[0],self.fechahora[1])

    def fijarFecha(self,fecha):
        if fecha.find("-")!=-1:
            fecha=fecha.split("-")
        elif fecha.find("-")==-1:
            fecha=fecha.split("/")
        self.fechahora[0]=fecha
        a=self.fechahora[0][0]
        self.fechahora[0][0]=self.fechahora[0][2]
        self.fechahora[0][2]=a
        self.fechahora[0]="/".join(self.fechahora[0])

    def fijarHora(self,hora):
        self.fechahora[1]=hora

    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")
        self.fijarFecha(fechahora[0])
        self.fijarHora(fechahora[1])

    def cambiar(self,parte):
##        if parte.find(" ")!=-1:
##            parte=parte.split(" ")
##        elif parte.find(" ")==-1:
        parte = parte.replace(" ","")
        parte=parte.split("=")
        dummy=self.fechahora[0].split("/")
        if "dd" in parte[0]:
            dummy[2]=parte[-1]
        elif "mm" in parte[0] and int(parte[-1]) < 13 and int(parte[-1]) > 0:
            dummy[1]=parte[-1]
        elif "aaaa" in parte[0]:
            dummy[0]=parte[-1]
        self.fechahora[0]=dummy[0]+"/"+dummy[1]+"/"+dummy[2]
        dummy=self.fechahora[1].split(":")
        if "SS" in parte[0]:
            dummy[2]=parte[-1]
        elif "MM" in parte[0]:
            dummy[1]=parte[-1]
        elif "HH" in parte[0]:
            dummy[0]=parte[-1]
        self.fechahora[1]=dummy[0]+":"+dummy[1]+":"+dummy[2]

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)