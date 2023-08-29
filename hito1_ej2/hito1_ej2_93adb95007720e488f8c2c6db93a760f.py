#Contestador de celular
numtel = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

if len(str(numtel)) > 8 or hora > 24:
    print("El número solo puede contener 8 dígitos")
    exit()

else:
    if hora in range(0, 7):
        print("CONTESTAR")
    #|||||||||||||||||||||||||||||
    elif hora in range(8, 14) and numtel % 1000 != 909:
        print("NO CONTESTAR")
    elif hora in range(8, 14) and numtel % 1000 == 909:
        print("CONTESTAR")
    #|||||||||||||||||||||||||||||
    elif hora in range(17, 19) and numtel % 100000000 // 100000 == 877:
        print("NO CONTESTAR")
    elif hora in range(17, 19) and numtel % 100000000 // 100000 != 877:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")