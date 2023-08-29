celular=list(input("Ingrese un numero de telefono"))
hora=int(input("Ingrese hora:"))
if hora>=0 and hora<=7:
    print("Contestar")
if hora>7 and hora<=14:
        if celular[5]=="9" and celular[6]=="0" and  celular[7]=="9":
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
if hora>14 and hora<17:
    print("NO CONTESTAR")
if hora>=17 and hora<=19 :
    if celular[0]=="8" and celular[1]=="7" and celular[2]=="7":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if hora>19 and hora<24:
    print("NO CONTESTAR")

