class FechaHora:
    def __init__(self):
        self.dia=""
        self.mes=""
        self.ano=""
        self.hor=""
        self.min=""
        self.seg=""
        self.fechahora=""

    def __str__(self):
        return self.fechahora

    def fijarFecha(self,fecha):
        self.dia=fecha[0:2]
        self.mes=fecha[3:5]
        self.ano=fecha[6:10]
        self.fechahora=self.ano+"/"+self.mes+"/"+self.dia+" "+self.hor+":"+self.min+":"+self.seg
        
    def fijarHora(self,hora):
        self.hor=hora[0:2]
        self.min=hora[3:5]
        self.seg=hora[6:8]
        self.fechahora=self.ano+"/"+self.mes+"/"+self.dia+" "+self.hor+":"+self.min+":"+self.seg

    def fijarFechaHora(self,fechahora):
        self.fechahora=fechahora
        self.dia=self.fechahora[0:2]
        self.mes=self.fechahora[3:5]
        self.ano=self.fechahora[6:10]
        self.hor=self.fechahora[11:13]
        self.min=self.fechahora[14:16]
        self.seg=self.fechahora[17:19]
        self.fechahora=self.ano+"/"+self.mes+"/"+self.dia+" "+self.hor+":"+self.min+":"+self.seg

    

    def cambiar(self,parte):
        cam=parte.replace(" ","").split("=")
        texto=cam[0].lower()

        if(texto=="dd"):
            self.dia=cam[1]
            
        if(texto=="mm"):
            self.mes=cam[1]

        if(texto=="aaaa"):
            self.ano=cam[1]

        if(texto=="hh"):
            self.hor=cam[1]

        if(texto=="min"):
            self.min=cam[1]            

        if(texto=="seg"):
            self.seg=cam[1]
            
        self.fechahora=self.ano+"/"+self.mes+"/"+self.dia+" "+self.hor+":"+self.min+":"+self.seg