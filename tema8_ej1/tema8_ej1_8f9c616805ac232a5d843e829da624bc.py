class CarroCompras:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularDescuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.precio * producto.descuento / 100
        return descuentos

    def calcularDespacho(self, tipoDespacho):
        valorProductos = sum(producto.precio for producto in self.productos)
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            return 0.2 * valorProductos
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            return 0.3 * valorProductos
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcularDescuentos()
        despacho = self.calcularDespacho(tipoDespacho)
        total = sum(producto.precio for producto in self.productos) - descuentos + despacho
        if "chile" in direccion.lower():
            total *= 1.2  # Aplicar 20% de impuesto para despachos a Chile
        return total


class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento


# Ejemplo de uso
if __name__ == "__main__":
    carro = CarroCompras()
    producto1 = Producto("Camisa", 10000, 10)
    producto2 = Producto("Pantalón", 20000, 15)
    producto3 = Producto("Zapatos", 50000, 20)
    carro.agregarProducto(producto1)
    carro.agregarProducto(producto2)
    carro.agregarProducto(producto3)

    tipoDespacho = 0  # Despacho Aéreo Normal
    direccion = "Alameda 340 Santiago Chile"
    total_a_pagar = carro.checkout(tipoDespacho, direccion)
    print("Total a pagar:", total_a_pagar)
