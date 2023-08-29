p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
def ver (lista):
    cantidad_codigo_p1 = 0
    cantidad_codigo_p2 = 0
    cantidad_codigo_p3 = 0
    cantidad_codigo_p4 = 0
    cantidad_codigo_p5 = 0
    total = 0

    for producto in lista:
        aux = producto.split(",")

        if aux[1] == "1":
            cantidad_codigo_p1 = cantidad_codigo_p1 + int(aux[0])
        elif aux[1] == "2":
            cantidad_codigo_p2 = cantidad_codigo_p2 + int(aux[0])
        elif aux[1] == "3":
            cantidad_codigo_p3 = cantidad_codigo_p3 + int(aux[0])
        elif aux[1] == "4":
            cantidad_codigo_p4 = cantidad_codigo_p4 + int(aux[0])
        elif aux[1] == "5":
            cantidad_codigo_p5 = cantidad_codigo_p5 + int(aux[0])
    if cantidad_codigo_p1 > 0:
        print (p1 [1] + ":" + str(cantidad_codigo_p1) + " unidades ")
        print ("")
    if cantidad_codigo_p2 > 0:
        print (p2 [1] + ":" + str(cantidad_codigo_p2) + " unidades ")
        print("")
    if cantidad_codigo_p3 > 0:
        print (p3 [1] + ":" + str(cantidad_codigo_p3) + " unidades ")
        print("")
    if cantidad_codigo_p4 > 0:
        print (p4 [1] + ":" + str(cantidad_codigo_p4) + " unidades ")
        print("")
    if cantidad_codigo_p5 > 0:
        print (p5 [1] + ":" + str(cantidad_codigo_p5) + " unidades ")
        print("")

def mostrar_checkout (lista):

    cantidad_codigo_p1 = 0
    cantidad_codigo_p2 = 0
    cantidad_codigo_p3 = 0
    cantidad_codigo_p4 = 0
    cantidad_codigo_p5 = 0
    total = 0

    for producto in lista:
        aux = producto.split(",")

        if aux [1] == "1":
            cantidad_codigo_p1 = cantidad_codigo_p1 + int(aux [0])
        elif aux [1] == "2":
            cantidad_codigo_p2 = cantidad_codigo_p2 + int(aux [0])
        elif aux [1] == "3":
            cantidad_codigo_p3 = cantidad_codigo_p3 + int(aux [0])
        elif aux [1] == "4":
            cantidad_codigo_p4 = cantidad_codigo_p4 + int(aux [0])
        elif aux [1] == "5":
            cantidad_codigo_p5 = cantidad_codigo_p5 + int(aux [0])

    while cantidad_codigo_p1 > 0 and cantidad_codigo_p2 > 0 and cantidad_codigo_p3 > 0:
        total = total + ((p1 [2] + p2 [2] + p3 [2]) * 80) / 100
        cantidad_codigo_p1 = cantidad_codigo_p1 - 1
        cantidad_codigo_p2 = cantidad_codigo_p2 - 1
        cantidad_codigo_p3 = cantidad_codigo_p3 - 1

    while cantidad_codigo_p4 > 0 and cantidad_codigo_p5 > 0:
        total = total + ((p4[2] + p5[2]) * 85) / 100
        cantidad_codigo_p4 = cantidad_codigo_p4 - 1
        cantidad_codigo_p5 = cantidad_codigo_p5 - 1

    total = total + cantidad_codigo_p1 * p1[2]
    total = total + cantidad_codigo_p2 * p2[2]
    total = total + cantidad_codigo_p3 * p3[2]
    total = total + cantidad_codigo_p4 * p4[2]
    total = total + cantidad_codigo_p5 * p5[2]

    return round (total, 1)

if __name__ == "__main__":
    x = 0
    lista = []
    while x != "1":

        print ("Productos: ")
        print (p1 [1] + ":" + str (p1[2]) + " Codigo: " + str(p1[0]))
        print (p2 [1] + ":" + str (p2[2]) + " Codigo: " + str(p2[0]))
        print (p3[1] + ":" + str(p3[2]) + " Codigo: " + str(p3[0]))
        print (p4 [1] + ":" + str (p4[2]) + " Codigo: " + str(p4[0]))
        print (p5[1] + ":" + str(p5[2]) + " Codigo: " + str(p5[0]))

        y = str (input("Ingrese su Producto de la forma Cantidad, Codigo. Si quiere terminar su compra escriba total. Si quiere ver los carrito escriba ver: "))

        if y == "checkout":
            x = y
            mostrar_checkout (lista)
        elif y == "ver":
            ver (lista)
        else:
            lista.append (y)
