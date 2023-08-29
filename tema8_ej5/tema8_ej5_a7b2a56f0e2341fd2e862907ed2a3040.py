class FechaHora:
    def __init__(self):
        self.fecha=''
        self.hora=''

    def __str__(self):
       fecha1=self.fecha.split('-')
       fecha2=str(fecha1[-1])+'/'+str(fecha1[-2])+'/'+str(fecha1[-3])
       return str(fecha2)+" "+str(self.hora)


    def fijarFecha(self,fecha):
        fc=fecha.split("-")
        
        if (int(fc[1])==(1) or (3) or (5) or (7) or (8) or (10) or (12) and 0<int(fc[0])<=31) or (int(fc[1])==(4) or (6) or (9) or (11) and 0<int(fc[0])<=30) or (int(fc[1])==(2) and 0<int(fc[0])<=28):
           self.fecha=fecha 
        else:
          return('error')

    def fijarHora(self,hora):
        hr=hora.split(":")
        if 0<=int(hr[0])<24 and 0<=int(hr[1])<60 and 0<=int(hr[2])<60:
          self.hora=hora
        else:
          return('error')

    def fijarFechaHora(self,fechahora):
        fh=fechahora.split(" ")
        fc=str(fh[0]).split("-")
        print(fc)
        print(int(fc[1]))
        if (int(fc[1])==(1) or (3) or (5) or (7) or (8) or (10) or (12) and 0<int(fc[0])<=31) or (int(fc[1])==(4) or (6) or (9) or (11) and 0<int(fc[0])<=30) or (int(fc[1])==(2) and 0<int(fc[0])<=28):
          self.fecha=str(fh[0])
        else:
          return('error')
        hr=str(fh[1]).split(":")
        print(hr)
        if 0<=int(hr[0])<24 and 0<=int(hr[1])<60 and 0<=int(hr[2])<60:
          self.hora=str(fh[1])
        else:
          return('error')
      

    def cambiar(self,parte):
        p=parte.strip()
        part=p.split("=")
        if part[0]=='dd':
          fc=self.fecha.strip("-")
          if (int(fc[1])==(1) or (3) or (5) or (7) or (8) or (10) or (12) and 0<int(part[1])<=31) or (int(fc[1])==(4) or (6) or (9) or (11) and 0<int(part[1])<=30) or (int(fc[1])==(2) and 0<int(part[1])<=28):    
            self.fecha=(str(part[1])+"-"+str(fc[1])+"-"+str(fc[2]))
          else:
            print('error')
        elif part[0]=='mm':
          fc=self.fecha.split("-")
          if (int(part[1])==(1) or (3) or (5) or (7) or (8) or (10) or (12) and 0<int(fc[0])<=31) or (int(part[1])==(4) or (6) or (9) or (11) and 0<int(fc[0])<=30) or (int(part[1])==(2) and 0<int(fc[0])<=28):
            self.fecha=(str(fc[0])+"-"+str(part[1])+"-"+str(fc[2]))
          else:
            print('error')
        elif part[0]=='aaaa ':
           fc=self.fecha.split("-")
           self.fecha=(str(fc[0])+"-"+str(fc[1])+"-"+str(part[1]).strip())
        elif part[0]=='HH':
           hr=hora.split(":")
           if 0<=int(part[1])<24:
            self.hora=(str(part[1])+':'+str(hr[1])+':'+str(hr[2]))
           else:
             print('error')
             
        elif part[0]=='MM':
           hr=hora.split(":")
           if 0<=int(part[1])<60:
            self.hora=(str(hr[0])+':'+str(part[1])+':'+str(hr[2]))
           else:
             print('error')
        elif part[0]=='SS':
           hr=hora.split(":")
           if 0<=int(part[1])<60:
            self.hora=(str(hr[0])+':'+str(hr[1])+':'+str(part[1]))
           else:
             print('error')     
             
           
           
if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
           