class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

    def fijarFecha(self, fecha):
        if '/' in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split('/'))
        elif '-' in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split('-'))

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(':'))

    def fijarFechaHora(self, fechahora):
        fecha, hora = fechahora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parte):
        partes = parte.split('=')
        parametro = partes[0].strip()
        valor = int(partes[1].strip())

        if parametro == 'dd':
            if valor >= 1 and valor <= 31:
                self.dia = valor
            else:
                print("Día inválido.")
        elif parametro == 'mm':
            if valor >= 1 and valor <= 12:
                self.mes = valor
            else:
                print("Mes inválido.")
        elif parametro == 'aaaa':
            if valor >= 1:
                self.anio = valor
            else:
                print("Año inválido.")
        elif parametro == 'HH':
            if valor >= 0 and valor <= 23:
                self.hora = valor
            else:
                print("Hora inválida.")
        elif parametro == 'MM':
            if valor >= 0 and valor <= 59:
                self.minuto = valor
            else:
                print("Minuto inválido.")
        elif parametro == 'SS':
            if valor >= 0 and valor <= 59:
                self.segundo = valor
            else:
                print("Segundo inválido.")
        else:
            print("Parámetro inválido.")


if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)
