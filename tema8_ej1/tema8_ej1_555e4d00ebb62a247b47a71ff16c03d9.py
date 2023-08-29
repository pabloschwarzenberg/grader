class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


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
            if item.producto.codigo == producto.codigo:
                if cantidad == 0:
                    self.lista_de_productos.remove(item)
                else:
                    item.cantidad = cantidad
                return
        item = Item(cantidad, producto)
        self.lista_de_productos.append(item)

    def calcular_descuentos(self):
        self.descuento = 0
        for item in self.lista_de_productos:
            descuento_producto = item.producto.precio * item.cantidad * 0.1
            self.descuento += descuento_producto

    def calcular_despacho(self, tipoDespacho):
        if tipoDespacho == 0:
            self.total += self.total * 0.2
        elif tipoDespacho == 1:
            self.total += self.total * 0.3

    def checkout(self, tipoDespacho, direccion):
        self.total = 0
        for item in self.lista_de_productos:
            subtotal = item.producto.precio * item.cantidad
            self.total += subtotal

        self.calcular_descuentos()
        self.calcular_despacho(tipoDespacho)

        if "chile" in direccion.lower():
            self.total += self.total * 0.2

        return self.total

    def __repr__(self):
        s = "Carro de Compras:\n"
        for item in self.lista_de_productos:
            s += "{0}: {1}\n".format(item.cantidad, item.producto.nombre)
        return s


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
        self.catalogo.append(producto)

    def menu(self):
        for producto in self.catalogo:
            print("{0}: {1} ${2}".format(
                producto.codigo, producto.nombre, producto.precio))

    def buscarProducto(self, numero):
        for producto in self.catalogo:
            if producto.codigo == numero:
                return producto


if __name__ == "__main__":
    tienda = Tienda()
    carro = Carro()

    while True:
        tienda.menu()
        item_ingresado = input("Ingresa un producto a comprar (numero,cantidad): ")
        if item_ingresado == "":
            break
        else:
            item = item_ingresado.split(",")
            codigo_producto = int(item[0])
            cantidad = int(item[1])
            producto = tienda.buscarProducto(codigo_producto)
            carro.agregar_item(cantidad, producto)

    tipo_despacho = int(input("Selecciona el tipo de despacho (0 = Despacho Aéreo Normal, 1 = Despacho Aéreo Express): "))
    direccion = input("Ingresa la dirección de despacho: ")

    total_pagar = carro.checkout(tipo_despacho, direccion)
    print("Total a pagar:", total_pagar)
    print(carro)
