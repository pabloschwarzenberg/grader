p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

carro = []
lista1 = []
lista2 = []
checkout = []
def pedirNumeroEntero():
 
    correcto=False
    opcion=""
    while(not correcto):
        try:
            opcion = input("Que producto deseas comprar?")
            correcto=True
        except ValueError:
            print('No existe el producto')
     
    return opcion

salir = False

while not salir:
    print("Buenos días")

    print("1. Pokemon X")
    print("2. Nintendo XL")
    print("3. Mario Kart 7")
    print("4. PlayStation 4")
    print("5. FIFA 16")
    print("6. Ver")
    print("7. Checkout")
    print("8. Salir")
    opcion = pedirNumeroEntero()
    if opcion == "1":
        cantidad = input("Cuantos desea comprar?")
        carro.append([opcion,cantidad])
        print(carro)
        
    if opcion == "2":
        cantidad = input("Cuantos desea comprar?")
        carro.append([opcion,cantidad])
        print(carro)
        
    if opcion =="3":
        cantidad = input("Cuantos desea comprar?")
        carro.append([opcion,cantidad])
        print(carro)
        
    if opcion == "4":
        cantidad = input("Cuantos desea comprar?")
        carro.append([opcion,cantidad])
        print(carro)
        
    if opcion == "5":
        cantidad = input("Cuantos desea comprar?")
        carro.append([opcion,cantidad])
        print(carro)
        
    if opcion == "6":
        x = 0
        y = 1
        for i in range(0,len(carro)):
            if(carro[i][x] == "1"):
                print( p1[1],"Cantidad:",carro[i][y])
            if(carro[i][x] == "2"):
                print(p2[1],"Cantidad:",carro[i][y])
            if(carro[i][x] == "3"):
                print(p3[1],"Cantidad:",carro[i][y])
            if(carro[i][x] == "4"):
                print(p4[1],"Cantidad:",carro[i][y])
            if(carro[i][x] == "5"):
                print(p5[1],"Cantidad:",carro[i][y])
    if opcion == "7":
        x = 0
        y = 1
        for i in range(0,len(carro)):
            if(carro[i][x] == "1"):
                cantidad = int(carro[i][y]) * p1[2]
                lista1.append(cantidad)
            if(carro[i][x] == "2"):
                cantidad = int(carro[i][y]) * p2[2]
                lista1.append(cantidad)
            if(carro[i][x] == "3"):
                cantidad = int(carro[i][y]) * p3[2]
                lista1.append(cantidad)
            if(carro[i][x] == "4"):
                cantidad = int(carro[i][y]) * p4[2]
                lista2.append(cantidad)
            if(carro[i][x] == "5"):
                cantidad = int(carro[i][y]) * p5[2]
                lista2.append(cantidad)
            sumlista1 = sum(lista1)
            sumlista2 = sum(lista2)

            desclista1 = sumlista1 - (sumlista1 * .20)
            desclista2 = sumlista2 - (sumlista2 * .15)

        print("Precio con el descuento del 20 porciento de los productos 1, 2 y 3: ",desclista1)
        print("Precio con el descuento del 15 porciento de los productos 4 y 5: ", desclista2)

        precio = desclista1 + desclista2

        print("El precio total es: ",round(precio,1))
    if opcion == "8":
        salir = True
      