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


class Carro:
    def __init__(self):
        self.lista_de_productos = []
        self.descuento = 0
        self.total = 0
        self.direccion = ""

    def agregar_item(self, cantidad, producto):
        for item in self.lista_de_productos:
            if item.producto == producto:
                if cantidad == 0:
                    self.lista_de_productos.remove(item)
                else:
                    item.cantidad = cantidad
                return
        item = Item(cantidad, producto)
        self.lista_de_productos.append(item)

    def checkout(self, tipoDespacho, direccion):
        self.total = 0
        self.direccion = direccion

        for item in self.lista_de_productos:
            self.total += item.cantidad * item.producto.precio

        # Calcular descuento
        self.descuento = 0
        if self.total >= 100:
            self.descuento = 0.1 * self.total

        # Calcular valor del despacho
        valor_despacho = 0
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            valor_despacho = 0.2 * self.total
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            valor_despacho = 0.3 * self.total

        # Calcular impuesto si la dirección es en Chile
        impuesto = 0
        if "chile" in direccion.lower():
            impuesto = 0.2 * self.total

        # Calcular valor total a pagar
        self.total -= self.descuento
        self.total += valor_despacho

        if "chile" in direccion.lower():
            self.total += 0.2 * self.total

        return self.total


class Tienda:
    def __init__(self):
        self.catalogo = []
        producto = Producto(1, "Juego Pokemon Y", 10, 31.51)
        self.catalogo.append(producto)
        producto = Producto(2, "Nintendo 3DS", 5, 190.95)
        self.catalogo.append(producto)
        producto = Producto(3, "Juego Mario Kart", 10, 29.96)
        self.catalogo.append(producto)
        producto = Producto(4, "Playstation 4", 10, 399)
        self.catalogo.append(producto)
        producto = Producto(5, "Fifa 14", 10, 41.95)

    def menu(self):
        for producto in self.catalogo:
            print("{0}: {1} ${2}".format(producto.codigo, producto.nombre, producto.precio))

    def buscarProducto(self, numero):
        for producto in self.catalogo:
            if producto.codigo == numero:
                return producto


def main():
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


if __name__ == "__main__":
    main()

