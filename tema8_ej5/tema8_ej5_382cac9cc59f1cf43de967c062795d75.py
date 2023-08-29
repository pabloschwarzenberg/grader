class FechaHora():
    def __init__(self):
        self.fecha = ""
        self.hora = ""
        pass

    def fijarFecha(self, fecha):
        self.fecha = fecha
        pass

    def fijarHora(self, hora):
        self.hora = hora
        pass

    def fijarFechaHora(self, fechahora):
        fechahora = fechahora.split()
        self.fecha = fechahora[0]
        self.hora = fechahora[1]
        return

    def cambiar(self, cambioespecifico):
        "".join(cambioespecifico.split())
        self.fecha = self.fecha.split("-")
        self.hora = self.hora.split(":")

        if cambioespecifico[0:2] == "dd":
            if int(cambioespecifico[3:]) > 31 or int(cambioespecifico[3:]) < 1:
                print("no existe esta fecha")
            else:
                self.fecha[0] = cambioespecifico[3:]

        elif cambioespecifico[0:2] == "mm":
            if int(cambioespecifico[3:]) > 12 or int(cambioespecifico[3:]) < 1:
                print("no existe esta fecha")
            else:
                self.fecha[1] = cambioespecifico[3:]

        elif cambioespecifico[0:4] == "aaaa":
            if int(cambioespecifico[6:]) < 0:
                print("no existe esta fecha")
            else:
                self.fecha[2] = cambioespecifico[6:]

        elif cambioespecifico[0:2] == "HH":
            if int(cambioespecifico[4:]) > 24 or int(cambioespecifico[4:]) < 0:
                print("no existe esta fecha")
            else:
                self.hora[0] = cambioespecifico[4:]

        elif cambioespecifico[0:2] == "MM":
            if int(cambioespecifico[4:]) > 59 or int(cambioespecifico[4:]) < 0:
                print("no existe esta fecha")
            else:
                self.hora[1] = cambioespecifico[4:]

        elif cambioespecifico[0:2] == "SS":
            if int(cambioespecifico[4:]) > 59 or print(cambioespecifico[4:]) < 0:
                print("no existe esta fecha")
            else:
                self.hora[2] = cambioespecifico[4:]
        self.fecha = "-".join(self.fecha)
        self.hora = ":".join(self.hora)

        return

    def __str__(self):
        self.fecha = self.fecha.split("-")
        dia = self.fecha[0]
        ano = self.fecha[-1]
        self.fecha[0] = ano
        self.fecha[-1] = dia
        self.fecha = ("/").join(self.fecha)
        return self.fecha.strip() + "  " + self.hora.strip()
 
if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
