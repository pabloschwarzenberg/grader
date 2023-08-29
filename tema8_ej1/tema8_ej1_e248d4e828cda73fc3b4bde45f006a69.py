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
        total_productos = 0
        for item in self.lista_de_productos:
            total_productos += item.cantidad * item.producto.precio

        if tipoDespacho == 0:  # Despacho Aéreo Normal
            valor_despacho = 0.2 * total_productos
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            valor_despacho = 0.3 * total_productos
        else:
            print("Tipo de despacho inválido.")
            return

        impuesto = 0
        if "chile" in direccion.lower():  # Despacho hacia Chile
            impuesto = 0.2 * total_productos

        total_pagar = total_productos + valor_despacho + impuesto
        return total_pagar

    def __repr__(self):
        s = "Carro de Compras:\n"
        for item in self.lista_de_productos:
            s = s + "{0}: {1}\n".format(item.cantidad, item.producto.nombre)
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
            print("{0}: {1} ${2}".format(producto.codigo, producto.nombre, producto.precio))

    def buscarProducto(self, numero):
        for producto in self.catalogo:
            if producto.codigo == numero:
                return producto


if __name__ == "__main__":
    tienda = Tienda()
    carro = Carro()
    while True:
        tienda.menu()
        item_ingresado = input("Ingresa un número de producto (0 para salir): ")
        if item_ingresado == '0':
            break

        cantidad_ingresada = int(input("Ingresa la cantidad: "))
        producto_seleccionado = tienda.buscarProducto(int(item_ingresado))
        carro.agregar_item(cantidad_ingresada, producto_seleccionado)

    tipo_despacho = int(input("Selecciona el tipo de despacho (0 para Despacho Aéreo Normal, 1 para Despacho Aéreo Express): "))
    direccion = input("Ingresa la dirección de envío: ")

    total_pagar = carro.checkout(tipo_despacho, direccion)
    print("El total a pagar es: ${:.2f}".format(total_pagar))