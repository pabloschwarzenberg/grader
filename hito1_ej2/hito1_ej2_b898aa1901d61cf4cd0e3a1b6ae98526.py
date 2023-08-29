#Contestador de celular
numero=int(input("Ingrese el numero de la llamada: "))
hora=int(input("Ingrese la hora de la llamda"))

if hora==0 and hora==7:
    print("CONTESTAR")
if hora<14 and numero%1000==909:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
if hora<=19 and hora>=17:
    if numero/100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if hora>19:
    print("NO CONTESTAR")


      