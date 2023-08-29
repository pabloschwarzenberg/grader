class FechaHora:
    def __init__(self):
        self.dia = 1
        self.mes = 1
        self.anio = 1900
        self.hora = 0
        self.minutos = 0
        self.segundos = 0

    def fijarFecha(self, fecha):
        partes = fecha.split("/")
        if len(partes) == 3:
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])
            print("Fecha fijada correctamente.")
        else:
            print("Formato de fecha inválido.")

    def fijarHora(self, hora):
        partes = hora.split(":")
        if len(partes) == 3:
            self.hora = int(partes[0])
            self.minutos = int(partes[1])
            self.segundos = int(partes[2])
            print("Hora fijada correctamente.")
        else:
            print("Formato de hora inválido.")

    def fijarFechaHora(self, fecha_hora):
        partes = fecha_hora.split(" ")
        if len(partes) == 2:
            self.fijarFecha(partes[0])
            self.fijarHora(partes[1])
            print("Fecha y hora fijadas correctamente.")
        else:
            print("Formato de fecha y hora inválido.")

    def cambiar(self, parametro):
        partes = parametro.split("=")
        if len(partes) == 2:
            tipo = partes[0].strip()
            valor = partes[1].strip()

            if tipo == "dd":
                nuevo_dia = int(valor)
                if nuevo_dia >= 1 and nuevo_dia <= 31:
                    self.dia = nuevo_dia
                    print("Día cambiado correctamente.")
                else:
                    print("Día inválido.")

            elif tipo == "mm":
                nuevo_mes = int(valor)
                if nuevo_mes >= 1 and nuevo_mes <= 12:
                    self.mes = nuevo_mes
                    print("Mes cambiado correctamente.")
                else:
                    print("Mes inválido.")

            elif tipo == "aaaa":
                nuevo_anio = int(valor)
                if nuevo_anio >= 1900:
                    self.anio = nuevo_anio
                    print("Año cambiado correctamente.")
                else:
                    print("Año inválido.")

            elif tipo == "HH":
                nueva_hora = int(valor)
                if nueva_hora >= 0 and nueva_hora <= 23:
                    self.hora = nueva_hora
                    print("Hora cambiada correctamente.")
                else:
                    print("Hora inválida.")

            elif tipo == "MM":
                nuevos_minutos = int(valor)
                if nuevos_minutos >= 0 and nuevos_minutos <= 59:
                    self.minutos = nuevos_minutos
                    print("Minutos cambiados correctamente.")
                else:
                    print("Minutos inválidos.")

            elif tipo == "SS":
                nuevos_segundos = int(valor)
                if nuevos_segundos >= 0 and nuevos_segundos <= 59:
                    self.segundos = nuevos_segundos
                    print("Segundos cambiados correctamente.")
                else:
                    print("Segundos inválidos.")

            else:
                print("Parámetro inválido.")
        else:
            print("Formato de parámetro inválido.")

    def __repr__(self):
        return "{self.anio}/{self.mes}/{self.dia} {self.hora}:{self.minutos}:{self.segundos}"


# Ejemplo de uso
fecha_hora = FechaHora()
fecha_hora.fijarFecha("30/09/2015")
fecha_hora.fijarHora("17:45:00")
print(fecha_hora)  # Resultado esperado: 2015/09/30 17:45:00

fecha_hora.cambiar("mm=10")
print(fecha_hora)  # Resultado esperado: 2015/10/30 17:45:00

fecha_hora.fijarHora("18:00:00")
fecha_hora.cambiar("aaaa=2016")
print(fecha_hora)  # Resultado esperado: 2016/10/30 18:00:00
