class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 2000
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def fijarFecha(self, fecha):
        partes = fecha.split("/")
        if len(partes) != 3:
            partes = fecha.split("-")
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
        clave = partes[0].strip()
        valor = partes[1].strip()

        if clave == "dd":
            nuevo_dia = int(valor)
            if nuevo_dia < 1 or nuevo_dia > 31:
                print("Error: El día ingresado es inválido.")
            else:
                self.dia = nuevo_dia
        elif clave == "mm":
            nuevo_mes = int(valor)
            if nuevo_mes < 1 or nuevo_mes > 12:
                print("Error: El mes ingresado es inválido.")
            else:
                self.mes = nuevo_mes
        elif clave == "aaaa":
            nuevo_anio = int(valor)
            if nuevo_anio < 1:
                print("Error: El año ingresado es inválido.")
            else:
                self.anio = nuevo_anio
        elif clave == "HH":
            nueva_hora = int(valor)
            if nueva_hora < 0 or nueva_hora > 23:
                print("Error: La hora ingresada es inválida.")
            else:
                self.hora = nueva_hora
        elif clave == "MM":
            nuevo_minuto = int(valor)
            if nuevo_minuto < 0 or nuevo_minuto > 59:
                print("Error: El minuto ingresado es inválido.")
            else:
                self.minuto = nuevo_minuto
        elif clave == "SS":
            nuevo_segundo = int(valor)
            if nuevo_segundo < 0 or nuevo_segundo > 59:
                print("Error: El segundo ingresado es inválido.")
            else:
                self.segundo = nuevo_segundo
        else:
            print("Error: Parámetro inválido.")

    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(
            self.anio, self.mes, self.dia, self.hora, self.minuto, self.segundo
        )


# Ejemplo de uso
if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha("10/06/2023")
    fecha_hora.fijarHora("15:30:45")

    print(fecha_hora)

    fecha_hora.cambiar("dd=20")
    fecha_hora.cambiar("mm=15")
    fecha_hora.cambiar("aaaa=2024")
    fecha_hora.cambiar("HH=12")
    fecha_hora.cambiar("MM=45")
    fecha_hora.cambiar("SS=30")

    print(fecha_hora)
