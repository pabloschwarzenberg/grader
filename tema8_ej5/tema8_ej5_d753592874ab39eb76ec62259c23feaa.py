class FechaHora:
    def __init__(self):
        self.dia=0
        self.mes=0
        self.year=0
        self.Horas=0
        self.Min=0
        self.Seg=0
    
    
    def fijarFecha(self, string):
        if "/" in string:
            a=string.split("/")
        if "-" in string:
            a=string.split("-")
        self.dia=a[0]
        self.mes=a[1]
        self.year=a[2]
        

    def __str__(self):
        return "{0}/{1}/{2} {3}:{4}:{5}".format(self.year,self.mes,self.dia,self.Horas,self.Min,self.Seg)

    def fijarHora(self,hora):
        b=hora.split(":")
        self.Horas=b[0]
        self.Min=b[1]
        self.Seg=b[2]     

    def fijarFechaHora(self,fechahora):
        a=fechahora.split(" ")
        Fecha=a[0]
        Fecha=fijarFecha(self, Fecha)
        Hora=a[1]
        Hora=fijarHora(self, Hora)
        

    def cambiar(self,parte):
        for i in range(len(parte)-1):
        a=""
            if parte[i]=="d" and parte[i+1]=="d":
                for j in range(len(parte)):
                    if isdigit(parte[j])==True and (self.mes!=2 or self.mes!="02"): 
                        a+=parte[j]
                    if int(a)<=30:
                        self.dia=a
                    else:
                        print("No se puede realizar acción")
                        
            if parte[i]=="m" and parte[i+1]=="m":
                for j in range(len(parte)):
                    if isdigit(parte[j])==True:
                        a+=parte[j]
                    if int(a)<=12:
                        self.mes=a
                    else:
                        print("No se puede realizar acción")
                        
            if parte[i]=="H" and parte[i+1]=="H":
                for j in range(len(parte)):
                    if isdigit(parte[j])==True: and int(parte[j])<=24:
                        a+=parte[j]
                    if int(a)<=24:
                        self.Horas=a
                    else:
                        print("No se puede realizar acción")
                        
            if parte[i]=="M" and parte[i+1]=="M":
                for j in range(len(parte)):
                    if isdigit(parte[j])==True:
                        a+=parte[j]
                    if int(a)<=60:
                        self.Min=a
                    else:
                        print("No se puede realizar acción")

            if parte[i]=="S" and parte[i+1]=="S":
                for j in range(len(parte)):
                    if isdigit(parte[j])==True:
                        a+=parte[j]
                    if int(a)<=60:
                        self.Seg=a
                    else:
                        print("No se puede realizar acción")
            
            if parte[i]=="M" and parte[i+1]=="M":
                for j in range(len(parte)):
                    if isdigit(parte[j])==True:
                        a+=parte[j]
                    if int(a)<=60:
                        self.dia=a
                    else:
                        print("No se puede realizar acción")

        for i in range(len(parte)-4):
        a=""
            if parte[i]=="a" and parte[i+1]=="a" and parte[i+2]=="a" and parte[i+3]=="a":
                for j in range(len(parte)):
                    if isdigit(parte[j])==True: 
                        a+=parte[j]
                    if len(a)==4:
                        self.dia=a
                    else:
                        print("No se puede realizar acción")
                        

