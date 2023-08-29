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
        self.items.append(item)

    def eliminar_producto(self, producto):
        for item in self.items:
            if item.producto == producto:
                self.items.remove(item)
                break

    def obtener_total(self):
        total = 0
        for item in self.items:
            total += item.producto.precio * item.cantidad
        return total

    def checkout(self, tipoDespacho, direccion):
        total_productos = self.obtener_total()

        descuentos = total_productos * 0.1  # Descuentos aplicados (10% del total de productos)

        if tipoDespacho == 0:  # Despacho Aéreo Normal
            valor_despacho = total_productos * 0.2  # 20% del valor de los productos
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            valor_despacho = total_productos * 0.3  # 30% del valor de los productos
        else:
            valor_despacho = 0

        if "Chile" in direccion:  # Despacho a Chile (aplicar impuesto)
            total_pagar = total_productos - descuentos + valor_despacho + (total_productos * 0.2)
        else:
            total_pagar = total_productos - descuentos + valor_despacho

        return total_pagar


# Ejemplo de uso
if __name__ == "__main__":
    producto1 = Producto(1, "Camisa", 10, 20)
    producto2 = Producto(2, "Pantalón", 5, 30)
    producto3 = Producto(3, "Zapatos", 2, 50)

    item1 = Item(2, producto1)
    item2 = Item(1, producto2)
    item3 = Item(3, producto3)

    carro = CarroCompras()
    carro.agregar_producto(item1)
    carro.agregar_producto(item2)
    carro.agregar_producto(item3)

    total_pagar = carro.checkout(1, "123 Main St Chile")
    print("Total a pagar:", total_pagar)

           