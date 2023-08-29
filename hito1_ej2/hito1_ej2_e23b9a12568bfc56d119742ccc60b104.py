#Contestador de celular
numero= str(input("Ingrese su numero telefónico de 8 digitos: "))
hora= int(input("Ingrese la hora de la llamada: "))
f=numero[5:9]
i=numero[0:3]
int(f)
int(i)
if (hora>=0 and hora<=7):
    print("CONTESTAR")
elif (hora>=8 and hora<14):
    if (f=="909"):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif (hora>=14 and hora<17):
    print("NO CONTESTAR")
elif (hora>=15 and hora<=19):
    if (i=="877"):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif(hora>19):
    print("NO CONTESTAR")