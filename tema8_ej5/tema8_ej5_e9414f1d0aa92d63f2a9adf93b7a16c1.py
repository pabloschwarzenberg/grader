class FechaHora:
    def __init__(self, fecha="", hora=""):
        self.dia = None
        self.mes = None
        self.anio = None
        self.hora = None
        self.minuto = None
        self.segundo = None

        if fecha:
            self.fijarFecha(fecha)
        if hora:
            self.fijarHora(hora)

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
        tipo = partes[0].strip()
        valor = int(partes[1].strip())

        if tipo == "dd":
            if valor < 1 or valor > 31:
                print("Error: Día inválido.")
                return
            self.dia = valor
        elif tipo == "mm":
            if valor < 1 or valor > 12:
                print("Error: Mes inválido.")
                return
            self.mes = valor
        elif tipo == "aaaa":
            self.anio = valor
        elif tipo == "HH":
            if valor < 0 or valor > 23:
                print("Error: Hora inválida.")
                return
            self.hora = valor
        elif tipo == "MM":
            if valor < 0 or valor > 59:
                print("Error: Minuto inválido.")
                return
            self.minuto = valor
        elif tipo == "SS":
            if valor < 0 or valor > 59:
                print("Error: Segundo inválido.")
                return
            self.segundo = valor
        else:
            print("Error: Parámetro inválido.")
            return

        print("Parámetro cambiado con éxito.")

    def __str__(self):
        fecha = f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d}"
        hora = f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
        return f"{fecha} {hora}"


# Ejemplo de uso
if __name__ == "__main__":
    fecha_hora = FechaHora()
    print(fecha_hora)  # Output: 0000/00/00 00:00:00

    fecha_hora.fijarFecha("24/06/2023")
    fecha_hora.fijarHora("15:30:45")
    print(fecha_hora)  # Output: 2023/06/24 15:30:45

    fecha_hora.fijarFechaHora("31/12/2022 23:59:59")
    print(fecha_hora)  # Output: 2022/12/31 23:59:59

    fecha_hora.c
