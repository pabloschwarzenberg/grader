class CarroCompras:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, producto, cantidad):
        if producto not in self.productos:
            self.productos[producto] = 0
        self.productos[producto] += cantidad
    
    def ver_productos(self):
        for producto, cantidad in self.productos.items():
            print(f"Producto {producto}: {cantidad} unidades")
    
    def checkout(self, tipoDespacho, direccion):
        total = 0
        descuento = 0
        despacho = 0
        
        # Calcular el valor total y aplicar descuentos
        for producto, cantidad in self.productos.items():
            if producto == "1":
                total += cantidad * 33.77
            elif producto == "2":
                total += cantidad * 203
            elif producto == "3":
                total += cantidad * 27.58
            elif producto == "4":
                total += cantidad * 348
            elif producto == "5":
                total += cantidad * 51.19
        
        if "1" in self.productos and "2" in self.productos and "3" in self.productos:
            descuento = 0.2
        
        if "4" in self.productos and "5" in self.productos:
            descuento = 0.15
        
        total -= total * descuento
        
        # Calcular el valor del despacho
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            despacho = total * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            despacho = total * 0.3
        
        total += despacho
        
        # Calcular impuesto si el despacho es hacia Chile
        if "Chile" in direccion:
            total += total * 0.2
        
        return total


carro = CarroCompras()

while True:
    orden = input("Ingresa una orden (producto,cantidad / ver / checkout): ")
    
    if orden == "ver":
        carro.ver_productos()
    elif orden == "checkout":
        tipo_despacho = int(input("Selecciona el tipo de despacho (0: Aéreo Normal, 1: Aéreo Express): "))
        direccion = input("Ingresa la dirección de despacho: ")
        total_pagar = carro.checkout(tipo_despacho, direccion)
        print("Total a pagar:", total_pagar)
        break
    else:
        try:
            producto, cantidad = orden.split(",")
            carro.agregar_producto(producto, int(cantidad))
        except ValueError:
            print("Orden inválida. Ingresa en el formato 'producto,cantidad'.")
