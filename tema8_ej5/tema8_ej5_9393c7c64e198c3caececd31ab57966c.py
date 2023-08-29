class FechaHora:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.anio = 0
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __str__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

    def fijarFecha(self, fecha):
        self.dia, self.mes, self.anio = map(int, fecha.split("/") if "/" in fecha else fecha.split("-"))

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(":"))

    def fijarFechaHora(self, fechahora):
        fecha, hora = fechahora.split(" ")
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parte):
        tipo, valor = parte.split("=")
        tipo = tipo.strip()
        valor = int(valor.strip())

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
            print(f"Error: Tipo de parámetro no válido ({tipo}).")

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)

           