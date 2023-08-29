class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 2000
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(
            self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo
        )

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

    def fijarFechaHora(self, fechahora):
        partes = fechahora.split(' ')
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parte):
        clave, valor = parte.split('=')
        clave = clave.strip().lower()
        valor = valor.strip()

        if clave == 'dd':
            dia = int(valor)
            if dia < 1 or dia > 31:
                print("Día inválido.")
            else:
                self.dia = dia
        elif clave == 'mm':
            mes = int(valor)
            if mes < 1 or mes > 12:
                print("Mes inválido.")
            else:
                self.mes = mes
        elif clave == 'aaaa':
            anio = int(valor)
            if anio < 1:
                print("Año inválido.")
            else:
                self.anio = anio
        elif clave == 'hh':
            hora = int(valor)
            if hora < 0 or hora > 23:
                print("Hora inválida.")
            else:
                self.hora = hora
        elif clave == 'min':
            minuto = int(valor)
            if minuto < 0 or minuto > 59:
                print("Minuto inválido.")
            else:
                self.minuto = minuto
        elif clave == 'ss':
            segundo = int(valor)
            if segundo < 0 or segundo > 59:
                print("Segundo inválido.")
            else:
                self.segundo = segundo
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
