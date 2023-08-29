class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1900
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def fijarFecha(self, fecha):
        if "/" in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split("/"))
        elif "-" in fecha:
            self.dia, self.mes, self.anio = map(int, fecha.split("-"))

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(":"))

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(" ")
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        parametro = parametro.replace(" ", "")
        if "=" in parametro:
            clave, valor = parametro.split("=")
            if clave == "dd":
                if 1 <= int(valor) <= 31:
                    self.dia = int(valor)
                else:
                    print("Error: Valor de día inválido.")
            elif clave == "mm":
                if 1 <= int(valor) <= 12:
                    self.mes = int(valor)
                else:
                    print("Error: Valor de mes inválido.")
            elif clave == "aaaa":
                if int(valor) >= 1900:
                    self.anio = int(valor)
                else:
                    print("Error: Valor de año inválido.")
            elif clave == "HH":
                if 0 <= int(valor) <= 23:
                    self.hora = int(valor)
                else:
                    print("Error: Valor de hora inválido.")
            elif clave == "MM":
                if 0 <= int(valor) <= 59:
                    self.minuto = int(valor)
                else:
                    print("Error: Valor de minuto inválido.")
            elif clave == "SS":
                if 0 <= int(valor) <= 59:
                    self.segundo = int(valor)
                else:
                    print("Error: Valor de segundo inválido.")
            else:
                print("Error: Parámetro desconocido.")
        else:
            print("Error: Formato de parámetro incorrecto.")

    def __repr__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"


# Ejemplo de uso
fecha_hora = FechaHora()
fecha_hora.fijarFecha("01/01/2023")
fecha_hora.fijarHora("12:30:00")
print(fecha_hora)  # Salida: 2023/01/01 12:30:00

fecha_hora.fijarFechaHora("02-02-2024 10:15:30")
print(fecha_hora)  # Salida: 2024/02/02 10:15:30

fecha_hora.cambiar("dd=30")
fecha_hora.cambiar("mm=13")  # Salida: Error: Valor de mes inválido.
fecha_hora.cambiar("aaaa=2022")
fecha_hora.cambiar("HH=