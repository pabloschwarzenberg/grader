class FechaHora:
    def __init__(self):
        self.dia = None
        self.mes = None
        self.anio = None
        self.hora = None
        self.minuto = None
        self.segundo = None

    def fijarFecha(self, fecha):
        if "/" in fecha:
            separador = "/"
        elif "-" in fecha:
            separador = "-"
        else:
            print("Formato de fecha inválido. Use el formato dd/mm/aaaa o dd-mm-aaaa")
            return

        partes = fecha.split(separador)
        if len(partes) != 3:
            print("Formato de fecha inválido. Use el formato dd/mm/aaaa o dd-mm-aaaa")
            return

        try:
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])
        except ValueError:
            print("Formato de fecha inválido. Use el formato dd/mm/aaaa o dd-mm-aaaa")
            return

    def fijarHora(self, hora):
        partes = hora.split(":")
        if len(partes) != 3:
            print("Formato de hora inválido. Use el formato HH:MM:SS")
            return

        try:
            self.hora = int(partes[0])
            self.minuto = int(partes[1])
            self.segundo = int(partes[2])
        except ValueError:
            print("Formato de hora inválido. Use el formato HH:MM:SS")
            return

    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(" ")
        if len(partes) != 2:
            print("Formato de fecha y hora inválido. Use el formato dd/mm/aaaa HH:MM:SS")
            return

        fecha = partes[0]
        hora = partes[1]

        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        partes = parametro.split("=")
        if len(partes) != 2:
            print("Formato de parámetro inválido. Use el formato 'nombre=valor'")
            return

        nombre = partes[0].strip()
        valor = partes[1].strip()

        if nombre == "dd":
            try:
                dia = int(valor)
                if dia < 1 or dia > 31:
                    print("Día inválido. Debe ser un valor entre 1 y 31.")
                else:
                    self.dia = dia
            except ValueError:
                print("Valor inválido para el día. Debe ser un número entero.")
        elif nombre == "mm":
            try:
                mes = int(valor)
                if mes < 1 or mes > 12:
                    print("Mes inválido. Debe ser un valor entre 1 y 12.")
                else:
                    self.mes = mes
            except ValueError:
                print("Valor inválido para el mes. Debe ser un número entero.")
        elif nombre == "aaaa":
            try:
                anio = int(valor)
                self.anio = anio
            except ValueError:
                print("Valor inválido para el año. Debe ser un número entero.")
        elif nombre == "HH":
            try:
                hora = int(valor)
                if hora < 0 or hora > 23:
                    print("Hora inválida. Debe ser un valor entre 0 y 23.")
                else:
                    self.hora = hora
            except ValueError:
                print("Valor inválido para la hora. Debe ser un número entero.")
        elif nombre == "MM":
            try:
                minuto = int(valor)
                if minuto < 0 or minuto > 59:
                    print("Minuto inválido. Debe ser un valor entre 0 y 59.")
                else:
                    self.minuto = minuto
            except ValueError:
                print("Valor inválido para el minuto. Debe ser un número entero.")
        elif nombre == "SS":
            try:
                segundo = int(valor)
                if segundo < 0 or segundo > 59:
                    print("Segundo inválido. Debe ser un valor entre 0 y 59.")
                else:
                    self.segundo = segundo
            except ValueError:
                print("Valor inválido para el segundo. Debe ser un número entero.")
        else:
            print("Parámetro desconocido. Los parámetros válidos son: dd, mm, aaaa, HH, MM, SS")

    def __repr__(self):
        return f"{self.anio}/{self.mes}/{self.dia} {self.hora}:{self.minuto}:{self.segundo}"


# Ejemplo de uso
if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha("05/06/2023")
    fecha_hora.fijarHora("18:30:45")
    print(fecha_hora)  # Salida: 2023/6/5 18:30:45

    fecha_hora.fijarFechaHora("10-12-2024 12:15:30")
    print(fecha_hora)  # Salida: 2024/12/10 12:15:30

    fecha_hora.cambiar("dd=25")
    fecha_hora.cambiar("HH=8")
    fecha_hora.cambiar("MM=0")
    fecha_hora.cambiar("SS=0")
    print(fecha_hora)  # Salida: 2024/12/25 8:0:0

    fecha_hora.cambiar("dd=40")  # Salida: Día inválido. Debe ser un valor entre 1 y 31.
    fecha_hora.cambiar("MM=15")  # Salida: Mes inválido. Debe ser un valor entre 1 y 12.
