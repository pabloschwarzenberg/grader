class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""

    def fijarFecha(self, fecha):
        # Validar el formato de fecha dd/mm/aaaa o dd-mm-aaaa
        if "/" in fecha:
            separador = "/"
        elif "-" in fecha:
            separador = "-"
        else:
            raise ValueError("Formato de fecha inválido. Utilice dd/mm/aaaa o dd-mm-aaaa")

        # Separar día, mes y año
        dia, mes, anio = fecha.split(separador)

        # Validar día, mes y año
        if not (1 <= int(dia) <= 31):
            raise ValueError("Día inválido")
        if not (1 <= int(mes) <= 12):
            raise ValueError("Mes inválido")
        if not (1 <= int(anio)):
            raise ValueError("Año inválido")

        self.fecha = f"{anio}/{mes}/{dia}"

    def fijarHora(self, hora):
        # Validar el formato de hora HH:MM:SS
        if ":" not in hora:
            raise ValueError("Formato de hora inválido. Utilice HH:MM:SS")

        # Separar horas, minutos y segundos
        horas, minutos, segundos = hora.split(":")

        # Validar horas, minutos y segundos
        if not (0 <= int(horas) < 24):
            raise ValueError("Hora inválida")
        if not (0 <= int(minutos) < 60):
            raise ValueError("Minuto inválido")
        if not (0 <= int(segundos) < 60):
            raise ValueError("Segundo inválido")

        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        # Validar el formato de fecha y hora dd/mm/aaaa HH:MM:SS
        if " " not in fecha_hora:
            raise ValueError("Formato de fecha y hora inválido. Utilice dd/mm/aaaa HH:MM:SS")

        fecha, hora = fecha_hora.split(" ")
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        # Validar el formato del parámetro
        if "=" not in parametro:
            raise ValueError("Formato de parámetro inválido. Utilice 'dd=valor', 'mm=valor', 'aaaa=valor', 'HH=valor', 'MM=valor' o 'SS=valor'")

        # Separar el nombre del parámetro y su valor
        nombre, valor = parametro.split("=")

        # Validar y cambiar el parámetro correspondiente
        if nombre == "dd":
            if not (1 <= int(valor) <= 31):
                raise ValueError("Día inválido")
            self.fecha = self.fecha[:8] + valor + self.fecha[10:]
        elif nombre == "mm":
            if not (1 <= int(valor) <= 12):
                raise ValueError("Mes inválido")
            self.fecha = self.fecha[:5] + valor + self.fecha[7:]
        elif nombre == "aaaa":
            if not (1 <= int(valor)):
                raise ValueError("Año inválido")
            self.fecha = valor + self.fecha[4:]
        elif nombre == "HH":
            if not (0 <= int(valor) < 24):
                raise ValueError("Hora inválida")
            self.hora = valor + self.hora[2:]
        elif nombre == "MM":
            if not (0 <= int(valor) < 60):
                raise ValueError("Minuto inválido")
            self.hora = self.hora[:3] + valor + self.hora[5:]
        elif nombre == "SS":
            if not (0 <= int(valor) < 60):
                raise ValueError("Segundo inválido")
            self.hora = self.hora[:6] + valor
        else:
            raise ValueError("Parámetro inválido")

    def __repr__(self):
        return f"{self.fecha} {self.hora}"

    def __str__(self):
        return f"{self.fecha} {self.hora}"


if __name__ == "__main__":
    fecha_hora = FechaHora()
    fecha_hora.fijarFecha("25/06/2023")
    fecha_hora.fijarHora("12:30:45")
    print(fecha_hora)

    fecha_hora.fijarFechaHora("02/08/2024 18:45:00")
    print(fecha_hora)

    fecha_hora.cambiar("dd=30")
    fecha_hora.cambiar("mm=11")
    fecha_hora.cambiar("aaaa=2025")
    fecha_hora.cambiar("HH=08")
    fecha_hora.cambiar("MM=15")
    fecha_hora.cambiar("SS=20")
    print(fecha_hora)
