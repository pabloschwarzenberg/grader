class Tienda:
    def __init__(self):
        self.carro = CarroCompras()

    def agregar_producto(self, producto):
        self.carro.agregar_producto(producto)

    def eliminar_producto(self, producto):
        self.carro.eliminar_producto(producto)

    def realizar_compra(self, tipoDespacho, direccion):
        total_pagar = self.carro.checkout(tipoDespacho, direccion)
        print("Total a pagar:", total_pagar)


class CarroCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def checkout(self, tipoDespacho, direccion):
        total = self.calcular_total()
        descuento = 0

        # Calcular descuentos
        for producto in self.productos:
            descuento += producto.calcular_descuento()

        # Calcular valor del despacho
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            despacho = 0.2 * total
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            despacho = 0.3 * total
        else:
            despacho = 0

        # Calcular impuesto si el despacho es hacia Chile
        if "chile" in direccion.lower():
            total += 0.2 * total

        # Calcular valor total a pagar
        total = total - descuento + despacho

        return total


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_descuento(self):
        return 0.1 * self.precio  # Descuento del 10%


# Ejemplo de uso
tienda = Tienda()

producto1 = Producto("Camiseta", 20)
producto2 = Producto("Pantalón", 30)
producto3 = Producto("Zapatos", 50)

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

tienda.realizar_compra(1, "Alameda 340 Santiago Chile")
