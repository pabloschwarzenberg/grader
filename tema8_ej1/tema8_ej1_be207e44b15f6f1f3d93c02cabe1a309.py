import tienda

class CarroDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.descuento
        return descuentos

    def calcular_valor_despacho(self, tipoDespacho):
        valor_productos = sum([producto.precio for producto in self.productos])
        if tipoDespacho == 0:
            return valor_productos * 0.2  # Despacho Aéreo Normal
        elif tipoDespacho == 1:
            return valor_productos * 0.3  # Despacho Aéreo Express
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        valor_despacho = self.calcular_valor_despacho(tipoDespacho)
        valor_total = sum([producto.precio for producto in self.productos]) - descuentos + valor_despacho
        if "chile" in direccion.lower():
            valor_total += valor_total * 0.2  # Agregar impuesto del 20% para despachos a Chile
        return valor_total


class Producto:
    def __init__(self, nombre, precio, descuento=0):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento


# Ejemplo de uso
carrito = CarroDeCompras()

producto1 = Producto("Camisa", 30, 5)
producto2 = Producto("Pantalón", 50, 10)
producto3 = Producto("Zapatos", 80)

carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)

tipo_despacho = 1  # Despacho Aéreo Express
direccion = "Alameda 340 Santiago Chile"

total_a_pagar = carrito.checkout(tipo_despacho, direccion)
print("Total a pagar:", total_a_pagar)
