class CarroCompras:
    def __init__(self):
        self.carro = {}
    
    def agregar_producto(self, producto, cantidad):
        if producto in self.carro:
            self.carro[producto] += cantidad
        else:
            self.carro[producto] = cantidad
    
    def mostrar_productos(self):
        for producto, cantidad in self.carro.items():
            print(f"Producto {producto}: {cantidad}")
    
    def checkout(self):
        total = 0
        descuento = 0
        
        if all(producto in self.carro for producto in ["1", "2", "3"]):
            total += 33.77 * self.carro["1"]
            total += 203 * self.carro["2"]
            total += 27.58 * self.carro["3"]
            descuento = 0.2
        elif all(producto in self.carro for producto in ["4", "5"]):
            total += 348 * self.carro["4"]
            total += 51.19 * self.carro["5"]
            descuento = 0.15
        else:
            print("No se aplica descuento")
            return
        
        total -= total * descuento
        print(f"Total a pagar: ${round(total, 1)}")


if __name__ == "__main__":
    carro = CarroCompras()

    while True:
        orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")
        
        if orden == "ver":
            carro.mostrar_productos()
        elif orden == "checkout":
            carro.checkout()
            break
        else:
            producto, cantidad = orden.split(",")
            carro.agregar_producto(producto, int(cantidad))
