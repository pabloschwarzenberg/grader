class FechaHora:
    def __init__(self, fecha="01/01/1900", hora="00:00:00"):
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def fijarFecha(self, fecha):
        separador = "/" if "/" in fecha else "-"
        self.dia, self.mes, self.anio = map(int, fecha.split(separador))

    def fijarHora(self, hora):
        self.hora, self.minuto, self.segundo = map(int, hora.split(":"))

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split(" ")
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        tipo, valor = parametro.split("=")
        tipo = tipo.strip().lower()
        valor = valor.strip()

        if tipo == "dd":
            dia = int(valor)
            if dia >= 1 and dia <= 31:
                self.dia = dia
            else:
                print("Día inválido")
        elif tipo == "mm":
            mes = int(valor)
            if mes >= 1 and mes <= 12:
                self.mes = mes
            else:
                print("Mes inválido")
        elif tipo == "aaaa":
            anio = int(valor)
            if anio >= 0:
                self.anio = anio
            else:
                print("Año inválido")
        elif tipo == "hh":
            hora = int(valor)
            if hora >= 0 and hora <= 23:
                self.hora = hora
            else:
                print("Hora inválida")
        elif tipo == "min":
            minuto = int(valor)
            if minuto >= 0 and minuto <= 59:
                self.minuto = minuto
            else:
                print("Minuto inválido")
        elif tipo == "ss":
            segundo = int(valor)
            if segundo >= 0 and segundo <= 59:
                self.segundo = segundo
            else:
                print("Segundo inválido")
        else:
            print("Parámetro inválido")

    def __repr__(self):
        return f"{self.anio:04d}/{self.mes:02d}/{self.dia:02d} {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"


# Ejemplo de uso
if __name__ == "__main__":
    fecha_hora = FechaHora()
    print(fecha_hora)

    fecha_hora.fijarFecha("20/06/2023")
    fecha_hora.fijarHora("12:30:45")
    print(fecha_hora)

    fecha_hora.fijarFechaHora("01/01/2000 23:59:59")
    print(fecha_hora)

    fecha_hora.cambiar("dd=30")
    fecha_hora.cambiar("mm=13")
    fecha_hora.cambiar("aaaa=2022")
    fecha_hora.cambiar("hh=25")
    fecha_hora.cambiar("min=61")
    fecha_hora.cambiar("ss=75")
    print(fecha_hora)
