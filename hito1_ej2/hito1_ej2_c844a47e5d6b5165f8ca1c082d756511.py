#Contestador de celular
numero=(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada: "))
if hora>=0 and hora<7:
    print("CONTESTAR")
elif hora>7 and hora<14:
    if numero[5:8]=="909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora>14 and hora<19:
    if numero[0:3]=="877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora>19 and hora<24:
    print("NO CONTESTAR")