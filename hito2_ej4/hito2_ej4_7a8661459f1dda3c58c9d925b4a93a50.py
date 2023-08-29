def agregar(carrito,string):

    compra = string.split(' ')
    carrito.append([int(compra[0]),int(compra[1])])

    return carrito
def ver(carrito,productos):
    print('Carrito de Compras')
    m = 1
    for c in carrito:
        print("Compra "+str(m))
        for j in productos:
            if int(c[0]) == j[0]:
                print('Codigo: '+str(j[0]))
                print('Nombre: '+j[1])
                print('Precio unitario: '+str(round(j[2],1)))
                descuento = 0
                if int(j[0]) == 1 or int(j[0]) == 2 or int(j[0]) == 3:
                    descuento = float(j[-1])*0.2
                else:
                    descuento = float(j[-1])*0.15
                print('Descuento: '+str(round(descuento,1)))
                print('Cantidad: '+str(c[1]))
        m += 1
    
def checkout(carrito,productos):    
    print('Compras ')
    total = 0
    for c in carrito:
        for j in productos:
            if int(c[0]) == int(j[0]):
                print('Codigo: '+str(j[0]))
                print('Nombre: '+j[1])
                print('Precio unitario: '+str(round(j[-1],1)))
                descuento = 0
                if int(j[0]) == 1 or int(j[0]) == 2 or int(j[0]) == 3:
                    descuento = float(j[-1])-float(j[-1])*0.2
                else:
                    descuento = float(j[-1])-float(j[-1])*0.15
                print('Descuento: '+str(round(descuento,1)))
                print('Cantidad: '+str(c[1]))
                print('Precio a Pagar(con descuento): '+str(round(descuento*int(c[1]),1)))
                
                total += descuento*int(c[1])
    print('Total a pagar: '+str(round(total,1)))
    return total

if __name__ == "__main__":
    opcion = 1
    productos = []
    productos.append([1,"Pokemon X",33.77])
    productos.append([2,"Nintendo XL",203])
    productos.append([3,"Mario Kart 7",27.58])
    productos.append([4,"PlayStation 4",348.00])
    productos.append([5,"FIFA 16",51.19])
    carrito = []
    while opcion != 0:
        print('1: Agregar producto al carro de compra')
        print('2: Mostrar el carro de compra')
        print('3: Autorizar la compra')
        print('0: Salir')

        opcion = int(input('Opcion: '))
    
        if opcion == 1:
            compra = input("Compra:")
            carrito = agregar(carrito,compra)
        elif opcion == 2:
            ver(carrito,productos)
        elif opcion == 3:
            juguetes = checkout(carrito,productos)
        elif opcion == 0:
            print('Saliendo ...')
        else:
            print('Error en opcion ...')
