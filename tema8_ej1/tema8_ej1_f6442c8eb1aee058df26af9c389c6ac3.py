class Tienda:
    def __init__(self):
        self.carro = []

    def agregarProducto(self, producto):
        self.carro.append(producto)

    def calcularDescuentos(self):
        descuentos = 0
        for producto in self.carro:
            descuentos += producto.descuento()
        return descuentos

    def calcularDespacho(self, tipoDespacho):
        valor_productos = sum(producto.precio() for producto in self.carro)
        if tipoDespacho == 0:
            return valor_productos * 0.2
        elif tipoDespacho == 1:
            return valor_productos * 0.3

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcularDescuentos()
        despacho = self.calcularDespacho(tipoDespacho)
        valor_productos = sum(producto.precio() for producto in self.carro)
        impuesto = 0
        if "chile" in direccion.lower():
            impuesto = valor_productos * 0.2
        total_pagar = valor_productos - descuentos + despacho + impuesto
        return total_pagar


class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio_base = precio
        self.descuento_porcentaje = descuento

    def descuento(self):
        return self.precio_base * (self.descuento_porcentaje / 100)

    def precio(self):
        return self.precio_base - self.descuento()


if __name__ == "__main__":
    tienda = Tienda()

    producto1 = Producto("Camiseta", 20000, 10)
    producto2 = Producto("Pantalón", 30000, 20)
    producto3 = Producto("Zapatos", 50000, 15)

    tienda.agregarProducto(producto1)
    tienda.agregarProducto(producto2)
    tienda.agregarProducto(producto3)

    tipoDespacho = 0  # Despacho Aéreo Normal
    direccion = "Alameda 340 Santiago Chile"

    total_pagar = tienda.checkout(tipoDespacho, direccion)
    print("Total a pagar:", total_pagar)
