class FechaHora:
    def __init__(self):
        self.dia=self.mes=self.year=self.hora=self.minuto=self.segundo=''

    def __str__(self):
        return ('/'.join([self.year,self.mes,self.dia]) + ' ' + ':'.join([self.hora,self.minuto,self.segundo]))

    def fijarFecha(self,fecha):
        if fecha.find('/')!=-1:
            lista=fecha.split('/')
        elif fecha.find('-')!=-1:
            lista=fecha.split('-')
        self.dia,self.mes,self.year=lista

    def fijarHora(self,hora):
        lista=hora.split(':')
        self.hora,self.minuto,self.segundo=lista

    def fijarFechaHora(self,param):
        self.dia=param[0:2]
        self.mes=param[3:5]
        self.year=param[6:10]
        self.hora=param[11:13]
        self.minuto=param[14:16]
        self.segundo=param[17:19]
        

    def cambiar(self,parte):
        parte=parte.split('=')
        parte=[i.strip() for i in parte]
        if parte[0]=='dd':
            if int(parte[1])>31:
                print("Error")
            else:
                self.dia=parte[1]
        elif parte[0]=='mm':
            if int(parte[1])>12 or int(parte[1])<1:
                print('Error')
            else:
                self.mes=parte[1]
        
        elif parte[0]=='aaaa':
            self.year=parte[1]
            
        elif parte[0].lower()=='hh':
            if int(parte[1])>23:
                print('Error')
            else:
                self.hora=parte[1]
                
                
        elif parte[0].lower()=='mm':
            if int(parte[1])>59:
                print('Error')
            else:
                self.minuto=parte[1]
                
        elif parte[0].lower()=='ss':
            if int(parte[1])>59:
                print('Error')
            else:
                self.segundo=parte[1]
                
if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           