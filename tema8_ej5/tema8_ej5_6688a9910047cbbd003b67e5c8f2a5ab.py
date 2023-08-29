class FechaHora:
    def __init__(self):
        self.fecha = ""
        self.hora = ""
    def fijarHora(self,string_hora):
        self.hora = string_hora
    def fijarFecha(self,string_fecha):
        if string_fecha.find("-") != -1:
            lista =string_fecha.split("-")
            año = lista[2]
            mes = lista[1]
            dia = lista[0]
            self.fecha = año + "/" + mes + "/" + dia
        else:
            lista = string_fecha.split("/")
            año = lista[2]
            mes = lista[1]
            dia = lista[0]
            self.fecha = año + "/" + mes + "/" + dia
    def fijarFechaHora(self,string):
        fecha_y_hora = string.split(" ")
        self.hora = fecha_y_hora[1]

        if fecha_y_hora[0].find("-") != -1:
            lista = fecha_y_hora[0].split("-")
            año = lista[2]
            mes = lista[1]
            dia = lista[0]
            self.fecha = año + "/" + mes + "/" + dia
        else:
            lista = fecha_y_hora[0].split("/")
            año = lista[2]
            mes = lista[1]
            dia = lista[0]
            self.fecha = año + "/" + mes + "/" + dia
        
    def cambiar(self,parametro):
        lista_parametro = parametro.split("=")
        fecha_auxiliar = self.fecha
        hora_auxiliar = self.hora
        if isinstance(int(lista_parametro[1]),int):
            if lista_parametro[0] == "dd":
                if int(lista_parametro[1]) > 30 or int(lista_parametro[1]) < 0:
                    return False
                else:
                    lista_fecha = fecha_auxiliar.split("/")
                    lista_fecha[2] = lista_parametro[1]
                    "/".join(lista_fecha)
                    self.fecha = lista_fecha
            elif lista_parametro[0] == "mm":
                if int(lista_parametro[1]) < 0 or int(lista_parametro[1]) > 12:
                    return False
                else:
                    lista_fecha = fecha_auxiliar.split("/")
                    lista_fecha[1] = lista_parametro[1]
                    "/".join(lista_fecha)
                    self.fecha = lista_fecha
            elif lista_parametro[0] == "aaaa":
                if int(lista_parametro[1]) < 0:
                    return False
                else:
                    lista_fecha = fecha_auxiliar.split("/")
                    lista_fecha[0] = parametro[1]
                    "/".join(lista_fecha)
                    self.fecha = lista_fecha

            elif lista_parametro[0] == "HH":
                if int(lista_parametro[1]) < 0 or int(lista_parametro[1]) > 24:
                    return False
                else:
                    lista_hora = hora_auxiliar.split(":")
                    lista_hora[0] = lista_parametro[1]
                    ":".join(lista_hora)
                    self.hora = lista_hora
            elif lista_paramtero[0] == "MM":
                if int(lista_parametro[1]) < 0 or int(lista_parametro[1]) > 59:
                    return False
                else:
                    lista_hora = hora_auxiliar.split(":")
                    lista_hora[1] = lista_paramtero[1]
                    ":".join(lista_hora)
                    self.hora = lista_hora
            elif lista_parametro[1] <0 or lista_parametro[1] > 0:
                return False
            else:
                lista_hora = hora_auxiliar.split(":")
                lista_hora[2] = lista_parametro[1]
                ":".join(lista_hora)
                self.hora = lista_hora
        else:
            return False
    def __str__(self):
        string = self.fecha
        string += " "
        string += self.hora
        return string
            
            