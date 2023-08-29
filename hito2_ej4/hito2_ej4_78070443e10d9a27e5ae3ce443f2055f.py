def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_carro(carro):
    print("Carro de compras:")
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def calcular_total(carro):
    descuento = 0
    
    if '1' in carro and '2' in carro and '3' in carro:
        descuento = 0.2
    elif '4' in carro and '5' in carro:
        descuento = 0.15
    
    total = 0
    for producto, cantidad in carro.items():
        if producto == '1':
            total += 33.77 * cantidad
        elif producto == '2':
            total += 203 * cantidad
        elif producto == '3':
            total += 27.58 * cantidad
        elif producto == '4':
            total += 348 * cantidad
        elif producto == '5':
            total += 51.19 * cantidad
    
    total -= total * descuento
    return round(total, 1)

def realizar_checkout(carro):
    total = calcular_total(carro)
    print("Checkout:")
    mostrar_carro(carro)
    print(f"Total a pagar: USD {total}")

if __name__ == "__main__":
    carro = {}
    
    while True:
        accion = input("Ingrese una acción (agregar, ver, checkout): ")
        
        if accion == "agregar":
            entrada = input("Ingrese el producto y la cantidad (ejemplo: 5,2): ")
            producto, cantidad = entrada.split(",")
            agregar_producto(carro, producto, int(cantidad))
        elif accion == "ver":
            mostrar_carro(carro)
        elif accion == "checkout":
            realizar_checkout(carro)
            break
        else:
            print("Acción inválida. Por favor, ingrese una acción válida.")


