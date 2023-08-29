class FechaHora:
    def __init__(self):
        self.fecha = None
        self.hora = None

    def __str__(self):
        return f"{self.fecha} {self.hora}"

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fechahora):
        fecha, hora = fechahora.split()
        self.fecha = fecha
        self.hora = hora

    def cambiar(self, parte):
        tipo, valor = parte.split('=')
        tipo = tipo.strip().lower()
        valor = valor.strip()
        
        if tipo == 'dd':
            if not valor.isdigit() or int(valor) > 31:
                print("Día inválido")
                return
            self.fecha = self.fecha[:2] + valor + self.fecha[4:]
        elif tipo == 'mm':
            if not valor.isdigit() or int(valor) > 12:
                print("Mes inválido")
                return
            self.fecha = self.fecha[:5] + valor + self.fecha[7:]
        elif tipo == 'aaaa':
            if not valor.isdigit():
                print("Año inválido")
                return
            self.fecha = valor + self.fecha[4:]
        elif tipo == 'hh':
            if not valor.isdigit() or int(valor) > 23:
                print("Hora inválida")
                return
            self.hora = valor + self.hora[2:]
        elif tipo == 'min':
            if not valor.isdigit() or int(valor) > 59:
                print("Minuto inválido")
                return
            self.hora = self.hora[:3] + valor + self.hora[5:]
        elif tipo == 'ss':
            if not valor.isdigit() or int(valor) > 59:
                print("Segundo inválido")
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