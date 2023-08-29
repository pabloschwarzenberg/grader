from datetime import datetime

class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 0
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(
            self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo
        )

    def fijarFecha(self, fecha):
        try:
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            try:
                fecha_obj = datetime.strptime(fecha, "%d-%m-%Y")
            except ValueError:
                print("Formato de fecha inválido.")
                return
        self.dia = fecha_obj.day
        self.mes = fecha_obj.month
        self.anio = fecha_obj.year

    def fijarHora(self, hora):
        partes = hora.split(":")
        self.hora = int(partes[0])
        self.minuto = int(partes[1])
        self.segundo = int(partes[2])

    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(" ")
        self.fijarFecha(partes[0])
        self.fijarHora(partes[1])

    def cambiar(self, parametro):
        partes = parametro.split("=")
        if len(partes) != 2:
            print("Formato inválido. Debe ser <parámetro>=<valor>.")
            return
        nombre_parametro = partes[0].strip().lower()
        valor = partes[1].strip()

        if nombre_parametro == "dd":
            dia = int(valor)
            if dia < 1 or dia > 31:
                print("Día inválido.")
                return
            self.dia = dia
        elif nombre_parametro == "mm":
            mes = int(valor)
            if mes < 1 or mes > 12:
                print("Mes inválido.")
                return
            self.mes = mes
        elif nombre_parametro == "aaaa":
            anio = int(valor)
            if anio < 0:
                print("Año inválido.")
                return
            self.anio = anio
        elif nombre_parametro == "hh":
            hora = int(valor)
            if hora < 0 or hora > 23:
                print("Hora inválida.")
                return
            self.hora = hora
        elif nombre_parametro == "mm":
            minuto = int(valor)
            if minuto < 0 or minuto > 59:
                print("Minuto inválido.")
                return
            self.minuto = minuto
        elif nombre_parametro == "ss":
            segundo = int(valor)
            if segundo < 0 or segundo > 59:
                print("Segundo inválido.")
                return
            self.segundo = segundo
        else:
            print("Parámetro inválido.")

if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha("30-09-2015")
    fecha_hora.fijarHora("12:30:45")
    print(fecha_hora)

    fecha_hora.cambiar("dd=2")
    fecha_hora.cambiar("mm=13")
    fecha_hora.cambiar("xyz=abc")
    print(fecha_hora)