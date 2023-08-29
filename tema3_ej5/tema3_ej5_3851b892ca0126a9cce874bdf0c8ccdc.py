def repr(self):
        s="Carro de Compras:\n"
        for item in self.lista_de_productos:
            s=s+"{0}: {1}\n".format(item.cantidad,item.producto.nombre)
        return s

class Tienda:
    def  init(self):
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
name=0
if name == "main":
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