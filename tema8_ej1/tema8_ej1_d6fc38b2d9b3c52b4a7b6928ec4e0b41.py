class CarroDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.calcular_descuento()
        return descuentos

    def calcular_despacho(self, tipoDespacho):
        valor_productos = sum([producto.precio for producto in self.productos])

        if tipoDespacho == 0:  # Despacho Aéreo Normal
            return 0.2 * valor_productos
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            return 0.3 * valor_productos

    def calcular_impuesto(self, direccion):
        if "Chile" in direccion:
            return 0.2
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto(direccion)

        valor_productos = sum([producto.precio for producto in self.productos])

        total_pagar = valor_productos - descuentos + despacho
        total_pagar *= (1 + impuesto)

        return total_pagar


# Ejemplo de uso
class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento

    def calcular_descuento(self):
        return self.precio * self.descuento


carro = CarroDeCompras()

producto1 = Producto("Camisa", 100, 0.1)  # Camisa con 10% de descuento
producto2 = Producto("Pantalón", 200, 0.2)  # Pantalón con 20% de descuento

carro.agregar_producto(producto1)
carro.agregar_producto(producto2)

tipoDespacho = 1  # Despacho Aéreo Express
direccion = "Alameda 340 Santiago Chile"

total_pagar = carro.checkout(tipoDespacho, direccion)
print("Total a pagar:", total_pagar)
