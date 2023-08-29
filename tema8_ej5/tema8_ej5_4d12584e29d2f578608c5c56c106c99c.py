class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1900
        self.hora = 0
        self.minuto = 0
        self.segundo = 0
    
    def fijarFecha(self, fecha):
        if '/' in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split('/'))
        elif '-' in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split('-'))
        else:
            print("Formato de fecha no válido")
    
    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(':'))
    
    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(' ')
        self.fijarFecha(fecha)
        self.fijarHora(hora)
    
    def cambiar(self, parametro):
        parametro = parametro.replace(' ', '')
        tipo, valor = parametro.split('=')
        valor = int(valor)
        if tipo == 'dd':
            if valor < 1 or valor > 31:
                print("Día inválido")
            else:
                self.dia = valor
        elif tipo == 'mm':
            if valor < 1 or valor > 12:
                print("Mes inválido")
            else:
                self.mes = valor
        elif tipo == 'aaaa':
            if valor < 1900 or valor > 9999:
                print("Año inválido")
            else:
                self.anio = valor
        elif tipo == 'HH':
            if valor < 0 or valor > 23:
                print("Hora inválida")
            else:
                self.hora = valor
        elif tipo == 'MM':
            if valor < 0 or valor > 59:
                print("Minuto inválido")
            else:
                self.minuto = valor
        elif tipo == 'SS':
            if valor < 0 or valor > 59:
                print("Segundo inválido")
            else:
                self.segundo = valor
        else:
            print("Parámetro inválido")
    
    def __str__(self):
        return f"{self.anio}/{self.mes}/{self.dia} {self.hora}:{self.minuto}:{self.segundo}           