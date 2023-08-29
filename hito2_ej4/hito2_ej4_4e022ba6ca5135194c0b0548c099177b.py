def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_carro(carro):
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def checkout(carro):
    total = 0
    
    descuento_20 = {'1', '2', '3'}
    descuento_15 = {'4', '5'}
    
    for producto, cantidad in carro.items():
        if producto in descuento_20:
            if producto == '1':
                precio = 33.77
            elif producto == '2':
                precio = 203.00
            elif producto == '3':
                precio = 27.58
            
            total += precio * cantidad * 0.8
        elif producto in descuento_15:
            if producto == '4':
                precio = 348.00
            elif producto == '5':
                precio = 51.19
            
            total += precio * cantidad * 0.85
    
    print(f"Total a pagar: ${total:.1f}")

if __name__ == "__main__":
    carro = {}
    
    while True:
        orden = input("Ingrese su orden (producto,cantidad / ver / checkout): ")
        partes = orden.split(",")
        
        if orden == "ver":
            mostrar_carro(carro)
        elif orden == "checkout":
            checkout(carro)
            break
        elif len(partes) == 2:
            producto = partes[0]
            cantidad = int(partes[1])
            
            agregar_producto(carro, producto, cantidad)
