class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

class Carro:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularTotal(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

class Tienda:
    def __init__(self):
        self.productos = [
            Producto(1, "Camiseta", 5000),
            Producto(2, "Pantalón", 10000),
            Producto(3, "Zapatos", 15000)
        ]
        self.carro = Carro()

    def buscarProducto(self, id):
        for producto in self.productos:
            if producto.id == id:
                return producto
        return None

    def agregarProductoAlCarro(self, id):
        producto = self.buscarProducto(id)
        if producto:
            self.carro.agregarProducto(producto)
            print("Producto agregado al carro:", producto.nombre)
        else:
            print("Producto no encontrado")

    def mostrarCarro(self):
        print("Productos en el carro:")
        for producto in self.carro.productos:
            print(producto.nombre)

    def calcularTotalCarro(self):
        total = self.carro.calcularTotal()
        print("Total a pagar:", total)

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcularDescuentos()
        despacho = self.calcularDespacho(tipoDespacho)
        impuesto = self.calcularImpuesto(direccion)
        total = self.carro.calcularTotal() - descuentos + despacho + impuesto
        return total

    def calcularDescuentos(self):
        descuentos = 0
        for producto in self.carro.productos:
            descuentos += producto.precio * 0.1  # Aplicar descuento del 10%
        return descuentos

    def calcularDespacho(self, tipoDespacho):
        total = self.carro.calcularTotal()
        if tipoDespacho == 0:
            return total * 0.2  # Despacho Aéreo Normal: 20% del valor de los productos
        elif tipoDespacho == 1:
            return total * 0.3  # Despacho Aéreo Express: 30% del valor de los productos
        else:
            return 0

    def calcularImpuesto(self, direccion):
        if "Chile" in direccion:
            total = self.carro.calcularTotal()
            return total * 0.2  # Agregar impuesto del 20% si el despacho es hacia Chile
        else:
            return 0


if __name__ == "__main__":
    tienda = Tienda()

    tienda.agregarProductoAlCarro(1)
    tienda.agregarProductoAlCarro(2)
    tienda.agregarProductoAlCarro(3)

    tienda.mostrarCarro()
    tienda.calcularTotalCarro()

    total_pagar = tienda.checkout(1, "Alameda 340 Santiago Chile")
    print("Total a pagar con descuentos, despacho e impuesto:", total_pagar)
