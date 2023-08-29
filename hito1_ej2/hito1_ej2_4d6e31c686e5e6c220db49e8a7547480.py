jane=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada:"))
a=jane%1000
if 0<=hora<=7:
    print("CONTESTAR")
if 7<hora<14:
    if a==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if 14<=hora<=19:
    if 14<=hora<=17:
        print("NO CONTESTAR")
    else:
        if 87699999<jane<87800000:
             print("NO CONTESTAR")
        else:
             print("CONTESTAR")
if 19<hora<23:
    print("NO CONTESTAR")
             