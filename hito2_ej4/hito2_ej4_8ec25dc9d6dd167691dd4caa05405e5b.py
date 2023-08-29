class CarritoCompras:
    def __init__(self):
        self.productos = {}
        self.descuento = 0
    
    def agregar_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad
    
    def ver_productos(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            for producto, cantidad in self.productos.items():
                print("Producto {}: {} unidad(es).".format(producto, cantidad))
    
    def calcular_total(self):
        total = 0
        for producto, cantidad in self.productos.items():
            precio = self.obtener_precio(producto)
            total += precio * cantidad
        
        if self.descuento > 0:
            total -= total * self.descuento
        
        return round(total, 1)
    
    def obtener_precio(self, producto):
        precios = {
            1: 33.77,
            2: 203,
            3: 27.58,
            4: 348.00,
            5: 51.19
        }
        return precios.get(producto, 0)
    
    def aplicar_descuento(self):
        productos_agregados = self.productos.keys()
        
        if set([1, 2, 3]).issubset(productos_agregados):
            self.descuento = 0.2
        elif set([4, 5]).issubset(productos_agregados):
            self.descuento = 0.15
        else:
            self.descuento = 0

carrito = CarritoCompras()

while True:
    orden = input("Ingresa la acción que deseas realizar (producto,cantidad / ver / checkout): ")
    
    if orden == "ver":
        carrito.ver_productos()
    elif orden == "checkout":
        carrito.aplicar_descuento()
        total = carrito.calcular_total()
        print("Total a pagar: USD", total)
        break
    else:
        try:
            producto, cantidad = map(int, orden.split(","))
            carrito.agregar_producto(producto, cantidad)
        except ValueError:
            print("Orden inválida. Intenta nuevamente.")