p1 = [1,"Pokemon X",33.77]
p2 = [2,"Nintendo XL",203]
p3 = [3,"Mario Kart 7",27.58]
p4 = [4,"PlayStation 4",348.00]
p5 = [5,"FIFA 16",51.19]

productos = {"1": 33.77, "2": 203.00, "3": 27.58, "4": 348.00, "5": 51.19}
carrito = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}

aux = False
while aux != True:
    n = input("Que hacer?: ")

    if n == "ver":
        print(p1, "\n", "-----------------")
        print(p2, "\n", "-----------------")
        print(p3, "\n", "-----------------")
        print(p4, "\n", "-----------------")
        print(p5)

    elif n == "checkout":
        suma = 0
        aux_d1 = False
        aux_d2 = False

        if carrito["1"] > 0 and carrito["2"] > 0 and carrito["3"] > 0:
            neto1 = ((productos["1"] * carrito["1"]) + (productos["2"] * carrito["2"]) + (productos["3"] * carrito["3"]))
            descuento1 = neto1 * 0.8
            aux_d1 = True

        if carrito["4"] > 0 and carrito["5"] > 0:
            neto2 = ((productos["4"] * carrito["4"]) + (productos["5"] * carrito["5"]))
            descuento2 = neto2 * 0.85
            aux_d2 = True
        
        for a in carrito:
          suma += (productos[a] * carrito[a])
        
        if aux_d1 == True:
          suma -= neto1
          suma += descuento1
        if aux_d2 == True:
          suma -= neto2
          suma += descuento2
        suma = round(suma, 2)
        print(suma)
        aux = True
    
    else:
        if n[0] in productos:
            producto = n[0]
        else:
            print("Producto inexistente, por favor ingreselo nuevamente.")
        if int(n[2]) > 0:
            cantidad = int(n[2])
        else:
            print("Cantidad de productos no permitida, por favor ingrese la cantidad nuevamente.")
    
        carrito[producto] += cantidad          
      