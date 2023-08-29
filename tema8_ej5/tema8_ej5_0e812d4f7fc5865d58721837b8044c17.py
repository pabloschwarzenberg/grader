class FechaHora:
    def __init__(self):
        self.año = 0
        self.mes = 0
        self.dia = 0
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        if self.hora < 10:
            hora = '0' + str(self.hora)
        else:
            hora = str(self.hora)

        if self.minuto < 10:
            minuto = '0' + str(self.minuto)
        else:
            minuto = str(self.minuto)

        if self.segundo < 10:
            segundo = '0' + str(self.segundo)
        else:
            segundo = str(self.segundo)
        
        if self.dia < 10:
            dia = '0' + str(self.dia)
        else:
            dia = str(self.dia)
            
        if self.mes < 10:
            mes = '0' + str(self.mes)
        else:
            mes = str(self.mes)

        return str(self.año) + '/' + mes + '/' + dia + ' ' + hora + ':' + minuto + ':' + segundo

    def fijarFecha(self, fecha):
        if '/' in fecha:
            componentes = fecha.split('/')
        else:
            componentes = fecha.split('-')

        self.dia = int(componentes[0])
        self.mes = int(componentes[1])
        self.año = int(componentes[2])

    def fijarHora(self, hora):
        componentes = hora.split(':')
        self.hora = int(componentes[0])
        self.minuto = int(componentes[1])
        self.segundo = int(componentes[2])

    def fijarFechaHora(self, fechahora):
        separados = fechahora.split(' ')
        separados[0] = separados[0].split('-')
        separados[1] = separados[1].split(':')

        self.dia = int(separados[0][0])
        self.mes = int(separados[0][1])
        self.año = int(separados[0][2])
        self.hora = int(separados[1][0])
        self.minuto = int(separados[1][1])
        self.segundo = int(separados[1][2])

    def cambiar(self, parte):
        parte = parte.split('=')
        parte[0] = parte[0].rstrip()
        parte[1] = parte[1].rstrip()
        if parte[0] == 'dd':
            self.dia = int(parte[1])
        if parte[0] == 'mm':
            self.mes = int(parte[1])
        if parte[0] == 'aaaa':
            self.año = int(parte[1])
        if parte[0] == 'HH':
            self.hora = int(parte[1])
        if parte[0] == 'MM':
            self.minuto = int(parte[1])
        if parte[0] == 'SS':
            self.segundo = int(parte[1])


if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)

