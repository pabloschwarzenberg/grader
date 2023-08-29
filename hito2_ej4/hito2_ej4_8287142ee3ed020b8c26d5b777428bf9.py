class CarroCompras:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, producto, cantidad):
        if producto not in self.productos:
            self.productos[producto] = 0
        self.productos[producto] += cantidad
    
    def ver_productos(self):
        for producto, cantidad in self.productos.items():
            print("F""Producto {producto}: {cantidad} unidades")
    
    def checkout(self):
        total = 0
        descuento = 0
        
        # Calcular el valor total y aplicar descuentos si corresponde
        if "1" in self.productos and "2" in self.productos and "3" in self.productos:
            total += self.productos["1"] * 33.77
            total += self.productos["2"] * 203
            total += self.productos["3"] * 27.58
            descuento = 0.2
        
        if "4" in self.productos and "5" in self.productos:
            total += self.productos["4"] * 348
            total += self.productos["5"] * 51.19
            descuento = 0.15
        
        total -= total * descuento
        total = round(total, 1)
        
        print("f""Total a pagar: USD {total}")


carro = CarroCompras()

while True:
    orden = input("Ingresa una orden (producto,cantidad / ver / checkout): ")
    
    if orden == "ver":
        carro.ver_productos()
    elif orden == "checkout":
        carro.checkout()
        break
    else:
        try:
            producto, cantidad = orden.split(",")
            carro.agregar_producto(producto, int(cantidad))
        except ValueError:
            print("Orden inválida. Ingresa en el formato 'producto,cantidad'.")
