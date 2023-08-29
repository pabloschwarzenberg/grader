class FechaHora:
    def __init__(self, dia=00, mes=00, anio=0000, hora=00, minuto=00, segundo=00):
        self.dia = int(dia)
        self.mes = int(mes)
        self.anio = int(anio)
        self.hora = int(hora)
        self.minuto = int(minuto)
        self.segundo = int(segundo)

    def imprimir_fecha_hora(self):
        print("{}/{}/{} {}:{}:{}".format(self.dia, self.mes, self.anio, self.hora, self.minuto, self.segundo))

    def fijarFecha(self, fecha):
        separador = "/"
        if "-" in fecha:
            separador = "-"
        partes = fecha.split(separador)
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
        fecha = partes[0]
        hora = partes[1]
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self, parametro):
        partes = parametro.replace(" ", "").split("=")
        if len(partes) != 2:
            print("Debe especificar el tipo de parámetro y su valor separados por un igual (=).")
            return

        tipo_parametro = partes[0]
        valor_parametro = partes[1]

        if tipo_parametro == "dd":
            if not valor_parametro.isdigit():
                print("El día debe ser un número entero.")
                return
            dia = int(valor_parametro)
            if dia < 1 or dia > 31:
                print("El día debe estar entre 1 y 31.")
                return
            self.dia = dia

        elif tipo_parametro == "mm":
            if not valor_parametro.isdigit():
                print("El mes debe ser un número entero.")
                return
            mes = int(valor_parametro)
            if mes < 1 or mes > 12:
                print("El mes debe estar entre 1 y 12.")
                return
            self.mes = valor_parametro

        elif tipo_parametro == "aaaa":
            if not valor_parametro.isdigit():
                print("El año debe ser un número entero.")
                return
            anio = int(valor_parametro)
            if anio < 1:
                print("El año debe ser mayor o igual a 1.")
                return
            self.anio = anio

        elif tipo_parametro == "HH":
          if not valor_parametro.isdigit():
              print("La hora debe ser un número entero.")
              return
          hora = int(valor_parametro)
          if hora < 0 or hora > 23:
              print("La hora debe estar entre 0 y 23.")
              return
          self.hora = valor_parametro

        elif tipo_parametro == "MM":
            if not valor_parametro.isdigit():
                print("El minuto debe ser un número entero.")
                return
            minuto = int(valor_parametro)
            if minuto < 0 or minuto > 59:
                print("El minuto debe estar entre 0 y 59.")
                return
            self.minuto = valor_parametro

        elif tipo_parametro == "SS":
            if not valor_parametro.isdigit():
                print("El segundo debe ser un número entero.")
                return
            segundo = int(valor_parametro)
            if segundo < 0 or segundo > 59:
                print("El segundo debe estar entre 0 y 59.")
                return
            self.segundo = valor_parametro

        else:
            print("Tipo de parámetro inválido. Los tipos válidos son: dd, mm, aaaa, HH, MM, SS.")

    def __str__(self):
        fecha_str = "{}/{}/{}".format(self.anio, str(self.mes).zfill(2), self.dia)
        hora_str = "{}:{}:{}".format(str(self.hora).zfill(2), str(self.minuto).zfill(2), str(self.segundo).zfill(2))
        return "{} {}".format(fecha_str, hora_str)