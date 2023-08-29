# Diccionario que contiene la información de los productos
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Variables para almacenar los productos en el carro
carro = []
total_carro = 0

def agregar_producto(producto_id, cantidad):
    global carro, total_carro
    
    producto_id = int(producto_id)
    cantidad = int(cantidad)
    
    if producto_id in productos:
        producto = productos[producto_id]
        subtotal = producto["precio"] * cantidad
        carro.append((producto_id, producto["nombre"], cantidad, subtotal))
        total_carro += subtotal
        print("Producto agregado al carro.")
    else:
        print("El producto no existe.")

def mostrar_productos():
    if len(carro) > 0:
        print("Productos en el carro:")
        for producto in carro:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}, Subtotal: {producto[3]}")
    else:
        print("El carro está vacío.")

def checkout():
    global carro, total_carro
    
    if len(carro) > 0:
        descuento = 0
        
        # Verificar si se aplica descuento del 20% (productos 1, 2 y 3)
        if all(producto[0] in [1, 2, 3] for producto in carro):
            descuento = total_carro * 0.2
        
        # Verificar si se aplica descuento del 15% (productos 4 y 5)
        if all(producto[0] in [4, 5] for producto in carro):
            descuento = total_carro * 0.15
        
        total_final = total_carro - descuento
        print(f"Total a pagar: {round(total_final, 1)}")
        
        # Reiniciar el carro
        carro = []
        total_carro = 0
    else:
        print("El carro está vacío.")

if __name__ == "__main__":
    while True:
        orden = input("Ingrese su orden (producto,cantidad / ver / checkout): ")
        
        if orden == "ver":
            mostrar_productos()
        elif orden == "checkout":
            checkout()
            break
        else:
            try:
                producto_id, cantidad = orden.split(",")
                agregar_producto(producto_id, cantidad)
            except ValueError:
                print("Orden inválida. Por favor, ingrese en el formato producto,cantidad.")