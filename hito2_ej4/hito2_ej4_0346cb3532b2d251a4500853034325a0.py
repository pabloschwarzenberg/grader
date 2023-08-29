p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_carro(carro):
    print("Productos en el carro:")
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def checkout(carro):
    total = 0

    for producto, cantidad in carro.items():
        if producto == '1' or producto == '2' or producto == '3':
            total += cantidad * 0.8 * precios[producto]
        elif producto == '4' or producto == '5':
            total += cantidad * 0.85 * precios[producto]
    
    total = round(total, 1)
    print(f"Total a pagar: USD {total}")

if __name__ == "__main__":
    carro = {}
    precios = {
        '1': 33.77,
        '2': 203,
        '3': 27.58,
        '4': 348.00,
        '5': 51.19
    }

    while True:
        orden = input("Ingrese la orden (producto,cantidad / ver / checkout): ")

        if orden == "ver":
            mostrar_carro(carro)
        elif orden == "checkout":
            checkout(carro)
            break
        else:
            try:
                producto, cantidad = orden.split(',')
                agregar_producto(carro, producto, int(cantidad))
            except:
                print("Orden inválida. Por favor, ingrese en el formato correcto (producto,cantidad).")
      