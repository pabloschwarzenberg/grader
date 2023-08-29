class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def fijarFecha(self, fecha):
        partes = fecha.split("/")
        if len(partes) != 3:
            partes = fecha.split("-")
        if len(partes) == 3:
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])

    def fijarHora(self, hora):
        partes = hora.split(":")
        if len(partes) == 3:
            self.hora = int(partes[0])
            self.minuto = int(partes[1])
            self.segundo = int(partes[2])

    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(" ")
        if len(partes) == 2:
            self.fijarFecha(partes[0])
            self.fijarHora(partes[1])

    def cambiar(self, parametro):
        partes = parametro.split("=")
        if len(partes) == 2:
            tipo = partes[0].strip()
            valor = partes[1].strip()
            if tipo == "dd":
                if valor.isdigit():
                    nuevo_dia = int(valor)
                    if 1 <= nuevo_dia <= 31:
                        self.dia = nuevo_dia
                    else:
                        print("Día inválido")
                else:
                    print("Día inválido")
            elif tipo == "mm":
                if valor.isdigit():
                    nuevo_mes = int(valor)
                    if 1 <= nuevo_mes <= 12:
                        self.mes = nuevo_mes
                    else:
                        print("Mes inválido")
                else:
                    print("Mes inválido")
            elif tipo == "aaaa":
                if valor.isdigit():
                    nuevo_anio = int(valor)
                    if nuevo_anio >= 1:
                        self.anio = nuevo_anio
                    else:
                        print("Año inválido")
                else:
                    print("Año inválido")
            elif tipo == "HH":
                if valor.isdigit():
                    nueva_hora = int(valor)
                    if 0 <= nueva_hora <= 23:
                        self.hora = nueva_hora
                    else:
                        print("Hora inválida")
                else:
                    print("Hora inválida")
            elif tipo == "MM":
                if valor.isdigit():
                    nuevo_minuto = int(valor)
                    if 0 <= nuevo_minuto <= 59:
                        self.minuto = nuevo_minuto
                    else:
                        print("Minuto inválido")
                else:
                    print("Minuto inválido")
            elif tipo == "SS":
                if valor.isdigit():
                    nuevo_segundo = int(valor)
                    if 0 <= nuevo_segundo <= 59:
                        self.segundo = nuevo_segundo
                    else:
                        print("Segundo inválido")
                else:
                    print("Segundo inválido")
            else:
                print("Parámetro inválido")
        else:
            print("Formato de parámetro inválido")

    def __str__(self):
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(
            self.anio, self.mes, self.dia, self.hora,
