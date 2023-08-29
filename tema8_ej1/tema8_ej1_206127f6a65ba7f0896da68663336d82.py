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
        descuento = self.calcular_descuento()
        despacho = self.calcular_despacho(tipoDespacho)
        total = self.calcular_total(descuento, despacho, direccion)
        return total

    def calcular_descuento(self):
        descuento_total = 0
        for item in self.lista_de_productos:
            descuento_total += item.cantidad * item.producto.precio * 0.1  # 10% de descuento por producto
        return descuento_total

    def calcular_despacho(self, tipoDespacho):
        total_productos = sum(item.cantidad * item.producto.precio for item in self.lista_de_productos)
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            return total_productos * 0.2  # 20% del valor de los productos
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            return total_productos * 0.3  # 30% del valor de los productos

    def calcular_total(self, descuento, despacho, direccion):
        total_productos = sum(item.cantidad * item.producto.precio for item in self.lista_de_productos)
        total = total_productos - descuento + despacho
        if "chile" in direccion.lower():
            total *= 1.2  # Agregar 20% de impuesto si el despacho es hacia Chile
        return total

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
        producto = Producto(5, "Fifa 14", 19.99, 0)
        self.catalogo.append(producto)

    def buscar_producto(self, codigo):
        for producto in self.catalogo:
            if producto.codigo == codigo:
                return producto
        return None


tienda_i = Tienda()
carro_i = Carro()
carro_i.agregar_item(2, tienda_i.buscar_producto(1))  # Agregar 2 juegos Pokemon Y al carro
carro_i.agregar_item(1, tienda_i.buscar_producto(2))  # Agregar 1 Nintendo 3DS al carro
carro_i.agregar_item(3, tienda_i.buscar_producto(4))  # Agregar 3 Playstation 4 al carro
print(carro_i)  # Imprimir el contenido del carro
total_pagar = carro_i.checkout(0, "Alameda 340 Santiago Chile")  # Realizar el checkout con despacho normal a Chile
print("Total a pagar:", total_pagar)
