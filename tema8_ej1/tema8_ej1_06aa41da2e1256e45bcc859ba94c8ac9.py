class Carro:
    def __init__(self):
        self.lista_de_productos = []

    def agregar_item(self, cantidad, producto):
        item = ItemCarro(cantidad, producto)
        self.lista_de_productos.append(item)

    def __str__(self):
        s = "Carro de Compras:\n"
        for item in self.lista_de_productos:
            s += "{0}: {1}\n".format(item.cantidad, item.producto.nombre)
        return s

    def checkout(self, tipoDespacho, direccion):
        total_productos = 0
        total_descuentos = 0
        for item in self.lista_de_productos:
            total_productos += item.cantidad * item.producto.precio
            total_descuentos += item.producto.calcular_descuento(item.cantidad)

        valor_despacho = 0
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            valor_despacho = total_productos * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            valor_despacho = total_productos * 0.3

        total_pagar = total_productos - total_descuentos + valor_despacho

        if "Chile" in direccion:
            total_pagar *= 1.2  # Agregar 20% por concepto de impuesto

        return total_pagar


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
