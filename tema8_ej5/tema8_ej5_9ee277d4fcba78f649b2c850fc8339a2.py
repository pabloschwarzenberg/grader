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
            raise ValueError("Formato de fecha incorrecto. Debe ser dd/mm/aaaa o dd-mm-aaaa")

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(':'))

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        clave, valor = parametro.split('=')
        valor = int(valor)
        if clave == 'dd':
            if valor < 1 or valor > 31:
                raise ValueError("Día inválido. Debe ser un valor entre 1 y 31.")
            self.dia = valor
        elif clave == 'mm':
            if valor < 1 or valor > 12:
                raise ValueError("Mes inválido. Debe ser un valor entre 1 y 12.")
            self.mes = valor
        elif clave == 'aaaa':
            if valor < 1900:
                raise ValueError("Año inválido. Debe ser un valor igual o mayor a 1900.")
            self.anio = valor
        elif clave == 'HH':
            if valor < 0 or valor > 23:
                raise ValueError("Hora inválida. Debe ser un valor entre 0 y 23.")
            self.hora = valor
        elif clave == 'MM':
            if valor < 0 or valor > 59:
                raise ValueError("Minuto inválido. Debe ser un valor entre 0 y 59.")
            self.minuto = valor
        elif clave == 'SS':
            if valor < 0 or valor > 59:
                raise ValueError("Segundo inválido. Debe ser un valor entre 0 y 59.")
            self.segundo = valor
        else:
            raise ValueError("Parámetro inválido.")

    def __repr__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"


if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha("11/06/2023")
    fecha_hora.fijarHora("12:30:45")
    print(fecha_hora)  # 2023/06/11 12:30:45

    fecha_hora.fijarFechaHora("20-02-2022 08:15:30")
    print(fecha_hora)  # 2022/02/20 08:15:30

    fecha_hora.cambiar("dd=25")
    fecha_hora.cambiar("mm=11")
    fecha_hora.cambiar("aaaa=2023")
   
