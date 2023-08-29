p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
      productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carro = {}
descuento_aplicado = False

def agregar_producto(producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def imprimir_carro():
    for producto, cantidad in carro.items():
        nombre = productos[producto]["nombre"]
        precio = productos[producto]["precio"]
        print(f"Producto: {nombre} - Cantidad: {cantidad} - Precio unitario: {precio}")

def aplicar_descuento():
    global descuento_aplicado
    if len(carro) >= 3 and all(producto in carro for producto in [1, 2, 3]):
        descuento_aplicado = True
        for producto in [1, 2, 3]:
            carro[producto] *= 0.8
    elif len(carro) >= 2 and all(producto in carro for producto in [4, 5]):
        descuento_aplicado = True
        for producto in [4, 5]:
            carro[producto] *= 0.85

def calcular_total():
    total = 0
    for producto, cantidad in carro.items():
        precio = productos[producto]["precio"]
        total += precio * cantidad
    if descuento_aplicado:
        total = round(total, 1)
    return total

if __name__ == "__main__":
    while True:
        orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")
        
        if orden == "ver":
            imprimir_carro()
        elif orden == "checkout":
            aplicar_descuento()
            total = calcular_total()
            print("Total a pagar:", total)
            break
        else:
            producto, cantidad = orden.split(",")
            producto = int(producto)
            cantidad = int(cantidad)
            agregar_producto(producto, cantidad)
