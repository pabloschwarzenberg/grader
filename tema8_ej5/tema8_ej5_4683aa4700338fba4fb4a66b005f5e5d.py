class FechaHora:
    def _init_(self):
        self.fecha = ''
        self.hora = ''

    def __str__(self):

        dia = self.fecha[:2]
        mes = self.fecha[3:5]
        year = self.fecha[6:]

        fecha_formato = year + '/' + mes + '/' + dia

        return fecha_formato + ' ' + self.hora

    def fijarFecha(self, fecha):
        self.fecha = fecha
        self.fecha = self.fecha.replace('-', '/')

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fechahora):
        fecha, hora = fechahora.split()
        self.fecha = fecha
        self.fecha = self.fecha.replace('-', '/')
        self.hora = hora

    def cambiar(self, parte):
        tipo, valor = parte.split('=')
        tipo = tipo.strip().lower()
        valor = valor.strip()

        self.fecha = self.fecha.replace('-', '/')

        if tipo == 'dd':
            if not valor.isdigit() or int(valor) < 1 or int(valor) > 31:
                print("Error: El día debe ser un número entre 1 y 31.")
                return
            self.fecha = valor + self.fecha[2:]
        
        elif tipo == 'mm':
            if not valor.isdigit() or int(valor) < 1 or int(valor) > 12:
                print("Error: El mes debe ser un número entre 1 y 12.")
                return
            self.fecha = self.fecha[:3] + valor + self.fecha[5:]
        
        elif tipo == 'aaaa':
            if not valor.isdigit() or len(valor) != 4:
                print("Error: El año debe ser un número de 4 dígitos.")
                return
            self.fecha = self.fecha[:6] + valor


        elif tipo == 'hh':
            if not valor.isdigit() or int(valor) < 0 or int(valor) > 23:
                print("Error: La hora debe ser un número entre 0 y 23.")
                return
            self.hora = valor + self.hora[2:]
        elif tipo == 'mm':
            if not valor.isdigit() or int(valor) < 0 or int(valor) > 59:
                print("Error: Los minutos deben ser un número entre 0 y 59.")
                return
            self.hora = self.hora[:3] + valor + self.hora[5:]
        elif tipo == 'ss':
            if not valor.isdigit() or int(valor) < 0 or int(valor) > 59:
                print("Error: Los segundos deben ser un número entre 0 y 59.")
                return
            self.hora = self.hora[:6] + valor

if __name__ == "__main__":
    fh = FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa=2016")
    print(fh)