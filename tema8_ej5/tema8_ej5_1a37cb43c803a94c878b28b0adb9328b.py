class FechaHora:
    def __init__(self, fecha=None, hora=None):
        if fecha is not None and hora is not None:
            self.fijarFecha(fecha)
            self.fijarHora(hora)

    def fijarFecha(self, fecha):
        if "/" in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split("/"))
        elif "-" in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split("-"))
        else:
            raise ValueError("Formato de fecha inválido. Use dd/mm/aaaa o dd-mm-aaaa.")

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(":"))

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        tipo, valor = parametro.split("=")
        tipo = tipo.strip().lower()
        valor = valor.strip()

        if tipo == "dd":
            if int(valor) < 1 or int(valor) > 31:
                print("Día inválido.")
            else:
                self.dia = int(valor)
        elif tipo == "mm":
            if int(valor) < 1 or int(valor) > 12:
                print("Mes inválido.")
            else:
                self.mes = int(valor)
        elif tipo == "aaaa":
            if int(valor) < 0:
                print("Año inválido.")
            else:
                self.anio = int(valor)
        elif tipo == "hh":
            if int(valor) < 0 or int(valor) > 23:
                print("Hora inválida.")
            else:
                self.hora = int(valor)
        elif tipo == "mm":
            if int(valor) < 0 or int(valor) > 59:
                print("Minuto inválido.")
            else:
                self.minuto = int(valor)
        elif tipo == "ss":
            if int(valor) < 0 or int(valor) > 59:
                print("Segundo inválido.")
            else:
                self.segundo = int(valor)
        else:
            print("Parámetro inválido.")

    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(
            self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo
        )


if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha("01/01/2023")
    fecha_hora.fijarHora("12:00:00")
    print(fecha_hora)

    fecha_hora.fijarFecha("02/02/2023")
    fecha_hora.fijarHora("13:30:45")
    print(fecha_hora)

    fecha_hora.fijarFechaHora("03/03/2023 14:45:30")
    print(fecha_hora)

    fecha_hora.cambiar("dd=31")
    fecha_hora.cambiar("mm=13")
    fecha_hora.cambiar("aaaa=-2023")
    fecha
