class FechaHora:
    def fijarFecha(self, fecha):
        self.fecha = fecha
        fecha = fecha.split("/")
        fecha = input("Ingrese la fecha: ")
        self.dia = int(fecha[0])
        self.mes = int(fecha[1])
        self.anio = int(fecha[2])
        print("Fecha: ", self.dia, "/", self.mes, "/", self.anio)
    def fijarHora(self, hora):
        self.hora = hora
        hora = hora.split(":")
        hora = input("Ingrese la hora: ")
        self.hora = int(hora[0])
        self.minutos = int(hora[1])
        self.segundos = int(hora[2])
        print("Hora: ", self.hora, ":", self.minutos, ":", self.segundos)
    def fijarFechaHora(self, fecha, hora):
        self.fecha = fecha
        self.hora = hora
        fecha = fecha.split("/")
        fecha = input("Ingrese la fecha: ")
        self.dia = int(fecha[0])
        self.mes = int(fecha[1])
        self.anio = int(fecha[2])
        hora = hora.split(":")
        hora = input("Ingrese la hora: ")
        self.hora = int(hora[0])
        self.minutos = int(hora[1])
        self.segundos = int(hora[2])
        print("Fecha y hora: ", self.dia, "/", self.mes, "/", self.anio, " ", self.hora, ":", self.minutos, ":", self.segundos)
    def cambiar(self, fecha, hora):
        self.fecha = fecha
        self.hora = hora
        fecha = fecha.split("/")
        fecha = input("Ingrese la fecha: ")
        self.dia = int(fecha[0])
        self.mes = int(fecha[1])
        self.anio = int(fecha[2])
        hora = hora.split(":")
        hora = input("Ingrese la hora: ")
        self.hora = int(hora[0])
        self.minutos = int(hora[1])
        self.segundos = int(hora[2])
        print("Fecha y hora: ", self.dia, "/", self.mes, "/", self.anio, " ", self.hora, ":", self.minutos, ":", self.segundos)
    def __str__(self):
        return "%02d/%02d/%02d %02d:%02d:%02d" % (self.dia, self.mes, self.anio, self.hora, self.minutos, self.segundos)
