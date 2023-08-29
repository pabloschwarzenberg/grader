class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


class Tienda:
    def __init__(self):
        self.catalogo = [
            Producto(1, "Camisa", 20000),
            Producto(2, "Pantalón", 30000),
            Producto(3, "Zapatos", 50000),
        ]

    def menu(self):
        print("Catálogo de productos:")
        for producto in self.catalogo:
            print(f"{producto.codigo}. {producto.nombre} - ${producto.precio}")


class Carro:
    def __init__(self):
        self.items = []

    def agregar_item(self, cantidad, producto):
        self.items.append((cantidad, producto))

    def __str__(self):
        carro_str = "Carro de compras:\n"
        for cantidad, producto in self.items:
            carro_str += f"{producto.nombre} - Cantidad: {cantidad}\n"
        return carro_str

    def buscarProducto(self, numero):
        for producto in self.catalogo:
            if producto.codigo == numero:
                return producto

    def checkout(self, tipoDespacho, direccion):
        total_productos = 0
        for cantidad, producto in self.items:
            total_productos += cantidad * producto.precio

        descuento = total_productos * 0.1  # Descuento del 10% sobre el total

        if tipoDespacho == 0:  # Despacho Aéreo Normal
            valor_despacho = total_productos * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            valor_despacho = total_productos * 0.3
        else:
            valor_despacho = 0

        if "chile" in direccion.lower():  # Despacho a Chile
            total = total_productos - descuento + valor_despacho
            impuesto = total * 0.2
            total += impuesto
        else:
            total = total_productos - descuento + valor_despacho

        return total


if __name__ == "__main__":
    tienda = Tienda()
    carro = Carro()
    while True:
        tienda.menu()
        item_ingresado = input("Ingresa un producto a comprar (numero,cantidad): ")
        if item_ingresado == "":
            break
        else:
            item_ingresado = item_ingresado.split(",")
            numero = int(item_ingresado[0])
            producto = tienda.buscarProducto(numero)
            cantidad = int(item_ingresado[1])
            carro.agregar_item(cantidad, producto)
        print(carro)

    print(carro.checkout(0, "usa"))
    print(carro.checkout(1, "usa"))
    print(carro.checkout(0, "Alameda 340 Santiago Chile"))
    print(carro.checkout(1, "Alameda 340 Santiago Chile"))

           