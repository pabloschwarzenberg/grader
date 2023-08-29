productos=[
    [1, "Pokemon X", 33.77],
    [2, "Nintendo XL", 203],
    [3, "Mario Kart 7", 27.58],
    [4, "PlayStation 4", 348.00],
    [5, "FIFA 16", 51.19]
]
carro=[]
descuento_total=0

def agregar_al_carro(producto_id,cantidad):
    global carro
    carro.append((producto_id,cantidad))
def calcular_descuento():
    global carro,descuento_total
    producto_ids=[producto_id for producto_id,_ in carro]

    if set([1,2,3]).issubset(set(producto_ids)):
        descuento_total=sum(productos[2] * cantidad for producto_id, cantidad in carro if producto_id <= 3) * 0.2
    elif set([4, 5]).issubset(set(producto_ids)):
        descuento_total = sum(productos[2] * cantidad for producto_id, cantidad in carro if producto_id >= 4) * 0.15

def mostrar_carro():
    global carro
    print("Productos en el carro:")
    for producto_id, cantidad in carro:
        producto = next((p for p in productos if p[0] == producto_id), None)
        if producto:
            print("Cantidad: {} - Producto: {} - Precio unitario: {}".format(cantidad, producto[1], producto[2]))

def checkout():
    global carro, descuento_total
    calcular_descuento()
    
    print("Resumen del carro:")
    mostrar_carro()
    print("Descuento total: {:.1f}".format(descuento_total))
    precio_total = sum(producto[2] * cantidad for producto_id, cantidad in carro for producto in productos if producto[0] == producto_id) - descuento_total
    print(f"Precio total a pagar: {round(precio_total, 1)}")

while True:
    orden = input("Ingresa una orden (agregar, ver, checkout): ")
    if orden == "agregar":
        producto_id, cantidad = map(int, input("Ingresa el producto y la cantidad separados por coma: ").split(","))
        agregar_al_carro(producto_id, cantidad)
    elif orden == "ver":
        mostrar_carro()
    elif orden == "checkout":
        checkout()
        break
    else:
        print("Orden inválida. Intenta nuevamente.")    