class FechaHora:
    def __init__(self):
       return


    def fijarFecha(self,fecha):
        self.dd=fecha[0:2]
        self.mm=fecha[3:5]
        self.aaaa=fecha[6:]
        return 

    def fijarHora(self,hora):
        self.HH=hora[0:2]
        self.MM=hora[3:5]
        self.SS=hora[6:]       
        return

    def fijarFechaHora(self,fechahora):
        
        self.dd=fechahora[0:2]
        self.mm=fechahora[3:5]
        self.aaaa=fechahora[6:10]

        self.HH=fechahora[11:13]
        self.MM=fechahora[14:16]
        self.SS=fechahora[17:]       
        return

    def cambiar(self,parte):
        self.parte=parte.strip().split('=')
        
        self.info=self.parte[0].strip()
        self.info2=self.parte[1].strip()
        
                        
        if self.info=='dd':
            self.dd=self.info2
        elif self.info=='mm':
            self.mm=self.info2
        elif self.info=='aaaa':
            self.aaaa=self.info2        
        elif self.info=='HH':
            self.HH=self.info2
        elif self.info=='MM':
            self.MM=self.info2
        elif self.info=='SS':
            self.SS=self.info2
        return
    
    def __str__(self):
        return self.aaaa+'/'+self.mm+'/'+self.dd+' '+self.HH+':'+self.MM+':'+self.SS

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           