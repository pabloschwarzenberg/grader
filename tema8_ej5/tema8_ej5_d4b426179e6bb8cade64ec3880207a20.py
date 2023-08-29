class FechaHora:
    def __init__(self, fecha="01/01/1900", hora="00:00:00"):
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def fijarFecha(self, fecha):
        # Validar formato de fecha
        if "/" in fecha:
            self.dia, self.mes, self.anio = fecha.split("/")
        elif "-" in fecha:
            self.dia, self.mes, self.anio = fecha.split("-")
        else:
            raise ValueError("Formato de fecha inválido. Use dd/mm/aaaa o dd-mm-aaaa.")

    def fijarHora(self, hora):
        # Validar formato de hora
        if ":" in hora:
            self.hora, self.minutos, self.segundos = hora.split(":")
        else:
            raise ValueError("Formato de hora inválido. Use HH:MM:SS.")

    def fijarFechaHora(self, fecha_hora):
        # Separar fecha y hora
        fecha, hora = fecha_hora.split()
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        # Obtener el tipo de parámetro y su valor
        tipo, valor = parametro.split("=")

        # Validar y cambiar el parámetro correspondiente
        if tipo == "dd":
            if int(valor) <= 31:
                self.dia = valor
            else:
                print("Día inválido.")
        elif tipo == "mm":
            if int(valor) <= 12:
                self.mes = valor
            else:
                print("Mes inválido.")
        elif tipo == "aaaa":
            self.anio = valor
        elif tipo == "HH":
            if int(valor) <= 23:
                self.hora = valor
            else:
                print("Hora inválida.")
        elif tipo == "MM":
            if int(valor) <= 59:
                self.minutos = valor
            else:
                print("Minutos inválidos.")
        elif tipo == "SS":
            if int(valor) <= 59:
                self.segundos = valor
            else:
                print("Segundos inválidos.")
        else:
            print("Parámetro inválido.")

    def __repr__(self):
        return f"{self.anio}/{self.mes}/{self.dia} {self.hora}:{self.minutos}:{self.segundos}"


# Ejemplo de uso
fecha_hora = FechaHora()
fecha_hora.fijarFechaHora("12/06/2023 08:30:00")
print(fecha_hora)  # Imprime: 2023/06/12 08:30:00
fecha_hora.cambiar("dd=31")
print(fecha_hora)  # Imprime: 2023/06/31 08:30:00
fecha_hora.cambiar("mm=13")  # Imprime: Mes inválido.
fecha_hora.cambiar("HH=24")  # Imprime: Hora inválida.
fecha_hora.cambiar("SS=70")  # Imprime: Segundos inválidos.
fecha_hora.cambiar("xxxx=valor")  # Imprime: Parámetro inválido.
           