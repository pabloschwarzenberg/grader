#Contestador de celular
telefono=int(input("Ingrese número telefónico: "))
hora=int(input("Ingrese hora (ejemplo19): "))
if 0<hora<7:
    print("CONTESTAR")
if hora<14 and 0<=telefono%3<=2:
    print("CONTESTAR")
else:
        if hora<14:
            print("NO CONTESTAR")
if 17<hora<19 and 87700000<=telefono<87800000:
    print("NO CONTESTAR")
else:
    if 17<hora<19:
        print("CONTESTAR")
if hora>19:
    print("NO CONTESTAR")