class CarroDeCompras:
    def __init__(self):
        self.productos = []
        self.descuentos = 0
        self.despacho = 0
        self.impuesto = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_descuentos(self):
        for producto in self.productos:
            if producto[0] == 1:
                self.descuentos += producto[2] * 0.1
            elif producto[0] == 2:
                self.descuentos += producto[2] * 0.15
            elif producto[0] == 3:
                self.descuentos += producto[2] * 0.2

    def calcular_despacho(self, tipo_despacho):
        valor_productos = sum([producto[2] for producto in self.productos])
        if tipo_despacho == 0:
            self.despacho = valor_productos * 0.2
        elif tipo_despacho == 1:
            self.despacho = valor_productos * 0.3

    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            self.impuesto = (sum([producto[2] for producto in self.productos]) - self.descuentos + self.despacho) * 0.2

    def checkout(self, tipo_despacho, direccion):
        self.calcular_descuentos()
        self.calcular_despacho(tipo_despacho)
        self.calcular_impuesto(direccion)
        valor_total = sum([producto[2] for producto in self.productos]) - self.descuentos + self.despacho + self.impuesto
        return valor_total

carro_de_compras = CarroDeCompras()

p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

carro_de_compras.agregar_producto(p1)
carro_de_compras.agregar_producto(p2)
carro_de_compras.agregar_producto(p3)
carro_de_compras.agregar_producto(p4)
carro_de_compras.agregar_producto(p5)

tipo_despacho = int(input("Ingrese el tipo de despacho (0: Aéreo Normal, 1: Aéreo Express): "))
direccion = input("Ingrese la dirección de despacho: ")

valor_total = carro_de_compras.checkout(tipo_despacho, direccion)

print(f"El valor total a pagar es: {valor_total}")
