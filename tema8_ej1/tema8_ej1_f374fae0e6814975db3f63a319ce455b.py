class Producto:
    def __init__(self, codigo, nombre, stock, precio):
        self.codigo = codigo
        self.stock = stock
        self.precio = precio
        self.nombre = nombre

    def __eq__(self, other):
        if self.codigo == other.codigo:
            return True
        else:
            return False


class Item:
    def __init__(self, cantidad, producto):
        self.cantidad = cantidad
        self.producto = producto


class CarroCompras:
    def __init__(self):
        self.items = []

    def agregar_producto(self, item):
        if item.producto.stock >= item.cantidad:
            self.items.append(item)
            item.producto.stock -= item.cantidad
            print("Producto agregado al carro de compras.")
        else:
            print("No hay stock suficiente del producto.")

    def eliminar_producto(self, item):
        if item in self.items:
            self.items.remove(item)
            item.producto.stock += item.cantidad
            print("Producto eliminado del carro de compras.")
        else:
            print("El producto no se encuentra en el carro de compras.")

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.producto.precio * item.cantidad
        return total

    def checkout(self, tipoDespacho, direccion):
        total = self.calcular_total()

        descuentos = 0
        for item in self.items:
            descuentos += item.producto.precio * 0.1 * item.cantidad

        if tipoDespacho == 0:
            despacho = total * 0.2
        elif tipoDespacho == 1:
            despacho = total * 0.3
        else:
            print("Tipo de despacho inválido.")
            return

        if "Chile" in direccion:
            total += total * 0.2

        total -= descuentos
        total += despacho

        return total


if __name__ == "__main__":
    producto1 = Producto(1, "Producto 1", 10, 100)
    producto2 = Producto(2, "Producto 2", 5, 200)

    item1 = Item(2, producto1)
    item2 = Item(1, producto2)

    carro = CarroCompras()
    carro.agregar_producto(item1)
    carro.agregar_producto(item2)

    total_pagar = carro.checkout(1, "Alameda 340 Santiago Chile")
    print("Total a pagar:", total_pagar)