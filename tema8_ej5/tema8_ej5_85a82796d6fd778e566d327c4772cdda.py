class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1900
        self.hora = 0
        self.minuto = 0
        self.segundo = 0
    
    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(
            self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo)
    
    def fijarFecha(self, fecha):
        partes = fecha.split('/')
        if len(partes) != 3:
            partes = fecha.split('-')
        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])
    
    def fijarHora(self, hora):
        partes = hora.split(':')
        self.hora = int(partes[0])
        self.minuto = int(partes[1])
        self.segundo = int(partes[2])
    
    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(' ')
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])
    
    def cambiar(self, parametro):
        partes = parametro.split('=')
        if len(partes) == 2:
            tipo_parametro = partes[0].strip()
            valor_parametro = int(partes[1].strip())
            
            if tipo_parametro == 'dd':
                if valor_parametro >= 1 and valor_parametro <= 31:
                    self.dia = valor_parametro
                else:
                    print("Día inválido.")
            elif tipo_parametro == 'mm':
                if valor_parametro >= 1 and valor_parametro <= 12:
                    self.mes = valor_parametro
                else:
                    print("Mes inválido.")
            elif tipo_parametro == 'aaaa':
                if valor_parametro >= 1900 and valor_parametro <= 9999:
                    self.anio = valor_parametro
                else:
                    print("Año inválido.")
            elif tipo_parametro == 'HH':
                if valor_parametro >= 0 and valor_parametro <= 23:
                    self.hora = valor_parametro
                else:
                    print("Hora inválida.")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
           