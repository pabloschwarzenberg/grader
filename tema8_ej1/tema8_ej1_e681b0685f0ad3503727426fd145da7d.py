class Producto:
    def __init__(self,codigo,nombre,stock,precio):
        self.codigo=codigo
        self.stock=stock
        self.precio=precio
        self.nombre=nombre

    def __eq__(self,other):
        if self.codigo == other.codigo:
            return True
        else:
            return False

class Item:
    def __init__(self,cantidad,producto):
        self.cantidad=cantidad
        self.producto=producto

class Carro:
    def __init__(self):
        self.lista_de_productos=[]
        self.descuento=0
        self.total=0
        self.direccion=""

    def agregar_item(self,cantidad,producto):
        for item in self.lista_de_productos:
            if item.producto == producto:
                if cantidad==0:
                    self.lista_de_productos.remove(item)
                else:
                    item.cantidad=cantidad
                return
        item=Item(cantidad,producto)
        self.lista_de_productos.append(item)          

    def checkout(self,tipoDespacho,direccion):
        self.total = 0
        self.descuento = 0
        descuento_1 = 0
        descuento_2 = 0
        for elemento in self.lista_de_productos:
            self.total += elemento.cantidad * elemento.producto.precio
            if elemento.producto.codigo == 1 or elemento.producto.codigo == 2 or elemento.producto.codigo == 3:
                descuento_1 += 1
            if elemento.producto.codigo == 4 or elemento.producto.codigo == 5:
                descuento_2 += 1
        if descuento_1 == 3:
            self.descuento += 0.2
        if descuento_2 == 2:
            self.descuento += 0.15
        if self.descuento != 0:
            self.total -= self.total * self.descuento
            print(self.total)
        if tipoDespacho == 0:
            print(0)
            self.total += self.total * 0.2
            print(self.total)
        elif tipoDespacho == 1:
            print(1)
            self.total += self.total * 0.3
            print(self.total)
        direccion = direccion.lower()
        if direccion.find("chile") != -1:
            print("chile")
            self.total = self.total * 1.2
            print(self.total)
        self.total = round(self.total, 0)
        return self.total

    def __repr__(self):
        s="Carro de Compras:\n"
        for item in self.lista_de_productos:
            s=s+"{0}: {1}\n".format(item.cantidad,item.producto.nombre)
        return s

class Tienda:
    def  __init__(self):
        self.catalogo=[]
        producto=Producto(1,"Juego Pokemon Y",10,31.51)
        self.catalogo.append(producto)
        producto=Producto(2,"Nintendo 3DS",5,190.95)
        self.catalogo.append(producto)
        producto=Producto(3,"Juego Mario Kart",10,29.96)
        self.catalogo.append(producto)
        producto=Producto(4,"Playstation 4",10,399)
        self.catalogo.append(producto)
        producto=Producto(5,"Fifa 14",10,41.95)
        self.catalogo.append(producto)

    def menu(self):
        for producto in self.catalogo:
            print("{0}: {1} ${2}".format(
                producto.codigo,producto.nombre,producto.precio))

    def buscarProducto(self,numero):
        for producto in self.catalogo:
            if producto.codigo==numero:
                return producto

if __name__ == "__main__":
    tienda=Tienda()
    carro=Carro()
    while True:
        tienda.menu()
        item_ingresado=input("Ingresa un producto a comprar (numero,cantidad): ")
        if item_ingresado=="":
            break
        else:
            item_ingresado=item_ingresado.split(",")
            numero=int(item_ingresado[0])
            producto=tienda.buscarProducto(numero)
            cantidad=int(item_ingresado[1])
            carro.agregar_item(cantidad,producto)
        print(carro)

    print(carro.checkout(0,"usa"))
    print(carro.checkout(1,"usa"))
    print(carro.checkout(0,"Alameda 340 Santiago Chile"))
    print(carro.checkout(1,"Alameda 340 Santiago Chile"))
            