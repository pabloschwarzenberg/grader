numero=str(input("Ingrese número telefónico: "))
hora=eval(input("Ingrese hora de la llamada: "))

if 0<hora<7:
    print("CONTESTAR")
elif hora<14:
    if numero[-3:]=="909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17<hora<19:
    if numero[:3]=="877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
