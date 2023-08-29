class FechaHora:
    def __init__(self):
        self.año=""
        self.mes=""
        self.dia=""        
        self.hora=""
        self.min=""
        self.seg=""

    def __str__(self):
        fecha_fomato=self.año+"/"+self.mes+"/"+self.dia+" "+self.hora+":"+self.min+":"+self.seg
        return fecha_fomato

    def fijarFecha(self,fecha):
        dia=fecha[0:2]
        mes=fecha[3:5]
        año=fecha[6:]
        self.dia=dia
        self.mes=mes
        self.año=año

    def fijarHora(self,hora):
        hr=hora[0:2]
        mins=hora[3:5]
        seg=hora[6:]
        self.hora=hr
        self.min=mins
        self.seg=seg

    def fijarFechaHora(self,fechahora):
        dia=fechahora[0:2]
        mes=fechahora[3:5]
        año=fechahora[6:10]
        hr=fechahora[11:13]
        mins=fechahora[14:16]
        seg=fechahora[17:]
        self.dia=dia
        self.mes=mes
        self.año=año
        self.hora=hr
        self.min=mins
        self.seg=seg        

    def cambiar(self,cambio):
        if "aaaa" in cambio:
            cambio=list(cambio)
            while " " in cambio:
                cambio.remove(" ")
            cambio=("").join(cambio)
            año_cambio=cambio[5:]
            if int(año_cambio)<0:
                mensaje="cambio invalido"
                return mensaje
            else:
                self.año=año_cambio
        elif "mm" in cambio:
            cambio=list(cambio)
            while " " in cambio:
                cambio.remove(" ")
            cambio=("").join(cambio)
            mes_cambio=cambio[3:]
            if int(mes_cambio)<0 or int(mes_cambio)>12:
                mensaje="cambio invalido"
                return mensaje
            else:
                self.mes=mes_cambio
        elif "dd" in cambio:
            cambio=list(cambio)
            while " " in cambio:
                cambio.remove(" ")
            cambio=("").join(cambio)
            dia_cambio=cambio[3:]
            if int(dia_cambio)<0 or int(dia_cambio)>31:
                mensaje="cambio invalido"
                return mensaje
            else:
                self.dia=dia_cambio
        elif "HH" in cambio:
            cambio=list(cambio)
            while " " in cambio:
                cambio.remove(" ")
            cambio=("").join(cambio)
            hr_cambio=cambio[3:]
            if int(hr_cambio)<0 or int(hr_cambio)>24:
                mensaje="cambio invalido"
                return mensaje
            else:
                self.hora=hr_cambio
        elif "MM" in cambio:
            cambio=list(cambio)
            while " " in cambio:
                cambio.remove(" ")
            cambio=("").join(cambio)
            mins_cambio=cambio[3:]
            if int(mins_cambio)<0 or int(mins_cambio)>59:
                mensaje="cambio invalido"
                return mensaje
            else:
                self.min=mins_cambio
        elif "SS" in cambio:
            cambio=list(cambio)
            while " " in cambio:
                cambio.remove(" ")
            cambio=("").join(cambio)
            seg_cambio=cambio[3:]
            if int(seg_cambio)<0 or int(seg_cambio)>59:
                mensaje="cambio invalido"
                return mensaje
            else:
                self.seg=seg_cambio

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           