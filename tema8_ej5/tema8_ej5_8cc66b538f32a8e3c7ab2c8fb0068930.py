class FechaHora:
    def __init__(self):
        pass

    def __str__(self):
        return self.fecha + " " + self.hora

    def fijarFecha(self,fecha):
        if "/" in fecha:
            self.fecha=fecha
            fechalist=fecha.split("/")
            self.dd=fechalist[0]
            self.mm=fechalist[1]
            self.aaaa=fechalist[2]
            self.fecha=[]
            self.fecha.append(self.aaaa)
            self.fecha.append(self.mm)
            self.fecha.append(self.dd)
            self.fecha="/".join(self.fecha)
            
        elif "-" in fecha:
            self.fecha=fecha
            fechalist=fecha.split("-")
            self.dd=fechalist[0]
            self.mm=fechalist[1]
            self.aaaa=fechalist[2]
            self.fecha=[]
            self.fecha.append(self.aaaa)
            self.fecha.append(self.mm)
            self.fecha.append(self.dd)
            self.fecha="/".join(self.fecha)

    def fijarHora(self,hora):
        if ":" in hora:
            self.hora=hora
            horalist=hora.split(":")
            self.HH=horalist[0]
            self.MM=horalist[1]
            self.SS=horalist[2]
            self.hora=[]
            self.hora.append(self.HH)
            self.hora.append(self.MM)
            self.hora.append(self.SS)
            self.hora=":".join(self.hora)

    def fijarFechaHora(self,fechahora):
        if " " in fechahora:
            self.fechahora=fechahora
            fechahoralist=fechahora.split(" ")
            self.fecha=fechahoralist[0]
            self.hora=fechahoralist[1]
            self.fijarFecha(self.fecha)
            self.fijarHora(self.hora)
            

    def cambiar(self,parte):
        if "dd" in parte:
            if " " in parte:
                self.dd=parte[5:]
            else:
                self.dd=parte[3:]
            self.fecha=[]
            self.fecha.append(self.aaaa)
            self.fecha.append(self.mm)
            self.fecha.append(self.dd)
            self.fecha="/".join(self.fecha)
        if "mm" in parte:
            if " " in parte:
                self.mm=parte[5:]
            else:
                self.mm=parte[3:]
            self.fecha=[]
            self.fecha.append(self.aaaa)
            self.fecha.append(self.mm)
            self.fecha.append(self.dd)
            self.fecha="/".join(self.fecha)
        if "aaaa" in parte:
            if " " in parte:
                self.aaaa=parte[7:]
            else:
                self.aaaa=parte[5:]
            self.fecha=[]
            self.fecha.append(self.aaaa)
            self.fecha.append(self.mm)
            self.fecha.append(self.dd)
            self.fecha="/".join(self.fecha)
        if "HH" in parte:
            if " " in parte:
                self.HH=parte[5:]
            else:
                self.HH=parte[3:]
            self.hora=[]
            self.hora.append(self.HH)
            self.hora.append(self.MM)
            self.hora.append(self.SS)
            self.hora="/".join(self.hora)
        if "MM" in parte:
            if " " in parte:
                self.MM=parte[5:]
            else:
                self.MM=parte[3:]
            self.hora=[]
            self.hora.append(self.HH)
            self.hora.append(self.MM)
            self.hora.append(self.SS)
            self.hora="/".join(self.hora)
        if "SS" in parte:
            if " " in parte:
                self.SS=parte[5:]
            else:
                self.SS=parte[3:]
            self.hora=[]
            self.hora.append(self.HH)
            self.hora.append(self.MM)
            self.hora.append(self.SS)
            self.hora="/".join(self.hora)
            

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           