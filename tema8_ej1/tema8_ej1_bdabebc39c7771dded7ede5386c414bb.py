class Producto:
    def __init__(self,codigo,nombre,precio):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
 
 
class Tienda:
    def __init__(self):
        self.catalogo=[]
        self.catalogo.append(Producto(1,"Camisa",10000))
        self.catalogo.append(Producto(2,"Pantalon",20000))
        self.catalogo.append(Producto(3,"Polera",5000))
        self.catalogo.append(Producto(4,"Chaqueta",30000))
 
    def menu(self):
        print("Catalogo:")
        for producto in self.catalogo:
            print(f"{producto.codigo}: {producto.nombre} - ${producto.precio}")
 
 
class Item:
    def __init__(self,producto,cantidad):
        self.producto=producto
        self.cantidad=cantidad
 
 
class Carro:
    def __init__(self):
        self.items=[]
 
    def agregar_item(self,cantidad,producto):
        item=Item(producto,cantidad)
        self.items.append(item)
 
    def __str__(self):
        carrito = "Carro de Compras:\n"
        for item in self.items:
            carrito += f"{item.producto.nombre} - Cantidad: {item.cantidad} - Precio unitario: ${item.producto.precio}\n"
        return carrito
 
    def buscarProducto(self,numero):
        for producto in self.catalogo:
            if producto.codigo == numero:
                return producto
 
    def calcular_descuentos(self):
        descuentos = 0
        for item in self.items:
            descuentos += item.cantidad * item.producto.precio * 0.1  # Descuento del 10% por producto
        return descuentos
 
    def calcular_despacho(self, tipoDespacho):
        valor_productos = 0
        for item in self.items:
            valor_productos += item.cantidad * item.producto.precio
        if tipoDespacho == 0:  # Despacho Aéreo Normal: 20% del valor de los productos
            return valor_productos * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express: 30% del valor de los productos
            return valor_productos * 0.3
        else:
            return 0
 
    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            return True
        return False
 
    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        impuesto = 0
        if self.calcular_impuesto(direccion):
            impuesto = (sum(item.cantidad * item.producto.precio for item in self.items) - descuentos + despacho) * 0.2
        total = sum(item.cantidad * item.producto.precio for item in self.items) - descuentos + despacho + impuesto
        return total
 
 
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

           