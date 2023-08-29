class FechaHora:
    def __init__(self, fecha, hora):
        self.fijarFecha(fecha)
        self.fijarHora(hora)
    
    def fijarFecha(self, fecha):
        if '/' in fecha:
            self.fecha = fecha.replace('/', '-')
        else:
            self.fecha = fecha
    
    def fijarHora(self, hora):
        self.hora = hora
    
    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(' ')
        self.fijarFecha(fecha)
        self.fijarHora(hora)
    
    def cambiar(self, parametro):
        tipo, valor = parametro.split('=')
        
        if tipo == 'dd':
            if int(valor) > 0 and int(valor) <= 31:
                self.fecha = valor + self.fecha[2:]
            else:
                print("El día ingresado es inválido.")
        elif tipo == 'mm':
            if int(valor) > 0 and int(valor) <= 12:
                self.fecha = self.fecha[:3] + valor + self.fecha[5:]
            else:
                print("El mes ingresado es inválido.")
        elif tipo == 'aaaa':
            if len(valor) == 4:
                self.fecha = self.fecha[:6] + valor
            else:
                print("El año ingresado es inválido.")
        elif tipo == 'HH':
            if int(valor) >= 0 and int(valor) < 24:
                self.hora = valor + self.hora[2:]
            else:
                print("La hora ingresada es inválida.")
        elif tipo == 'MM':
            if int(valor) >= 0 and int(valor) < 60:
                self.hora = self.hora[:3] + valor + self.hora[5:]
            else:
                print("Los minutos ingresados son inválidos.")
        elif tipo == 'SS':
            if int(valor) >= 0 and int(valor) < 60:
                self.hora = self.hora[:6] + valor
            else:
                print("Los segundos ingresados son inválidos.")
        else:
            print("El tipo de parámetro ingresado es inválido.")
    
    def __str__(self):
        return self.fecha + ' ' + self.hora
