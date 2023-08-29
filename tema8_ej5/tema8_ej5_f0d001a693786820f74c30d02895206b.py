class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1900
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def fijarFecha(self, fecha):
        partes = fecha.split("/")
        self.dia = int(partes[0])
        self.mes = int(partes[1])
        self.anio = int(partes[2])

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
        tipo = partes[0].strip()
        valor = int(partes[1].strip())

        if tipo == "dd":
            if 1 <= valor <= 31:
                self.dia = valor
            else:
                print("Error: El día debe estar entre 1 y 31.")
        elif tipo == "mm":
            if 1 <= valor <= 12:
                self.mes = valor
            else:
                print("Error: El mes debe estar entre 1 y 12.")
        elif tipo == "aaaa":
            self.anio = valor
        elif tipo == "HH":
            if 0 <= valor <= 23:
                self.hora = valor
            else:
                print("Error: La hora debe estar entre 0 y 23.")
        elif tipo == "MM":
            if 0 <= valor <= 59:
                self.minuto = valor
            else:
                print("Error: El minuto debe estar entre 0 y 59.")
        elif tipo == "SS":
            if 0 <= valor <= 59:
                self.segundo = valor
            else:
                print("Error: El segundo debe estar entre 0 y 59.")
        else:
            print("Error: Parámetro no válido.")

    def __str__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"


# Ejemplo de uso
fecha_hora = FechaHora()

fecha_hora.fijarFecha("12/05/2023")
fecha_hora.fijarHora("18:30:15")

print(fecha_hora)

fecha_hora.cambiar("dd=25")
fecha_hora.cambiar("mm=15")
fecha_hora.cambiar("aaaa=2022")
fecha_hora.cambiar("HH=8")
fecha_hora.cambiar("MM=45")
fecha_hora.cambiar("SS=70")

print(fecha_hora)