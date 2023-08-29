class Producto:
    def __init__(self,codigo,nombre,stock,precio):
        self.codigo = codigo
        self.stock = stock
        self.precio = precio
        self.nombre = nombre

    def __eq__(self,other):
        return self.codigo == other.codigo


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
        item=Item(cantidad,producto)
        self.lista_de_productos.append(item)
        self.total += producto.precio
    
    def calcular_descuento(self):
        self.descuento = 0

        carrito = [0, 0, 0, 0, 0]

        tienda = Tienda()

        p1 = tienda.buscarProducto(1).precio
        p2 = tienda.buscarProducto(2).precio
        p3 = tienda.buscarProducto(3).precio
        p4 = tienda.buscarProducto(4).precio
        p5 = tienda.buscarProducto(5).precio

        for item in self.lista_de_productos:
            carrito[item.producto.codigo - 1] = item.cantidad

        if carrito[0] > 0 and carrito[1] > 0 and carrito[2] > 0:
            carrito[0] -= 1
            carrito[1] -= 1
            carrito[2] -= 1
            self.descuento += (p1 + p2 + p3) * 0.2
        elif carrito[3] > 0 and carrito[4] > 0:
            carrito[3] -= 1
            carrito[4] -= 1
            self.descuento += (p4 + p5) * 0.15
        

    def checkout(self, tipoDespacho, direccion):
        direccion = direccion.lower()
        self.calcular_descuento()

        precio_total = self.total - self.descuento

        if tipoDespacho == 0:
            precio_total += precio_total * 0.2
        else:
            precio_total += precio_total * 0.3

        if "chile" in direccion:
            precio_total += precio_total * 0.2
        
        return round(precio_total, 0)

    def __repr__(self):
        s = "Carro de Compras:\n"
        for item in self.lista_de_productos:
            s += "{0}: {1}\n".format(item.cantidad,item.producto.nombre)
        return s

class Tienda:
    def  __init__(self):
        self.catalogo = []
        self.catalogo.append(Producto(1,"Juego Pokemon Y",10,31.51))
        self.catalogo.append(Producto(2,"Nintendo 3DS",5,190.95))
        self.catalogo.append(Producto(3,"Juego Mario Kart",10,29.96))
        self.catalogo.append(Producto(4,"Playstation 4",10,399))
        self.catalogo.append(Producto(5,"Fifa 14",10,41.95))

    def menu(self):
        for producto in self.catalogo:
            print("{0}: {1} ${2}".format(producto.codigo, producto.nombre, producto.precio))

    def buscarProducto(self,numero):
        for producto in self.catalogo:
            if producto.codigo == numero:
                return producto

if __name__ == "__main__":
    tienda = Tienda()
    carro = Carro()
    while True:
        tienda.menu()
        item_ingresado=input("Ingresa un producto a comprar (numero,cantidad): ")
        if item_ingresado == "":
            break
        else:
            item_ingresado = item_ingresado.split(",")
            numero = int(item_ingresado[0])
            producto = tienda.buscarProducto(numero)
            cantidad = int(item_ingresado[1])
            carro.agregar_item(cantidad,producto)
        print(carro)

    print(carro.checkout(0,"usa"))
    print(carro.checkout(1,"usa"))
    print(carro.checkout(0,"Alameda 340 Santiago Chile"))
    print(carro.checkout(1,"Alameda 340 Santiago Chile"))
           