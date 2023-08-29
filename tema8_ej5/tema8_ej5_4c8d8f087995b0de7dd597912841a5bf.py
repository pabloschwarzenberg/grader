class FechaHora:
    def __init__(self, fecha=None, hora=None):
        self.fecha = fecha
        self.hora = hora

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fecha_hora):
        fecha, hora = fecha_hora.split()
        self.fecha = fecha
        self.hora = hora

    def cambiar(self, parametro):
        partes = parametro.split('=')
        if len(partes) != 2:
            print("Formato incorrecto. Debe ser 'nombre_parametro=valor'.")
            return
        
        nombre_parametro = partes[0].strip()
        valor_parametro = partes[1].strip()

        if nombre_parametro == 'dd':
            if not valor_parametro.isdigit() or int(valor_parametro) > 31:
                print("Valor incorrecto para día.")
                return
            self.fecha = "{}/{}/{}".format(valor_parametro, self.fecha[3:5], self.fecha[6:])
        elif nombre_parametro == 'mm':
            if not valor_parametro.isdigit() or int(valor_parametro) > 12:
                print("Valor incorrecto para mes.")
                return
            self.fecha = "{}/{}/{}".format(self.fecha[:2], valor_parametro, self.fecha[6:])
        elif nombre_parametro == 'aaaa':
            if not valor_parametro.isdigit() or len(valor_parametro) != 4:
                print("Valor incorrecto para año.")
                return
            self.fecha = "{}/{}/{}".format(self.fecha[:2], self.fecha[3:5], valor_parametro)
        elif nombre_parametro == 'HH':
            if not valor_parametro.isdigit() or int(valor_parametro) > 23:
                print("Valor incorrecto para hora.")
                return
            self.hora = "{}:{}:{}".format(valor_parametro, self.hora[3:5], self.hora[6:])
        elif nombre_parametro == 'MM':
            if not valor_parametro.isdigit() or int(valor_parametro) > 59:
                print("Valor incorrecto para minutos.")
                return
            self.hora = "{}:{}:{}".format(self.hora[:2], valor_parametro, self.hora[6:])
        elif nombre_parametro == 'SS':
            if not valor_parametro.isdigit() or int(valor_parametro) > 59:
                print("Valor incorrecto para segundos.")
                return
            self.hora = "{}:{}:{}".format(self.hora[:2], self.hora[3:5], valor_parametro)
        else:
            print("Parámetro inválido.")

    def __repr__(self):
        return "{}/{}/{} {}:{}:{}".format(self.fecha[6:], self.fecha[3:5], self.fecha[:2], self.hora[:2], self.hora[3:5], self.hora[6:])

