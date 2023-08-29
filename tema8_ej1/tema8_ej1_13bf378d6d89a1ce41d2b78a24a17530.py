class CarroCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.precio * producto.descuento
        return descuentos

    def calcular_despacho(self, tipoDespacho):
        valor_productos = sum([producto.precio for producto in self.productos])
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            return 0.2 * valor_productos
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            return 0.3 * valor_productos
        else:
            return 0

    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            return 0.2
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto(direccion)

        valor_productos = sum([producto.precio for producto in self.productos])
        total_pagar = valor_productos - descuentos + despacho
        total_pagar += impuesto * total_pagar

        return total_pagar


class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento



carro = CarroCompras()

while True:
    nombre = input("Ingrese el nombre del producto y aprete (q) para pasar a los envios: ")
    if nombre == 'q':
        break
    precio = float(input("Ingrese el precio del producto: "))
    descuento = float(input("Ingrese el descuento del producto (en decimal y escribalo con puntoy no coma ): "))

    producto = Producto(nombre, precio, descuento)
    carro.agregar_producto(producto)

tipo_despacho = int(input("Ingrese el tipo de despacho (0 para Aéreo Normal, 1 para Aéreo Express): "))
direccion = input("Ingrese la dirección de despacho: ")

total_pagar = carro.checkout(tipo_despacho, direccion)
print("Total a pagar:", total_pagar)