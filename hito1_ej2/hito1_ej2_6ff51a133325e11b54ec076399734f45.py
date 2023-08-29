hora=int(input("Ingrese hora de llamada de 0 a 23: "))
celular=int(input("Ingrese numero telefonico en 8 digitos: "))
c1=(celular%1000)
c2=(celular//100000)


if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora < 14:
    if c1 == 909:
         print(("CONTESTAR"))
    else:
        print("NO CONTESTAR")
elif hora >= 17 and hora <= 19:
    if c2 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora > 19:
     print("NO CONTESTAR")
