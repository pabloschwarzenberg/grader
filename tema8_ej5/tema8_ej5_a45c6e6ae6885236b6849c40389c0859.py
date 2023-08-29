class FechaHora:
    def __init__(self):
        self.fecha_hora=""
        

    def fijarFecha(self,fecha):
        if(fecha[2]=="/"):                          # /, -, 26/11/2022, 26-11-2022
            fecha=fecha.split("/")
        else:                                       #[26,11,2022]
            fecha=fecha.split("-")                  
        self.day=fecha[0]                           
        self.month=fecha[1]
        self.year=fecha[2]
        fecha_hora_aux=self.fecha_hora.split(" ")         # 26/11/2022,12:01:30     => [26/11/2022,12:01:30] =>
        if (len(self.fecha_hora)==0):
            self.fecha_hora=fecha[0]+"/"+fecha[1]+"/"+fecha[2]  
        elif(len(self.fecha_hora)>1 or (fecha_hora_aux[0][2]==":" and len(self.fecha_hora)==1)):
            self.fecha_hora=fecha[0]+"/"+fecha[1]+"/"+fecha[2]+" "+self.fecha_hora          
        else:                                                                           #self.fecha_hora="26/11/2022", self.fecha_hora="26/11/2022 12:01:30"
            self.fecha_hora=fecha[0]+"/"+fecha[1]+"/"+fecha[2]
            
    def fijarHora(self,hour):
        hour=hour.split(":")                    
        self.hrs=hour[0]
        self.mins=hour[1]
        self.secs=hour[2]
        fecha_hora_aux=self.fecha_hora.split(" ")                       #[fecha,hora]              
        if (len(self.fecha_hora)==0):                                   
            self.fecha_hora=hour[0]+":"+hour[1]+":"+hour[2]                             #self.fecha_hora 12:01:22
        elif(len(self.fecha_hora)>1 or (fecha_hora_aux[0][2]=="/" and len(self.fecha_hora)==1)):    # self.fecha_hora=22/01/1999 => 22/01/1999 12:01:22
            self.fecha_hora=self.fecha_hora_aux+" "+hour[0]+":"+hour[1]+":"+hour[2]                 # self.fecha_hora=01:02:09 => 12:01:22
        else:
            self.fecha_hora=hour[0]+":"+hour[1]+":"+hour[2]
        
        
    def fijarFechaHora(self,fechahora):
        fechahora=fechahora.split(" ")        #[26/11/2022,12:01:30]
        fecha=fechahora[0]                    #fecha= 26/11/2022
        hora=fechahora[1]                       #hora= 12:01:30
        fecha=fecha.split("/")                  #   fecha=[26,11,2022]    
        hora=hora.split(":")                    #hora=[12,01,30]
        self.day=fecha[0]                       
        "self.month=fecha[1]"
        self.year=fecha[2]
        self.hrs=hora[0]
        self.mins=hora[1]
        self.secs=hora[2]
        self.fecha_hora=fecha[0]+"/"+fecha[1]+"/"+fecha[2]+" "+hora[0]+":"+hora[1]+":"+hora[2]  
        
    def cambiar(self,cambio):
        cambio=cambio.split("=")                    #dd=3, aaaa=1999, SS=30,  
        formato=cambio[0]                           #[dd,3]         dd=5 => dd=3
        cambiar=cambio[1]                           #
        if(formato=="dd" and int(cambiar)<=31 and int(cambiar)>=1):
            self.day=cambiar
        elif(formato=="mm" and int(cambiar)<=12 and int(cambiar)>0):        
            self.month=cambiar
        elif(formato=="aaaa"):
            self.year=cambiar
        elif(formato=="HH" and int(cambiar)<=24 and int(cambiar)>=0):
            self.hrs=cambiar
        elif(formato=="MM" and int(cambiar)<=60 and int(cambiar)>=0):
            self.mins=cambiar
        elif(formato=="SS" and int(cambiar)<=60 and int(cambiar)>=0):
            self.secs=cambiar
        else:
            print("entrada invalida.")              
        self.fecha_hora=self.day+"/"+self.month+"/"+self.year+" "+self.hrs+":"+self.mins+":"+self.secs    
        
            
if __name__ == "__main__":
   
    calendario1=FechaHora()                    
    calendario1.fijarHora("13:25:30")                   #self.fecha_hora= "13:25:30"
    calendario1.fijarFecha("19-12-2023")                #self.fecha_hora= "19-12-2023" "13:25:30"
    calendario1.fijarFechaHora("19/12/2023 13:22:10")  #self.fecha_hora= "19/12/2023 13:22:10"
    calendario1.cambiar("aaaa=2022")                    #self.fecha_hora= "19/12/2022 13:22:10"
    print(calendario1.fecha_hora)                       