class FechaHora:
    def __init__(self):
        self.dia = None
        self.mes = None
        self.anio = None
        self.hora = None
        self.minuto = None
        self.segundo = None

    def fijarFecha(self, fecha):
        self.dia, self.mes, self.anio = fecha.split("/")

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = hora.split(":")

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        tipo, valor = parametro.split("=")

        if tipo == "dd":
            if int(valor) < 1 or int(valor) > 31:
                print("Día inválido")
            else:
                self.dia = valor
        elif tipo == "mm":
            if int(valor) < 1 or int(valor) > 12:
                print("Mes inválido")
            else:
                self.mes = valor
        elif tipo == "aaaa":
            self.anio = valor
        elif tipo == "HH":
            if int(valor) < 0 or int(valor) > 23:
                print("Hora inválida")
            else:
                self.hora = valor
        elif tipo == "MM":
            if int(valor) < 0 or int(valor) > 59:
                print("Minuto inválido")
            else:
                self.minuto = valor
        elif tipo == "SS":
            if int(valor) < 0 or int(valor) > 59:
                print("Segundo inválido")
            else:
                self.segundo = valor
        else:
            print("Parámetro inválido")

    def __str__(self):
        fecha = "{}/{}/{}".format(self.anio, self.mes, self.dia)
        hora = "{}:{}:{}".format(self.hora, self.minuto, self.segundo)
        return "{} {}".format(fecha, hora)
