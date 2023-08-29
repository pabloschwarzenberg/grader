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
        
        # encontrar el total del carro
        queProductos = []
        self.total = 0
        for item in self.lista_de_productos:
            self.total += float(item.cantidad)*float(item.producto.precio)
        
        # aplicar el descuento
        self.total = self.total * 0.80
        
        # encontrar los descuentos
        # iteramos por todos los productos
        #for i in range(len(tienda.catalogo)):
        #    print i
            #print item.cantidad
        
        
        
#         if item.cantidad !=0:
#             queProductos.append(1)
#         else:
#             queProductos.append(0)
        
#         print (queProductos)
                
        # identificar los descuentos
        '''
        Si se agregan los productos 1, 2 y 3 al carro, se aplica un descuento del 20% del valor conjunto. 
        Lo mismo ocurre, si se agregan los productos 4 y 5 al carro, se les aplica un descuento del 15%. 
        '''
        
        
            
        # analizar tipo de despacho
        if tipoDespacho == 0:
            self.total = 1.2*self.total
        else:
            self.total = 1.3*self.total
        
        # si direccion de despacho es en Chile, agregar un 20% de IVA
        if ("chile" in direccion) or ("Chile" in direccion):
            self.total = 1.2 * self.total
                
        #return "{0:0.f}".format(self.total)
        return int(round(self.total))
    
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
        item_ingresado=raw_input("Ingresa un producto a comprar (numero,cantidad): ")
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
           