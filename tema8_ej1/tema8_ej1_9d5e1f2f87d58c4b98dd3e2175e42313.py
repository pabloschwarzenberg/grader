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
        descuento_total = self.calcular_descuento()
        despacho = self.calcular_despacho(tipoDespacho)
        total_pagar = self.calcular_total_pagar(descuento_total, despacho)

        if tipoDespacho == 1 and "chile" in direccion.lower():
            total_pagar *= 1.2

        return total_pagar

    def calcular_descuento(self):
        descuento_total = 0
        for item in self.lista_de_productos:
            descuento = item.producto.precio * 0.1  # Supongamos un descuento fijo del 10% por producto
            descuento_total += descuento * item.cantidad
        return descuento_total

    def calcular_despacho(self, tipoDespacho):
        valor_productos = sum(item.producto.precio * item.cantidad for item in self.lista_de_productos)
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            despacho = valor_productos * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            despacho = valor_productos * 0.3
        else:
            despacho = 0
        return despacho

    def calcular_total_pagar(self, descuento_total, despacho):
        valor_productos = sum(item.producto.precio * item.cantidad for item in self.lista_de_productos)
        total_pagar = valor_productos - descuento_total + despacho
        return total_pagar

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