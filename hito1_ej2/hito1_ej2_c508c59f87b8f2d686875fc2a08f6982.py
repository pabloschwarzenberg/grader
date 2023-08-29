#Contestador de celular
n= int(input("Ingrese numero telefonico: "))
h= int(input("Ingrese hora de la llamada: "))
if h>=0 and h<=7:
    print ("Resultado: CONTESTAR")
elif h<14:
    if str(n)[5:8]=="909":
        print ("Resultado: CONTESTAR")
    else:
        print ("Resultado: NO CONTESTAR")
elif h>=17 and h<=19:
    if str(n)[0:3] != "877":
        print ("Resultado: CONTESTAR")
    else:
        print ("Resultado: NO CONTESTAR")
elif h>19:
    print ("Resultado: NO CONTESTAR")
else:
    print ("Resultado: NO CONTESTAR")
        