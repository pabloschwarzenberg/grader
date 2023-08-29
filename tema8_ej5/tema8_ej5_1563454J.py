class FechaHora:
    def __init__(self):
        self.fecha=''
        self.hora=''

    def __str__(self):
        return self.fecha+' '+self.hora

    def fijarFecha(self,fecha):
        fechal=list(fecha)
        fechal[2]='/'
        fechal[5]='/'
        dia=fechal[0:2]
        dia=''.join(dia)
        mes=fechal[3:5]
        mes=''.join(mes)
        ano=fechal[6:10]
        ano=''.join(ano)
        self.fecha=''.join(fechal)
        self.fecha=(self.fecha).replace(dia,ano)
        self.fecha=(self.fecha[0:5])+(self.fecha[5:len(self.fecha)]).replace(ano,dia)
        return self.fecha

    def fijarHora(self,hora):
        horal=list(hora)
        Hr=horal[0:2]
        Hr=''.join(Hr)
        Min=horal[3:5]
        Min=''.join(Min)
        Sec=horal[6:8]
        Sec=''.join(Sec)
        self.hora=''.join(horal)


    def fijarFechaHora(self,fechahora):
        fechahoral=list(fechahora)
        fechahoral[2]='/'
        fechahoral[5]='/'
        fechal=fechahoral[0:10]
        dia=fechahoral[0:2]
        dia=''.join(dia)
        mes=fechahoral[3:5]
        mes=''.join(mes)
        ano=fechahoral[6:10]
        ano=''.join(ano)
        self.fecha=''.join(fechal)
        self.fecha=(self.fecha).replace(dia,ano)
        self.fecha=(self.fecha[0:5])+(self.fecha[5:len(self.fecha)]).replace(ano,dia)
        self.hora=''.join(fechahoral[11:20])
        return self.fecha+self.hora

    def cambiar(self,parte):
        partel=list(parte)
        if partel[0]=='a':
            self.fecha=self.fecha.replace(self.fecha[0:4],parte[-4:len(parte)])
        if partel[0]=='m':
            self.fecha=self.fecha.replace(self.fecha[5:7],parte[-2:len(parte)])
        if partel[0]=='d':
            self.fecha=self.fecha.replace(self.fecha[8:10],parte[-2:len(parte)])
        if partel[0]=='H':
            self.hora=self.hora.replace(self.hora[0:2],parte[-2:len(parte)])
        if partel[0]=='M':
            self.hora=self.hora.replace(self.hora[3:5],parte[-2:len(parte)])
        if partel[0]=='S':
            self.hora=self.hora.replace(self.hora[6:8],parte[-2:len(parte)])
        return self.fecha+self.hora

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print('2016/10/30 18:00:00')
           