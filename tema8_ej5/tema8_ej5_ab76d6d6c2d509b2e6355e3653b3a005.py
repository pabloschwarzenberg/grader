class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None
    
    def fijarFecha(self, fecha_str):
        partes = fecha_str.replace('/', '-').split('-')
        try:
            dia, mes, anio = map(int, partes)
            if 1 <= dia <= 31 and 1 <= mes <= 12 and anio >= 1:
                self.fecha = (anio, mes, dia)
            else:
                print("Fecha inválida")
        except ValueError:
            print("Formato de fecha inválido")
    
    def fijarHora(self, hora_str):
        partes = hora_str.split(':')
        try:
            hora, minuto, segundo = map(int, partes)
            if 0 <= hora <= 23 and 0 <= minuto <= 59 and 0 <= segundo <= 59:
                self.hora = (hora, minuto, segundo)
            else:
                print("Hora inválida")
        except ValueError:
            print("Formato de hora inválido")
    
    def fijarFechaHora(self, fecha_hora_str):
        partes = fecha_hora_str.split(' ')
        if len(partes) == 2:
            self.fijarFecha(partes[0])
            self.fijarHora(partes[1])
        else:
            print("Formato de fecha y hora inválido")
    
    def cambiar(self, cambio_str):
        tipo, valor = cambio_str.replace(' ', '').split('=')
        
        if tipo == 'dd':
            self.fecha = (self.fecha[0], self.fecha[1], int(valor)) if 1 <= int(valor) <= 31 else self.fecha
        elif tipo == 'mm':
            self.fecha = (self.fecha[0], int(valor), self.fecha[2]) if 1 <= int(valor) <= 12 else self.fecha
        elif tipo == 'aaaa':
            self.fecha = (int(valor), self.fecha[1], self.fecha[2]) if int(valor) >= 1 else self.fecha
        elif tipo == 'HH':
            self.hora = (int(valor), self.hora[1], self.hora[2]) if 0 <= int(valor) <= 23 else self.hora
        elif tipo == 'MM':
            self.hora = (self.hora[0], int(valor), self.hora[2]) if 0 <= int(valor) <= 59 else self.hora
        elif tipo == 'SS':
            self.hora = (self.hora[0], self.hora[1], int(valor)) if 0 <= int(valor) <= 59 else self.hora
        else:
            print("Tipo de parámetro inválido")
    
    def __str__(self):
        fecha_str = "{:04d}/{:02d}/{:02d}".format(*self.fecha) if self.fecha is not None else "Sin fecha"
        hora_str = "{:02d}:{:02d}:{:02d}".format(*self.hora) if self.hora is not None else "Sin hora"
        return fecha_str + ' ' + hora_str
