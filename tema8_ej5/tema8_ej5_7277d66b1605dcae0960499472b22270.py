class FechaHora:
    def __init__(self, dia, mes, anio, hora, minuto, segundo):
        self.dia = dia
        self.mes = mes
        self.anio = anio
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def imprimir(self):
        print(":02d}/{:02d}/{:04d} {:02d}:{:02d}:{:02d}".format(self.dia, self.mes, self.anio, self.hora, self.minuto, self.segundo)")