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

    def calcular_descuento(self):
        total_descuento = 0
        for item in self.lista_de_productos:
            producto = item.producto
            descuento_producto = producto.precio * 0.1  # 10% de descuento
            total_descuento += descuento_producto * item.cantidad
        self.descuento = total_descuento

    def calcular_despacho(self, tipoDespacho):
        total_productos = self.calcular_total_productos()
        if tipoDespacho == 0:
            despacho = total_productos * 0.2  # 20% del valor de los productos
        elif tipoDespacho == 1:
            despacho = total_productos * 0.3  # 30% del valor de los productos
        else:
            despacho = 0
        return despacho

    def calcular_total_productos(self):
        total_productos = 0
        for item in self.lista_de_productos:
            producto = item.producto
            total_producto = producto.precio * item.cantidad
            total_productos += total_producto
        return total_productos

    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            impuesto = self.total * 0.2  # 20% de impuesto
        else:
            impuesto = 0
        return impuesto

    def checkout(self, tipoDespacho, direccion):
        self.calcular_descuento()
        self.total = self.calcular_total_productos()
        despacho = self.calcular_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto(direccion)
        total_pagar = self.total - self.descuento + despacho + impuesto
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
        producto = Producto(5, "Fifa 14", 10, 41

           