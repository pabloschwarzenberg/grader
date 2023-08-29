numero=int(input("Ingrese numero de telefono "))
hora=int(input("Ingrese hora de llamada" ))
if 0<=hora<=6:
    print("CONTESTAR")
else:
    if 7<=hora<=13:
        if numero%1000==909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif 17<=hora<19:
        if numero//100000==877:
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
    else:
        print("NO CONTESTAR")