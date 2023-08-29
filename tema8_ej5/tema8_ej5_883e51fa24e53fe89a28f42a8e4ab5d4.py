class FechaHora:
    def __init__(self, fecha="01/01/1970", hora="00:00:00"):
        self.fijarFechaHora(fecha, hora)

    def fijarFecha(self, fecha):
        self.fecha = fecha.strip()
        self.validarFecha()

    def fijarHora(self, hora):
        self.hora = hora.strip()
        self.validarHora()

    def fijarFechaHora(self, fecha, hora):
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        parametro = parametro.strip()
        tipo, valor = parametro.split('=')
        if tipo == "dd":
            self.fecha = valor + self.fecha[2:]
        elif tipo == "mm":
            self.fecha = self.fecha[:3] + valor + self.fecha[5:]
        elif tipo == "aaaa":
            self.fecha = self.fecha[:6] + valor
        elif tipo == "HH":
            self.hora = valor + self.hora[2:]
        elif tipo == "MM":
            self.hora = self.hora[:3] + valor + self.hora[5:]
        elif tipo == "SS":
            self.hora = self.hora[:6] + valor
        else:
            print("Error: Parámetro inválido")
            return False
        self.validarFecha()
        self.validarHora()

    def __str__(self):
        return f"{self.fecha[6:]}/{self.fecha[3:5]}/{self.fecha[:2]} {self.hora}"

    def validarFecha(self):
        try:
            datetime.datetime.strptime(self.fecha, '%d/%m/%Y')
        except ValueError:
            print("Error: Fecha inválida")
            return False
        return True

    def validarHora(self):
        try:
            datetime.datetime.strptime(self.hora, '%H:%M:%S')
        except ValueError:
            print("Error: Hora inválida")
            return False
        return True
           