class FechaHora:
    def __init__(self):
        self.nichi=1
        self.gatsu=1
        self.toshi=1
        self.ji=0
        self.bun=0
        self.byou=0

    def __str__(self):
        年=str(self.toshi)
        if self.gatsu<10:
            月="0"+str(self.gatsu)
        else:
            月=str(self.gatsu)
        if self.nichi<10:
            日="0"+str(self.nichi)
        else:
            日=str(self.nichi)
        if self.ji<10:
            時="0"+str(self.ji)
        else:
            時=str(self.ji)
        if self.bun<10:
            分="0"+str(self.bun)
        else:
            分=str(self.bun)
        if self.byou<10:
            秒="0"+str(self.byou)
        else:
            秒=str(self.byou)
        
        return 年+"/"+月+"/"+日+" "+時+":"+分+":"+秒

    def fijarFecha(self,fecha):
        if "/" in fecha:
            fecha=fecha.split("/")
        elif "-" in fecha:
            fecha=fecha.split("-")

        dia=int(fecha[0])
        mes=int(fecha[1])
        año=int(fecha[2])

        meses31=[1,3,5,7,8,10,12]
        meses30=[4,6,9,11]
        if año%4==0:
            if año%100==0:
                if año%400==0:
                    if año%2000==0:
                        bisiesto=True
                    else:
                        bisiesto=False
                else:
                    bisiesto=False
            else:
                bisiesto=True
        else:
            bisiesto=False

        if mes in meses30:
            maxd=30
        elif mes in meses31:
            maxd=31
        elif mes==2:
            if bisiesto:
                maxd=29
            else:
                maxd=28

        if 1<=dia<=maxd:
            self.nichi=dia
        else:
            raise ValueError("Esa fecha no existe")

        if 1<=mes<=12:
            self.gatsu=mes
        else:
            raise ValueError("Esa fecha no existe")

        if año>0:
            self.toshi=año
        else:
            raise ValueError("Esa fecha no existe")

    def fijarHora(self,hora):
        hora=hora.split(":")
        hour=int(hora[0])
        minute=int(hora[1])
        second=int(hora[2])
        if 0<=hour<=24:
            self.ji=hour
        else:
            raise ValueError("Esa hora no existe")

        if 0<=minute<=60:
            self.bun=minute
        else:
            raise ValueError("Esa hora no existe")

        if 0<=second<=60:
            self.byou=second
        else:
            raise ValueError("Esa hora no existe")

    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split()
        fecha=fechahora[0]
        hora=fechahora[1]
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self,parte):
        parte=parte.split("=")
        que=parte[0]
        a_que=parte[1]
        if "a" in que:
            parametre=str(self.nichi)+"/"+str(self.gatsu)+"/"+a_que
            self.fijarFecha(parametre)
        elif "m" in que:
            parametre=str(self.nichi)+"/"+a_que+"/"+str(self.toshi)
            self.fijarFecha(parametre)
        elif "d" in que:
            parametre=a_que+"/"+str(self.gatsu)+"/"+str(self.toshi)
            self.fijarFecha(parametre)
        elif "H" in que:
            parametre=a_que+":"+str(self.bun)+":"+str(self.byou)
            self.fijarHora(parametre)
        elif "M" in que:
            parametre=str(self.ji)+":"+a_que+":"+str(self.byou)
            self.fijarHora(parametre)
        elif "S" in que:
            parametre=str(self.ji)+":"+str(self.bun)+":"+a_que
            self.fijarHora(parametre)

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)