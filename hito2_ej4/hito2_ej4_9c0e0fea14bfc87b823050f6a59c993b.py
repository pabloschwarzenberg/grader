
#LISTADO CON LOS PRODUCTOS Y SUS RESPECTIVOS CODIGOS
p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

#Contador de la cantidad de productos, cantidad y total
contador_while = 1
contador_while2 = 1
contador_productos=0
total=0
contador_cantidad=0
total_productos=""
print("Para ver tu carrito (ver)")
print("Para pagar tu compra (checkout)")
while contador_while == 1:  #Iniciamos el ciclo para que el usuario decida cuando pagar
    while contador_while2 == 1: #Iniciamos el 2do ciclo para que el usuario decida cuando pagar
        producto = input("Ingresa el producto: ")#String que pide al usuario el producto y su cantidad
        palabra = str(producto)
        producto_str = str(producto[0])
        if(producto_str == str(1)): #CODIGO PARA EL PRODUCTO 1
            cantidad_str = float(str(producto[2]))
            precio_producto1 = float(str(p1[2]))
            contador_productos+= 1
            contador_cantidad+= cantidad_str
            total1= (((p1[2] * cantidad_str) * 20)/100)
            total += (p1[2] * cantidad_str) - total1
            total_producto = precio_producto1 * cantidad_str
            print(total_producto)
            contador_while2 = 1
            continue 

        else:
            if(producto_str == str(2)): #CODIGO PARA EL PRODUCTO 2
                cantidad_str = float(str(producto[2]))
                precio_producto1 = float(str(p2[2]))
                contador_productos += 1
                contador_cantidad += cantidad_str
                total1 = (((p2[2] * cantidad_str) * 20) / 100)
                total += (p2[2] * cantidad_str) - total1
                total_producto = precio_producto1 * cantidad_str
                print(total_producto)
                contador_while2 = 1
                continue
            else:
                if (producto_str == str(3)):  # CODIGO PARA EL PRODUCTO 3
                    cantidad_str = float(str(producto[2]))
                    precio_producto1 = float(str(p3[2]))
                    contador_productos += 1
                    contador_cantidad += cantidad_str
                    total1 = (((p3[2] * cantidad_str) * 20) / 100)
                    total += (p3[2] * cantidad_str) - total1
                    total_producto = precio_producto1 * cantidad_str
                    print(total_producto)
                    contador_while2 = 1
                    continue
                else:
                    if (producto_str == str(4)):  # CODIGO PARA EL PRODUCTO 4
                        cantidad_str = float(str(producto[2]))
                        precio_producto1 = float(str(p4[2]))
                        contador_productos += 1
                        contador_cantidad += cantidad_str
                        total1 = (((p4[2] * cantidad_str) * 15) / 100)
                        total += (p4[2] * cantidad_str) - total1
                        total_producto = precio_producto1 * cantidad_str
                        print(total_producto)
                        contador_while2 = 1
                        continue
                    else:
                        if (producto_str == str(5)):  # CODIGO PARA EL PRODUCTO 5
                            cantidad_str = float(str(producto[2]))
                            precio_producto1 = float(str(p5[2]))
                            contador_productos += 1
                            contador_cantidad += cantidad_str
                            total1 = (((p5[2] * cantidad_str) * 15) / 100)
                            total += (p5[2] * cantidad_str) - total1
                            total_producto = precio_producto1 * cantidad_str
                            print(total_producto)
                            contador_while2 = 1
                            continue
                        else:
                            if (palabra == "checkout"):# CODIGO PARA PAGAR
                                print(round(total, 1)) # Valor redondeado a 1 decimal y con los porcentajes correspondientes
                                contador_while2 = 0
                                continue
                            else:
                                if (palabra == "ver"):# CODIGO PARA VER EL CARRITO
                                    print("1: Juego Pokemon X para Nintendo 3DS, USD 33.77")
                                    print("2: Nintendo 3DS XL, USD 203")
                                    print("3: Juego Mario Kart 7 para Nintendo 3DS, USD 27.58")
                                    print("4: PlayStation 4, USD 348.00")
                                    print("5: FIFA 16, PlayStation 4, USD 51.19")
                                    contador_while2 = 1
                                    continue