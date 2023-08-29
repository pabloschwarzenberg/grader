class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return self.nombre + " " + str(self.precio)


class Cliente:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
        self.carro = []

    def __str__(self):
        return self.nombre + " " + self.rut

    def agregarProducto(self, producto):
        self.carro.append(producto)

    def checkout(self, tipoDespacho, direccion):
        total = 0
        for producto in self.carro:
            total += producto.precio

        descuento = 0
        if tipoDespacho == 0:
            descuento = total * 0.2
        elif tipoDespacho == 1:
            descuento = total * 0.3

        total -= descuento

        if "Chile" in direccion:
            total *= 1.2

        return total



producto1 = Producto("Polera", 10000)
producto2 = Producto("Pantalon", 20000)
producto3 = Producto("Calcetines", 5000)

cliente = Cliente("Juan", "12345678")
cliente.agregarProducto(producto1)
cliente.agregarProducto(producto2)
cliente.agregarProducto(producto3)

total_a_pagar = cliente.checkout(1, "Alameda 340 Santiago Chile")
print("Total a pagar:", total_a_pagar)
