productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203.00},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carro = {}

def agregar_producto(producto_id, cantidad):
    if producto_id in carro:
        carro[producto_id] += cantidad
    else:
        carro[producto_id] = cantidad

def ver_productos():
    for producto_id, cantidad in carro.items():
        producto = productos[producto_id]
        print("Producto: {}\tCantidad: {}".format(producto["nombre"], cantidad))

def checkout():
    total = 0
    
    for producto_id, cantidad in carro.items():
        producto = productos[producto_id]
        precio = producto["precio"]
        
        if set([1, 2, 3]).issubset(set(carro.keys())):
            precio *= 0.8
        elif set([4, 5]).issubset(set(carro.keys())):
            precio *= 0.85
        
        total += precio * cantidad
    
    print("Total a pagar: ${:.1f}".format(round(total, 1)))
    carro.clear()

if __name__ == "__main__":

    while True:
        orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")
        orden = orden.lower().strip()
        
        if orden == "ver":
            ver_productos()
        elif orden == "checkout":
            checkout()
        else:
            try:
                producto_id, cantidad = orden.split(",")
                producto_id = int(producto_id)
                cantidad = int(cantidad)
                agregar_producto(producto_id, cantidad)
                print("Producto agregado al carro.")
            except ValueError:
                print("Orden inválida. Por favor, intente nuevamente.")