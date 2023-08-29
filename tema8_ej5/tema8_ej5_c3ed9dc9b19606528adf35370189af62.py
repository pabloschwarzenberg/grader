#clase fecha hora:
class FechaHora:
    def __init__(self):
        self.fecha=""
        self.hora=""
        
    def __str__(self):
        return self.fecha+" "+self.hora
    
    def fijarFecha(self,fecha):
        f=[]
        dato=""
        i=0
        while i<len(fecha):
          a=fecha[i]
          if a!="/" and a!="-":
            dato+=a
          if a=="/" or a=="-":
            f.append(dato)
            dato=""       
          if i==len(fecha)-1:
            f.append(dato)
            dato=""
          i+=1
        fecha="{}/{}/{}".format(f[2],f[1],f[0])
        self.fecha=fecha
        
    def fijarHora(self,hora):
        h=[]
        parametro=""
        i=0
        while i<len(hora):
            a=hora[i]
            if a!=":":
              parametro+=a
            if a==":":
              h.append(parametro)
              parametro=""
            if i==len(hora)-1:
              h.append(parametro)
            i+=1
        hora="{}:{}:{}".format(h[0],h[1],h[2])
        self.hora=hora

    def fijarFechaHora(self,fechahora):
        parametro=""
        datos=[]
        i=0
        while i<len(fechahora):
            a=fechahora[i]
            if a!=" ":
                parametro+=a
            if a==" ":
                datos.append(parametro)
                parametro=""
            if i==len(fechahora)-1:
                datos.append(parametro)
                parametro=""
            i+=1
        fecha=datos[0]
        hora=datos[1]
        self.fijarFecha(fecha)
        self.fijarHora(hora)
        return FechaHora()
        
    def cambiar(self,parte):
        i=0
        cambios=[]
        dato=""
        while i<len(parte):
            a=parte[i]
            if a!="=":
                dato+=a
            if a=="=":
                cambios.append(dato)
                dato=""
            if i==len(parte)-1:
                cambios.append(dato)
            i+=1
       
        if cambios[0]=="aaaa ":
            i=0
            fecha=[]
            dato=""
            while i<len(self.fecha):
                a=self.fecha[i]
                if a!="/":
                    dato+=a
                if a=="/":
                    fecha.extend([dato])
                    dato=""
                if i==len(self.fecha)-1:
                    fecha.extend([dato])
                i+=1
            a=list(cambios[1])
            a.pop(0)
            a="".join(a)
            fecha[0]=a
            fecha="/".join(fecha)
            self.fecha=fecha
        if cambios[0]=="mm":
            i=0
            fecha=[]
            dato=""
            while i<len(self.fecha):
                a=self.fecha[i]
                if a!="/":
                    dato+=a
                if a=="/":
                    fecha.extend([dato])
                    dato=""
                if i==len(self.fecha)-1:
                    fecha.extend([dato])
                i+=1
            fecha[1]=cambios[1]
            fecha="/".join(fecha)
            self.fecha=fecha

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)