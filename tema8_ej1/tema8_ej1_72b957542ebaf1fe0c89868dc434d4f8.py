class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"{self.nombre}: ${self.precio}"


class CarroCompras:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def eliminarProducto(self, producto):
        self.productos.remove(producto)

    def obtenerTotal(self):
        total = sum(producto.precio for producto in self.productos)
        return total

    def checkout(self, tipoDespacho, direccion):
        descuentos = sum(producto.precio * 0.1 for producto in self.productos)
        despacho = 0

        if tipoDespacho == 0:
            despacho = self.obtenerTotal() * 0.2
        elif tipoDespacho == 1:
            despacho = self.obtenerTotal() * 0.3

        total = self.obtenerTotal() - descuentos + despacho

        if "chile" in direccion.lower():
            total += total * 0.2

        return total


if __name__ == "__main__":
    carro = CarroCompras()
    producto1 = Producto("Camisa", 15000)
    producto2 = Producto("Pantalón", 30000)
    producto3 = Producto("Zapatos", 50000)

    carro.agregarProducto(producto1)
    carro.agregarProducto(producto2)
    carro.agregarProducto(producto3)

    print("Productos en el carro:")
    for producto in carro.productos:
        print(producto)

    total = carro.obtenerTotal()
    print(f"Total: ${total}")

    tipoDespacho = 0
    direccion = "Alameda 340 Santiago Chile"
    total_pagar = carro.checkout(tipoDespacho, direccion)
    print(f"Total a pagar: ${total_pagar}")
