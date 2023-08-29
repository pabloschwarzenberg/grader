class FechaHora:
    def __init__(self, fecha=None, hora=None):
        self.fecha = None
        self.hora = None
        if fecha:
            self.fijarFecha(fecha)
        if hora:
            self.fijarHora(hora)

    def fijarFecha(self, fecha_str):
        
        if "/" in fecha_str:
            separador = "/"
        elif "-" in fecha_str:
            separador = "-"
        else:
            raise ValueError("Formato de fecha incorrecto. Utilice dd/mm/aaaa o dd-mm-aaaa.")

        
        dia, mes, anio = fecha_str.split(separador)

        
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)

        if dia < 1 or dia > 31:
            raise ValueError("Día inválido.")
        if mes < 1 or mes > 12:
            raise ValueError("Mes inválido.")
        if anio < 0 or anio > 9999:
            raise ValueError("Año inválido.")

        self.fecha = (dia, mes, anio)

    def fijarHora(self, hora_str):
        
        if ":" not in hora_str:
            raise ValueError("Formato de hora incorrecto. Utilice HH:MM:SS.")

        
        horas, minutos, segundos = hora_str.split(":")

        
        horas = int(horas)
        minutos = int(minutos)
        segundos = int(segundos)

        if horas < 0 or horas > 23:
            raise ValueError("Hora inválida.")
        if minutos < 0 or minutos > 59:
            raise ValueError("Minuto inválido.")
        if segundos < 0 or segundos > 59:
            raise ValueError("Segundo inválido.")

        self.hora = (horas, minutos, segundos)

    def fijarFechaHora(self, fecha_hora_str):
        
        fecha_str, hora_str = fecha_hora_str.split()

        
        self.fijarFecha(fecha_str)
        self.fijarHora(hora_str)

    def cambiar(self, parametro):
        
        tipo, valor = parametro.split("=")
        tipo = tipo.strip()
        valor = valor.strip()

        
        if tipo == "dd":
            dia = int(valor)
            if dia < 1 or dia > 31:
                print("Día inválido.")
            else:
                self.fecha = (dia, self.fecha[1], self.fecha[2])
        elif tipo == "mm":
            mes = int(valor)
            if mes < 1 or mes > 12:
                print("Mes inválido.")
            else:
                self.fecha = (self.fecha[0], mes, self.fecha[2])
        elif tipo == "aaaa":
            anio = int(valor)
            if anio < 0 or anio > 9999:
                print("Año inválido.")
            else:
                self.fecha = (self.fecha[0], self.fecha[1], anio)
        elif tipo == "HH":
            horas = int(valor)
            if horas < 0 or horas > 23:
                print("Hora inválida.")
            else:
                self.hora = (horas, self.hora[1], self.hora[2])
        elif tipo == "MM":
            minutos = int(valor)
            if minutos < 0 or minutos > 59:
                print("Minuto inválido.")
            else:
                self.hora = (self.hora[0], minutos, self.hora[2])
        elif tipo == "SS":
            segundos = int(valor)
            if segundos < 0 or segundos > 59:
                print("Segundo inválido.")
            else:
                self.hora = (self.hora[0], self.hora[1], segundos)
        else:
            print("Tipo de parámetro inválido.")

    def __str__(self):
        fecha_str = "{:04d}/{:02d}/{:02d}".format(self.fecha[2], self.fecha[1], self.fecha[0])
        hora_str = "{:02d}:{:02d}:{:02d}".format(self.hora[0], self.hora[1], self.hora[2])
        return fecha_str + " " + hora_str



fecha_hora = FechaHora()
fecha_hora.fijarFecha("05/06/2023")
fecha_hora.fijarHora("10:30:45")
fecha_hora.cambiar("dd=2")
fecha_hora.cambiar("mm=4")
fecha_hora.cambiar("aaaa=2022")
fecha_hora.cambiar("HH=23")
fecha_hora.cambiar("MM=59")
fecha_hora.cambiar("SS=30")
print(fecha_hora)
    


           