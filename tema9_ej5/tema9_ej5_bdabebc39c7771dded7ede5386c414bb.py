class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


class Tienda:
    def __init__(self):
        self.catalogo = []
        self.catalogo.append(Producto(1, "Camisa", 10000))
        self.catalogo.append(Producto(2, "Pantalon", 20000))
        self.catalogo.append(Producto(3, "Polera", 5000))
        self.catalogo.append(Producto(4, "Chaqueta", 30000))

    def menu(self):
        print("Catálogo:")
        for producto in self.catalogo:
            print(f"{producto.codigo}: {producto.nombre} - ${producto.precio}")


class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad


class Carro:
    def __init__(self):
        self.items = []

    def agregar_item(self, cantidad, producto):
        item = Item(producto, cantidad)
        self.items.append(item)

    def __str__(self):
        carrito = "Carro de Compras:\n"
        for item in self.items:
            carrito += f"{item.producto.nombre} - Cantidad: {item.cantidad} - Precio unitario: ${item.producto.precio}\n"
        return carrito


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
