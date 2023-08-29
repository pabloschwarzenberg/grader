numero= int(input("Ingrese su numero de telefono (8 cifras): "))
hora=int(input("Ingrese la hora entre 0 y 23: "))
numfinal = 909
numinicial = 877
if hora > 0 and hora < 7:
    print("Contestar (puede ser una emergencia)")
elif hora > 7 and hora < 14:
    if numfinal == 909:
        print("Contestar")
    else:
        print("contestar")
elif hora > 17 and hora < 19:
    if numinicial == 877:
        print("No contestar")
    else:
        print("contestar")
elif numinicial == 877:
    print("No contestar")
elif hora > 19:
    print("No Contestar")