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

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(':'))

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(' ')
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        tipo, valor = parametro.split('=')
        if tipo == 'dd':
            if 1 <= int(valor) <= 31:
                self.dia = int(valor)
            else:
                print("Error: El valor del día debe estar entre 1 y 31.")
        elif tipo == 'mm':
            if 1 <= int(valor) <= 12:
                self.mes = int(valor)
            else:
                print("Error: El valor del mes debe estar entre 1 y 12.")
        elif tipo == 'aaaa':
            self.anio = int(valor)
        elif tipo == 'HH':
            if 0 <= int(valor) <= 23:
                self.hora = int(valor)
            else:
                print("Error: El valor de la hora debe estar entre 0 y 23.")
        elif tipo == 'MM':
            if 0 <= int(valor) <= 59:
                self.minuto = int(valor)
            else:
                print("Error: El valor del minuto debe estar entre 0 y 59.")
        elif tipo == 'SS':
            if 0 <= int(valor) <= 59:
                self.segundo = int(valor)
            else:
                print("Error: El valor del segundo debe estar entre 0 y 59.")
        else:
            print("Error: Tipo de parámetro inválido.")

    def __repr__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
