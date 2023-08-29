class FechaHora:
    def __init__(self):
        # Inicializar los atributos de la clase con valores por defecto
        self.dd = 1
        self.mm = 1
        self.aaaa = 2000
        self.HH = 0
        self.MM = 0
        self.SS = 0

    def __str__(self):
        # Retornar una representación de la fecha y hora en formato aaaa/mm/dd HH:MM:SS
        return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(self.aaaa, self.mm, self.dd, self.HH, self.MM, self.SS)

    def fijarFecha(self,fecha):
        # Validar que el argumento sea un string
        if not isinstance(fecha, str):
            print("La fecha debe ser un string")
            return
        # Dividir el string por los separadores / o -
        fecha = fecha.replace("-", "/")
        fecha = fecha.split("/")
        # Validar que el string tenga tres partes (dd, mm, aaaa)
        if len(fecha) != 3:
            print("La fecha debe tener el formato dd/mm/aaaa o dd-mm-aaaa")
            return
        # Convertir las partes a enteros y asignarlas a variables locales
        try:
            dd = int(fecha[0])
            mm = int(fecha[1])
            aaaa = int(fecha[2])
        except ValueError:
            print("La fecha debe tener solo números")
            return
        # Validar que los valores sean válidos para una fecha
        if not (1 <= dd <= 31 and 1 <= mm <= 12 and 1900 <= aaaa <= 2100):
            print("La fecha tiene valores inválidos")
            return
        # Actualizar los atributos de la clase con los valores locales
        self.dd = dd
        self.mm = mm
        self.aaaa = aaaa

    def fijarHora(self,hora):
        # Validar que el argumento sea un string
        if not isinstance(hora, str):
            print("La hora debe ser un string")
            return
        # Dividir el string por los separadores :
        hora = hora.split(":")
        # Validar que el string tenga tres partes (HH, MM, SS)
        if len(hora) != 3:
            print("La hora debe tener el formato HH:MM:SS")
            return
        # Convertir las partes a enteros y asignarlas a variables locales
        try:
            HH = int(hora[0])
            MM = int(hora[1])
            SS = int(hora[2])
        except ValueError:
            print("La hora debe tener solo números")
            return
        # Validar que los valores sean válidos para una hora
        if not (0 <= HH <= 23 and 0 <= MM <= 59 and 0 <= SS <= 59):
            print("La hora tiene valores inválidos")
            return
        # Actualizar los atributos de la clase con los valores locales
        self.HH = HH
        self.MM = MM
        self.SS = SS

    def fijarFechaHora(self,fechahora):
      # Validar que el argumento sea un string
      if not isinstance(fechahora, str):
        print("La fecha y hora debe ser un string")
        return
      # Dividir el string por el espacio entre la fecha y la hora
      fechahora = fechahora.split()
      # Validar que el string tenga dos partes (fecha y hora)
      if len(fechahora) != 2:
        print("La fecha y hora debe tener el formato dd/mm/aaaa HH:MM:SS")
        return
      # Llamar al método fijarFecha con la primera parte del string
      self.fijarFecha(fechahora[0])
      # Llamar al método fijarHora con la segunda parte del string
      self.fijarHora(fechahora[1])

           